#import os
#import openai
# 加载 .env 到环境变量
#from dotenv import load_dotenv, find_dotenv
#_ = load_dotenv(find_dotenv())

# 配置 OpenAI 服务
#openai.api_key = os.getenv('OPENAI_API_KEY') # 设置 OpenAI 的 key
#openai.api_base = os.getenv('OPENAI_API_BASE') # 指定代理地址

#response = openai.ChatCompletion.create(
#    model="gpt-3.5-turbo",
#    messages=[
#        {
#            "role": "user",
#            "content": "讲个笑话"
#        }
#    ],
#)

print(response['choices'][0]['message'].get("content"))

import os
from openai import OpenAI

# 加载 .env 到环境变量
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# 配置 OpenAI 服务

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

print(response)