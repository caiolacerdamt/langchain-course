from langchain_openai import ChatOpenAI
import base64
from IPython.display import Image
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini", output_version="responses/v1")

tool = {"type": "image_generation", "quality": "low"}

llm_with_tools = llm.bind_tools([tool])

ai_message = llm_with_tools.invoke(
    "Draw a picture of a cute fuzzy horse with an umbrella"
)

image = next(
    item for item in ai_message.content if item["type"] == "image_generation_call"
)
Image(base64.b64decode(image["result"]), width=200)