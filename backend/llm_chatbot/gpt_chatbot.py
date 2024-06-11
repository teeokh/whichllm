from openai import OpenAI
client = OpenAI()

# Returns the usecase category based on user text input
def categorise_text(text):
    try:
        response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal:whichllm-1:9YiBR3Fe:ckpt-step-158",
        messages=[
            {
            "role": "system",
            "content": [
                {
                "text": "You are working for an LLM recommendation application. Your only purpose is to categorize the user's desired use case into one of several categories. The listed categories: General Knowledge, Basic Reasoning, Science, Advanced Reasoning, Mathematics, Programming, Medical Knowledge, Legal Knowledge, Document Analysis, Image Analysis, Audio Processing, Video Analysis, Text Generation, Creativity, Relative User Preference. If there is no clear use case, please return 'No clear use case identified'.",
                "type": "text"
                }
            ]
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        category = response.choices[0].message.content

        if category == "No clear use case identified":
            return 'No clear use case identified'
        else:
            return category
        
    except Exception as e:
        print(f"Error categorizing text: {e}")
        raise RuntimeError("Failed to categorize text")