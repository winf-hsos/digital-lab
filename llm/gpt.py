from openai import OpenAI
client = OpenAI()

system_message = "You are a helpful assistant. You try to keep your answers as short as possible!"
user_message = input("User: ")

messages = [
    {"role": "system", "content": f"{system_message}"},
    {"role": "user", "content": f"{user_message}"}
]

# Which model to use
model = "gpt-4-turbo-preview"

chat_response = client.chat.completions.create(
    model=model,
    messages=messages
)

response = chat_response.choices[0].message.content
print(f"AI: {response}")
