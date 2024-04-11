from ollama import Client

user_input = input("Mitä haluat kysyä? " )

client = Client(host="http://localhost:11434")

response = client.chat(model="llama2", stream=True, messages=[
    {
        "role": "user",
        "content": user_input
    },
    
])

for chunk in response:
    print(chunk['message']['content'], end='', flush=True)
