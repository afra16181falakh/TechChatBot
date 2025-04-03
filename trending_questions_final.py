import requests
import json

# Function to call the OpenAI language model API
def call_language_model(question):
    api_url = "https://api.openai.com/v1/chat/completions"  # OpenAI API endpoint
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # Specify the model
        "messages": [{"role": "user", "content": question}],
        "max_tokens": 150  # Adjust as needed
    }
    
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response from model.")
    else:
        return "Error: Unable to fetch response from the model."

def main():
    print("Welcome to the Trending Questions Answering System!")
    # Predefined question for testing
    test_question = "What are the current trends in AI?"
    print(f"Testing with question: {test_question}")
    answer = call_language_model(test_question)
    print(answer)

if __name__ == "__main__":
    main()
