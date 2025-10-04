#使用Flask库实现Web服务器功能
#sk-5ea6d576847044398ca2dadd3b2d9a09

from openai import OpenAI

API_KEY = "sk-5ea6d576847044398ca2dadd3b2d9a09"
client = OpenAI(api_key = API_KEY,
                base_url ="https://api.deepseek.com/v1")

prompt = "大学新生如何学习python语言程序设计?"
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[
        {"role": "user",
         "content": prompt} #用户信息
    ],
    stream=True
)

for chunk in response:
    if not chunk.choices:
        continue
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True) #输出结果
    if chunk.choices[0].delta.reasoning_content:
        print(chunk.choices[0].delta.reasoning_content, end="", flush=True) #输出推理过程