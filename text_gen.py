#get the prompt and generate text/scripts 

import openai

def generate_topics(keyword):
    openai.api_key = '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'
    prompt = f"You are a user looking for topics related to {keyword}"
    response = openai.Completion.create(
        engine='gpt-3.5-turbo',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        top_p=1.0,
        n=1,
        stop='\n'
    )
    topics = response.choices[0].text.strip()
    return topics

# Get keyword from user
keyword = input("Enter a keyword: ")

# Generate topics using OpenAI API
topics = generate_topics(keyword)

# Print generated topics
print("Generated topics:")
print(topics)

