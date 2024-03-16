from dotenv import load_dotenv
from icecream import ic
from openai import OpenAI
# import numpy as np

load_dotenv()
client = OpenAI()
#     # This is the default and can be omitted
#     api_key=os.environ.get("OPENAI_API_KEY"),
# )

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Who was Alexander Graham Bell?",
        }
    ],
    model="gpt-3.5-turbo"
    )

ic(chat_completion)
