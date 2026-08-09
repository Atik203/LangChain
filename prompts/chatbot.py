from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name="gpt-4", temperature=0.7)


while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = model.invoke(user_input)
    print("AI: ", response.content)