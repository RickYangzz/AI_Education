from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os

load_dotenv()

# 填写您自己的APIKey
client = ZhipuAI(api_key=f"{os.getenv('API_KEY')}") 

response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=[
        {"role": "system", "content": "你是一个聪明且富有创造力的小说作家"},
        {"role": "user", "content": "请你作为童话故事大王，写一篇短篇童话故事，故事的主题是要永远保持一颗善良的心，要能够激发儿童的学习兴趣和想象力，同时也能够帮助儿童更好地理解和接受故事中所蕴含的道理和价值观。"}
    ],
)

print(response.choices[0].message)
