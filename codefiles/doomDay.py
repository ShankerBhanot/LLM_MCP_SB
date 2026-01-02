import openai
from openai import OpenAI
#client = OpenAI(api_key="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")  # Replace with your actual OpenAI API key

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn"}
    ],
    max_tokens=5
)
print(response.choices[0].message.content) 

"""
response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a Python function to reverse a string."}
    ]
)
print(response.choices[0].message.content)

"""