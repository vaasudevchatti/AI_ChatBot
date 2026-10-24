from config import client

while True:

    question = input("you: ")
    if question.lower() == "exit": break

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        max_tokens=1024,
        messages=[{"role": "user", "content": question}]
    )
    print()
    print("bot:", response.choices[0].message.content)
    print()