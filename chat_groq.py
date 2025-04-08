from openai import OpenAI

client = OpenAI(
    api_key="",
    base_url="https://api.groq.com/openai/v1"
)

messages = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit"}:  # Exit condition
        print("Exiting chat. Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    assistant_response = chat_completion.choices[0].message.content
    print(f"Assistant: {assistant_response}")

    messages.append({"role": "assistant", "content": assistant_response})