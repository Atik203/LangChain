from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4",temperature=.7)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What's the weather like today?")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)