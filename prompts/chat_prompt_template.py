from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate(
    [
        SystemMessage(content="You are a helpful assistant of {domain}"),
        HumanMessage(content="Explain in simple term , what is {topic}"),
    ]
)

prompt = chat_template.invoke({"domain": "cricket", "topic": "Dusra"})
print(prompt)
