import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

model = ChatOpenAI(model_name="gpt-5.4-mini", temperature=1.5)

result = model.invoke(
    "suggest me 5 creative ideas for a sci-fi short story within 5 lines"
)
print(result.content)
