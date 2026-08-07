import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

model = ChatOpenAI(model_name="gpt-5.4-mini")

result = model.invoke("what is the capital of France?")
print(result.content)
