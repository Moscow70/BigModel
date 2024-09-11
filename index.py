from openai import OpenAI
from pathlib import Path
import json
import os

# api_key = str(os.getenv('OPENAI_API_KEY'))
# print(api_key)

def get_completion(messages, model, tools_arr) :
    response = client.chat.completions.create(
        model = model,
        messages = messages,
        temperature = 0,
        max_tokens = 1024,
        tools = tools_arr
    )
    return response.choices[0].message

tools_arr = [
    {
        "type": "function",
        "function": {
            "name": "sum",
            "description": "sum函数可以用来计算一组数据的和",
            "parameters": {
                "type": "object",
                "properties": {
                    "numbers": {
                        "type": "array",
                        "items":{
                            "type":"number"
                        }
                    }
                }
            }
        }
    }
]



client = OpenAI(
    api_key = "sk-vkD6BPzRuC5IuRR6FJ54OoX9NCOeLXF29ZfJklsn7pjzWtx3",
    base_url = "https://api.agicto.cn/v1"
)



prompt = "桌上有2个苹果，四个桃子和 3 本书，一共有几个水果？"

messages = [
    {"role": "system", "content": "你是一个数学家，你可以计算任何算式。"},
    {"role": "user", "content": prompt}
]

response = get_completion(messages, "gpt-3.5-turbo", tools_arr)

print(response)




# chat_completion = client.chat.completions.create(
#     messages=[
#         # {
#         #     "role": "user",
#         #     "content": """按照如下输出格式，输出一个.json文件，不需要输出任何附加文字，至少5组数据
#         #         data = { 
#         #             "name": "张三", 
#         #             "age": 30, 
#         #             "city": "北京" 
#         #         } """,
#         # }
#         {"role": "system", "content": "You are a helpful assistant."},
#     ],
#     model="gpt-3.5-turbo", #此处更换其它模型,请参考模型列表 eg: google/gemma-7b-it
# )

# file_path = Path('D:/testdata/output/output.txt')

# data = chat_completion.choices[0].message.content

# with open(file_path, 'w', encoding='utf-8') as file:
#     # json.dump(data, file, ensure_ascii=False, indent = 4)
#     file.write(data)

# print(chat_completion.choices[0].message.content)
