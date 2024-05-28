import openai

#openai.api_key =

query = "what is the most popular programming language"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=query,
    temperature=0,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty = 0.0
)

print(response)
