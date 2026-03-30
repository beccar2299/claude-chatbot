import anthropic

client = anthropic.Anthropic()

def chat(messages):
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=messages
    )
    return response.content[0].text

def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

messages = []

while True:
    user_input = input("> ")
    add_user_message(messages, user_input)
    answer = chat(messages)
    add_assistant_message(messages, answer)
    print("---")
    print(answer)
    print("---")
