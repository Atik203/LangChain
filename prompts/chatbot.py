from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name="gpt-4", temperature=0.7)

chat_history = [{}]

while True:
    user_input = input("You: ")
    chat_history.append({"role": "user", "content": user_input})
    if user_input.lower() == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append({"role": "ai", "content": result.content})
    print("AI: ", result.content)

print(chat_history)