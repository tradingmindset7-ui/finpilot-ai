import os
import streamlit as st
from google import genai

st.set_page_config(
    page_title="FinPilot AI | Finance Learning Assistant",
    page_icon="📊",
    layout="centered",
)

SYSTEM_PROMPT = """You are FinPilot AI, an educational finance assistant for Indian learners.
Explain finance and investing concepts in clear, simple English. Use headings, examples,
and transparent calculations when useful. Distinguish facts from estimates and state
assumptions. Do not invent live prices, financial data, citations, or company filings.
If the question requires current data that is not supplied, say that you cannot verify it.
Do not promise returns or give personalised buy/sell instructions. Explain risks and the
limitations of financial ratios. This is education, not personalised investment advice."""

st.markdown("""
<style>
.block-container {max-width: 850px; padding-top: 2rem; padding-bottom: 3rem;}
.hero {padding: 1.4rem; border: 1px solid rgba(128,128,128,.25); border-radius: 18px;}
.small-note {font-size: .88rem; opacity: .82;}
</style>
""", unsafe_allow_html=True)

st.title("📊 FinPilot AI")
st.caption("Understand finance. Learn to analyse. Ask better questions.")

with st.container(border=True):
    st.subheader("Your finance learning assistant")
    st.write("Explore financial statements, investing concepts, valuation metrics, and personal-finance fundamentals in plain English.")
    st.markdown("**Try asking about:**")
    examples = [
        "Explain ROE vs ROCE with a simple example.",
        "How do I read a cash flow statement?",
        "What is the difference between P/E and EV/EBITDA?",
        "What are the warning signs of high company debt?",
    ]
    cols = st.columns(2)
    for i, example in enumerate(examples):
        if cols[i % 2].button(example, use_container_width=True, key=f"example_{i}"):
            st.session_state["question"] = example

st.info("Educational use only. AI responses can be wrong. This demo does not provide personalised investment advice or verified live market data.")

api_key = ""
try:
    api_key = st.secrets.get("GEMINI_API_KEY", "")
except Exception:
    api_key = ""
api_key = api_key or os.environ.get("GEMINI_API_KEY", "")

if not api_key:
    st.warning("The demo is ready, but its AI key has not been configured yet. Add GEMINI_API_KEY in the app host's private Secrets settings to enable answers.")
else:
    question = st.text_area(
        "Ask a finance question",
        key="question",
        placeholder="Example: Explain operating cash flow versus net profit.",
        height=130,
    )
    if st.button("Explain with AI", type="primary", use_container_width=True):
        if not question.strip():
            st.warning("Enter a question first.")
        else:
            try:
                client = genai.Client(api_key=api_key)
                with st.spinner("Preparing an explanation…"):
                    response = client.models.generate_content(
                        model=os.environ.get("GEMINI_MODEL", "gemini-2.5-flash"),
                        contents=f"{SYSTEM_PROMPT}\n\nUser question:\n{question.strip()}",
                    )
                answer = getattr(response, "text", None)
                if answer:
                    st.markdown("### Explanation")
                    st.markdown(answer)
                else:
                    st.error("The model returned an empty response. Try again.")
            except Exception as exc:
                # Avoid displaying credentials or full request data to users.
                st.error("The AI request failed. Check the private API key, model availability, free-tier quota, and service status.")
                with st.expander("Technical error details"):
                    st.code(f"{type(exc).__name__}: {str(exc)[:500]}")

st.divider()
left, right = st.columns(2)
with left:
    st.markdown("**Built for learning**")
    st.caption("Financial concepts, ratios, and statement literacy.")
with right:
    st.markdown("**Not a trading signal service**")
    st.caption("No guaranteed returns or personalised buy/sell calls.")
st.caption("FinPilot AI · Early prototype · Replace this working name after checking brand availability.")
