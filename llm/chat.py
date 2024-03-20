from openai import OpenAI
client = OpenAI()

system_message = "You are a helpful assistant. When asked, you never give away the answer, instead you ask helpful questions so that the user finds the answer by himself."


messages = [
    {"role": "system", "content": f"{system_message}"},  
]

# Which model to use
model = "gpt-4-turbo-preview"

user_message = ""

while user_message != "bye":
     
    user_message = input("User: ")
    messages.append({"role": "user", "content": f"{user_message}"})

    chat_response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    response_message = chat_response.choices[0].message
    messages.append(response_message)
    response_text = chat_response.choices[0].message.content

    print(f"\nAI: {response_text}\n")
