import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

st.header("Research Tool")
user_input = st.text_input("Enter your research query here:", key="query")

if st.button("Submit"):
    if user_input:
        llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7)
        response = llm.invoke(user_input)
        st.write(response.content)
    else:
        st.warning("Please enter a research query before submitting.")
