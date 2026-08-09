import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model_name="gpt-4", temperature=0.7)

st.header("Research Tool")

paper_input = st.selectbox(
    "Select a Research paper name",
    [
        "Select .....",
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "GPT-3: Language Models are Few-Shot Learners",
        "RoBERTa: A Robustly Optimized BERT Pretraining Approach",
        "XLNet: Generalized Autoregressive Pretraining for Language Understanding",
    ],
)

style_input = st.selectbox(
    "Select a Explanation Style",
    [
        "Select .....",
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical",
    ],
)

length_input = st.selectbox(
    "Select a Explanation Length",
    [
        "Select .....",
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (6+ paragraphs)",
    ],
)

if st.button("Generate Explanation"):
    if "Select ....." in [paper_input, style_input, length_input]:
        st.warning("Please make a selection for all fields before generating.")
    else:
        template = load_prompt("template.json")
        prompt = template.invoke(
            {
                "paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input,
            }
        )
        with st.spinner("Generating explanation..."):
            result = model.invoke(prompt)
            st.write(result.content)

