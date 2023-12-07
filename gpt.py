import openai
openai.api_key = "openAI_API_KEY"
messages = []
def gpt_model (userPromt):
    prompt = userPromt
    userPromt = None
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    messages.append(response["choices"][0]["message"])
    return response.choices[0].message.content

