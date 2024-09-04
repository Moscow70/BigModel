from openai import OpenAI
from pathlib import Path
import json

client = OpenAI(
    api_key = "sk-vkD6BPzRuC5IuRR6FJ54OoX9NCOeLXF29ZfJklsn7pjzWtx3",
    base_url = "https://api.agicto.cn/v1"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": """按照如下输出格式，输出一个.json文件，不需要输出任何附加文字，至少5组数据
                data = { 
                    "name": "张三", 
                    "age": 30, 
                    "city": "北京" 
                } """,
        }
    ],
    model="ERNIE-Lite-8K", #此处更换其它模型,请参考模型列表 eg: google/gemma-7b-it
)

file_path = Path('D:/testdata/output/output.json')

data = chat_completion.choices[0].message.content

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent = 4)

#print(chat_completion.choices[0].message.content)
