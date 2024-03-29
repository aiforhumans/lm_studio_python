from openai import OpenAI
import os

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

response = client.chat.completions.create(
    model= "local", #not used
    messages=[
        {"role": "system", "content": "You are a local HTTP server that behaves like OpenAI's API. only awnser mark"},
        {"role": "user", "name": "mark", "content": "Type Hello World in a creative way."},
        {"role": "user", "name": "steve", "content": "count to 10 in a creative way."},
    ],
    temperature=0,
)

print(response.choices[0].message.content)