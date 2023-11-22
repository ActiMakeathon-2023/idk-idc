from openai import OpenAI

client = OpenAI(
    api_key = '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'
)

# returns 1 or 0 by comparing with opeanAI api
def faults_cmp(first, second):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You will be provided with 2 strings which represent machine faults. You should output one number: '1' if those strings represent the same or similar faults and '0' otherwise"},
        {"role": "user", "content": f"First: '{first}' Second: '{second}'"}
        ]
    )
    response = chat_completion.choices[0].message.content
    if not response.isdigit() or (int(response) != 1 and int(response) != 0):
        raise ValueError("The API response is not valid. Expected '1' or '0'.")
    return int(response)
