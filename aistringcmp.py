from openai import OpenAI

client = OpenAI(
    api_key=""
)

first_message = "OPERATOR: NORMAL STOP ACTUATED"
second_message = "sdafED"
chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You will be provided with 2 strings which represent machine faults. You should output one number: '1' if those strings represent the same or similar faults and '0' otherwise"},
    {"role": "user", "content": f"First: '{first_message}' Second: '{second_message}'"}
    ]
)

print(chat_completion.choices[0].message.content)
