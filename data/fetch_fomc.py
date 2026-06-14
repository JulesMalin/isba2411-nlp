#!/usr/bin/env python3
"""Fetch one year of FOMC meeting transcripts and build a plain-text corpus.

Downloads the verbatim FOMC meeting transcript PDFs from the Federal Reserve,
extracts their text, lightly cleans it, and concatenates everything into
``data/fomc_corpus.txt`` for use in Milestone 2.

Note: full verbatim transcripts are released on a ~5-year lag, so the default
year (2019) is a complete, fully released set of 8 meetings.

Usage:
    python data/fetch_fomc.py            # default year 2019 -> data/fomc_corpus.txt
    python data/fetch_fomc.py --year 2018
    python data/fetch_fomc.py --keep-pdfs   # also keep the raw PDFs in data/raw/

Requires: pypdf  (pip install pypdf)
"""
import argparse
import os
import re
import sys
import urllib.request

# FOMC meeting dates (YYYYMMDD) by year. Each scheduled meeting has a transcript.
MEETING_DATES = {
    2017: ["20170201", "20170315", "20170503", "20170614",
           "20170920", "20171101", "20171213"],
    2018: ["20180131", "20180321", "20180502", "20180613",
           "20180801", "20180926", "20181108", "20181219"],
    2019: ["20190130", "20190320", "20190501", "20190619",
           "20190731", "20190918", "20191030", "20191211"],
}

URL_TMPL = "https://www.federalreserve.gov/monetarypolicy/files/FOMC{date}meeting.pdf"
# federalreserve.gov rejects the default urllib User-Agent with HTTP 403.
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))


def extract_text(pdf_bytes):
    """Return extracted text from PDF bytes using pypdf."""
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("Missing dependency: pypdf. Install with `pip install pypdf`.")
    import io
    reader = PdfReader(io.BytesIO(pdf_bytes))
    return "\n".join((page.extract_text() or "") for page in reader.pages)


def clean(text):
    """Light cleanup: drop page-footer artifacts, collapse whitespace."""
    # Remove standalone page numbers / footer lines like "January 29-30, 2019  1 of 245"
    text = re.sub(r"^\s*\w+\s+\d+(?:-\d+)?,\s*\d{4}\s+\d+\s+of\s+\d+\s*$",
                  "", text, flags=re.MULTILINE)
    text = re.sub(r"[ \t]+", " ", text)          # collapse runs of spaces/tabs
    text = re.sub(r"\n{3,}", "\n\n", text)        # collapse blank-line runs
    return text.strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--year", type=int, default=2019,
                    help="meeting year to fetch (default: 2019)")
    ap.add_argument("--out", default=os.path.join(HERE, "fomc_corpus.txt"),
                    help="output corpus path (default: data/fomc_corpus.txt)")
    ap.add_argument("--keep-pdfs", action="store_true",
                    help="also save the raw PDFs under data/raw/")
    args = ap.parse_args()

    dates = MEETING_DATES.get(args.year)
    if not dates:
        sys.exit(f"No meeting dates configured for {args.year}. "
                 f"Available: {sorted(MEETING_DATES)}")

    raw_dir = os.path.join(HERE, "raw")
    if args.keep_pdfs:
        os.makedirs(raw_dir, exist_ok=True)

    parts, total_chars = [], 0
    for d in dates:
        url = URL_TMPL.format(date=d)
        print(f"  downloading {url}")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                pdf_bytes = r.read()
        except Exception as e:  # noqa: BLE001
            print(f"  !! skipped {d}: {e}")
            continue
        if args.keep_pdfs:
            with open(os.path.join(raw_dir, f"FOMC{d}meeting.pdf"), "wb") as f:
                f.write(pdf_bytes)
        text = clean(extract_text(pdf_bytes))
        header = f"\n\n===== FOMC MEETING {d[:4]}-{d[4:6]}-{d[6:]} =====\n\n"
        parts.append(header + text)
        total_chars += len(text)
        print(f"     extracted {len(text):,} chars")

    if not parts:
        sys.exit("No transcripts fetched — nothing written.")

    corpus = "".join(parts).strip() + "\n"
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(corpus)
    print(f"\nWrote {args.out}")
    print(f"  meetings: {len(parts)}   chars: {total_chars:,}   "
          f"size: {os.path.getsize(args.out) / 1_048_576:.2f} MB")


if __name__ == "__main__":
    main()
