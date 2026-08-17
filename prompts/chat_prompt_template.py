from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage

chat_template = ChatPromptTemplate([
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="{question}")
])

prompt = chat_template.format(question="What is the capital of France?")
print(prompt)