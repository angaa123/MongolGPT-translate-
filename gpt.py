import openai
openai.api_key = "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"
messages = []
def gpt_model (userPromt):
    prompt = userPromt
    userPromt = None
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    messages.append(response["choices"][0]["message"])
    return response.choices[0].message.content

