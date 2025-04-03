import time
import random

MOCK_RESPONSES = [
    "Current AI trends include multimodal AI systems and small language models.",
    "Key developments focus on AI safety and responsible AI practices.",
    "There's growing interest in AI applications for healthcare and education.",
    "Recent advances include more efficient neural network architectures."
]

def get_response(question):
    """Get a response either from API or mock data"""
    # Simulate processing time
    time.sleep(1.2)
    
    # Return a relevant mock response
    question = question.lower()
    if "trend" in question or "ai" in question:
        return random.choice(MOCK_RESPONSES)
    elif "time" in question:
        return "I don't have real-time clock access."
    elif "neural" in question:
        return "Neural networks are computing systems inspired by biological neurons."
    else:
        return "I can answer questions about AI trends and technology."

def main():
    print("AI Chatbot (Working Demo)")
    print("Type 'exit' to quit\n")
    
    while True:
        question = input("Your question: ")
        if question.lower() == 'exit':
            break
            
        print("\nThinking...")
        answer = get_response(question)
        print(f"\n{answer}\n")

if __name__ == "__main__":
    main()
