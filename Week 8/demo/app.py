"""Cobalt Support Copilot, part 3: it answers the customer.

The demo for ISBA 2411 Week 8, Lecture 15. Every stage on screen is a stage from the
lecture, and the sidebar exposes the settings the lecture argues about:

    retrieve   all-MiniLM-L6-v2, the same encoder used in Lectures 13 and 14
    rerank     cross-encoder/ms-marco-MiniLM-L-6-v2, the second pass
    refuse     a threshold on the reranker score, the same shape of decision as the
               confidence threshold in Lecture 13
    generate   Qwen2.5-1.5B-Instruct, greedy by default so answers are reproducible

Run it with:   streamlit run app.py
"""
import json, os, time
import numpy as np
import streamlit as st

HERE = os.path.dirname(os.path.abspath(__file__))
KB   = os.path.join(HERE, "..", "cobalt_kb.json")
ENCODER  = "sentence-transformers/all-MiniLM-L6-v2"
RERANKER = "cross-encoder/ms-marco-MiniLM-L-6-v2"
GENERATOR = "Qwen/Qwen2.5-1.5B-Instruct"

st.set_page_config(page_title="Cobalt Support Copilot", page_icon="🟦", layout="wide")

# --------------------------------------------------------------------- loading
@st.cache_resource(show_spinner=False)
def load():
    """Loading is staged and reported, because an opaque spinner cannot distinguish
    'downloading three gigabytes' from 'hung'. On a warm cache this takes about 25
    seconds; the first run in a fresh Colab downloads the generator and takes minutes."""
    import torch
    from sentence_transformers import SentenceTransformer, CrossEncoder
    from transformers import AutoTokenizer, AutoModelForCausalLM
    dev = "mps" if torch.backends.mps.is_available() else (
          "cuda" if torch.cuda.is_available() else "cpu")
    # float32 doubles the memory for no benefit on a GPU. On a shared Colab GPU that is
    # the difference between loading and an out-of-memory crash.
    dtype = torch.float16 if dev == "cuda" else torch.float32

    with st.status("Starting the copilot…", expanded=True) as status:
        st.write(f"running on **{dev}**")
        st.write("reading Cobalt's help centre…")
        kb = json.load(open(KB))

        st.write(f"loading the encoder and indexing {len(kb)} chunks…")
        enc = SentenceTransformer(ENCODER, device=dev)
        X = enc.encode([f"{d['title']}. {d['section']}. {d['text']}" for d in kb],
                       normalize_embeddings=True, batch_size=32)

        st.write("loading the reranker…")
        rr = CrossEncoder(RERANKER, device=dev)

        st.write("loading the generator, about 3 GB. "
                 "**The first run on a new machine downloads it and can take several "
                 "minutes.** After that it is cached and takes seconds.")
        tok = AutoTokenizer.from_pretrained(GENERATOR)
        gen = AutoModelForCausalLM.from_pretrained(GENERATOR, dtype=dtype).to(dev).eval()

        status.update(label=f"Ready. {len(kb)} chunks indexed, running on {dev}.",
                      state="complete", expanded=False)
    return kb, enc, X, rr, tok, gen, dev, torch

kb, enc, X, rr, tok, gen, DEVICE, torch = load()

# Tested against every example below. The one-shot example and the literal NO_ANSWER
# token both matter: without them a 1.5B model ignores the citation rule and, worse,
# cheerfully invents a feature that does not exist.
SYSTEM = ("You are a Cobalt support agent. You may ONLY use facts from the numbered passages.\n"
          "RULES:\n"
          "1. After EVERY sentence that states a fact, put the passage number in brackets, "
          "e.g. [2].\n"
          "2. If the passages do not answer the ticket, reply with exactly this and nothing "
          "else:\n   NO_ANSWER\n"
          "3. Never name a menu, setting or feature that does not appear in the passages.\n"
          "Example of a good reply:\n"
          "Go to Admin, then Identity Providers, and choose Reconnect [1]. Your signing "
          "certificate must be current or the reconnect will fail [1].")

EXAMPLES = {
 "SSO broken for the whole team":
   "Our SSO through Okta stopped working after the weekend. Nobody on our team can sign in.",
 "Charged twice":
   "We were charged twice this month for the same seats. We need a refund on the duplicate.",
 "Export times out":
   "Exporting anything over about 10,000 rows just times out. We need the full extract.",
 "Sync stopped with no error":
   "The nightly sync silently stopped three days ago and nothing alerted us.",
 "→ Retrieval fails, and watch what it does":
   "Sarah left last week but her account still has access. Please revoke it.",
 "→ Not in the documentation at all":
   "The date picker will not let me select anything before 2024, and there is no tooltip.",
 "→ A feature Cobalt does not have":
   "Please add dark mode. Our team works late and the white background is rough.",
}

# --------------------------------------------------------------------- sidebar
st.sidebar.title("The dials")
st.sidebar.caption("Every one of these is a decision from tonight's lecture.")
use_rerank = st.sidebar.toggle("Second pass: rerank", value=True,
    help="Off = trust the fast first pass. On = re-read each candidate against the question.")
n_first  = st.sidebar.slider("Pass 1 keeps", 3, 15, 8, help="How many candidates retrieval returns")
n_final  = st.sidebar.slider("Pass 2 keeps", 1, 5, 3, help="How many passages reach the model")
threshold = st.sidebar.slider("Refuse below this score", -12.0, 2.0, -8.5, .5,
    help="The reranker's score for the best passage. Lower = answer more, and be wrong more.")
greedy = st.sidebar.toggle("Greedy decoding", value=True,
    help="On = same answer every time, auditable. Off = sampling, varies per run.")
st.sidebar.divider()
st.sidebar.caption(f"encoder  {ENCODER.split('/')[-1]}\n\nreranker  {RERANKER.split('/')[-1]}"
                   f"\n\ngenerator  {GENERATOR.split('/')[-1]}\n\nrunning on  {DEVICE}")
st.sidebar.caption(f"{len(kb)} chunks from {len(set(d['doc_id'] for d in kb))} help articles")

# ------------------------------------------------------------------------ main
st.title("Cobalt Support Copilot")
st.caption("Paste a customer ticket. The copilot searches Cobalt's own help centre, "
           "drafts a reply, and shows you where every claim came from.")

# Streamlit keeps widget state, so a plain value= on the text area would NOT update
# when the example changes. Drive it through session_state instead, or switching
# examples mid-demo silently keeps the previous ticket.
if "ticket" not in st.session_state:
    st.session_state.ticket = ""

def _load_example():
    st.session_state.ticket = EXAMPLES.get(st.session_state.example_pick, "")

st.selectbox("Start from an example, or write your own below",
             ["(write my own)"] + list(EXAMPLES),
             key="example_pick", on_change=_load_example)
ticket = st.text_area("Customer ticket", key="ticket", height=110,
                      placeholder="Paste the customer's message here…")
go = st.button("Draft a reply", type="primary", disabled=not ticket.strip())

def retrieve(q):
    sims = X @ enc.encode([q], normalize_embeddings=True)[0]
    cand = list(np.argsort(sims)[::-1][:n_first])
    if use_rerank:
        scores = rr.predict([(q, kb[i]["text"]) for i in cand])
        ranked = sorted(zip(cand, scores), key=lambda t: -t[1])
    else:
        ranked = [(i, float(sims[i]) * 10 - 8) for i in cand]   # put on a comparable scale
    return ranked[:n_final], ranked

def generate(q, picked):
    ctx = "\n".join(f"[{n+1}] ({kb[i]['title']} / {kb[i]['section']}) {kb[i]['text']}"
                    for n, (i, _) in enumerate(picked))
    msgs = [{"role": "system", "content": SYSTEM},
            {"role": "user", "content":
             f"Passages:\n{ctx}\n\nCustomer ticket:\n{q}\n\nWrite a short reply to the customer."}]
    prompt = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    ids = tok(prompt, return_tensors="pt").to(DEVICE)
    kw = dict(max_new_tokens=200, pad_token_id=tok.eos_token_id)
    kw.update(dict(do_sample=False) if greedy else dict(do_sample=True, temperature=0.9, top_p=0.92))
    with torch.no_grad():
        out = gen.generate(**ids, **kw)
    return tok.decode(out[0][ids["input_ids"].shape[1]:], skip_special_tokens=True).strip()

if go:
    t0 = time.time()
    picked, allranked = retrieve(ticket)
    best = picked[0][1]
    with st.spinner("Retrieving, reranking, generating…"):
        raw = generate(ticket, picked)
    refused = raw.strip().upper().startswith("NO_ANSWER") or best < threshold

    left, right = st.columns([1.05, 1])
    with left:
        st.subheader("The drafted reply")
        if refused:
            st.warning("**I don't have that in our documentation.**\n\n"
                       "Nothing in the help centre scored well enough to answer from. "
                       "This ticket is going to a human.")
            st.caption(f"Best passage scored {best:+.2f}. The model was given the passages on "
                       "the right and judged that they do not answer this ticket. Look at what "
                       "was retrieved: sometimes the answer genuinely is not in the help centre, "
                       "and sometimes it is there but ranked too low to be sent.")
        else:
            st.success(raw)
            st.caption("Every [n] refers to a passage on the right. If a claim has no number, "
                       "it was not grounded, and that is the thing to look for.")
        st.caption(f"{time.time()-t0:.1f}s · retrieval {'+ rerank ' if use_rerank else ''}"
                   f"+ generation, all local")

    with right:
        st.subheader("What it retrieved")
        st.caption("These passages, and only these, were given to the model.")
        for n, (i, sc) in enumerate(picked, 1):
            d = kb[i]
            with st.container(border=True):
                c1, c2 = st.columns([4, 1])
                c1.markdown(f"**[{n}] {d['title']}**  \n*{d['section']}*")
                c2.metric("score", f"{sc:+.1f}", label_visibility="collapsed")
                st.caption(d["text"])
        with st.expander(f"the other {len(allranked)-len(picked)} candidates that were dropped"):
            for i, sc in allranked[len(picked):]:
                st.caption(f"{sc:+6.2f}   {kb[i]['title']} / {kb[i]['section']}")
else:
    st.info("Pick an example above and press **Draft a reply**. "
            "The two examples marked with an arrow are questions Cobalt's documentation "
            "does not cover, so you can watch it decline instead of inventing an answer.")
