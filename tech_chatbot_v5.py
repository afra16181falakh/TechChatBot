import time
import random

# Comprehensive knowledge base with more technical depth
TECH_KNOWLEDGE = {
    # AI/ML with expanded coverage
    "ai": [
        "Current AI trends: Transformers, diffusion models, and multimodal systems",
        "Key focus areas: AI safety, interpretability, and ethical development",
        "Emerging applications in healthcare, education, and creative fields"
    ],
    "machine_learning": [
        "Core concepts: Supervised, unsupervised, and reinforcement learning",
        "Popular frameworks: TensorFlow, PyTorch, Scikit-learn",
        "ML lifecycle: Data preparation, model training, evaluation, deployment"
    ],
    "deep_learning": [
        "Neural network architectures: CNNs, RNNs, Transformers",
        "Training techniques: Backpropagation, gradient descent, regularization",
        "Applications: Computer vision, NLP, speech recognition"
    ],
    "reinforcement_learning": [
        "Reinforcement learning involves training agents to make decisions through trial and error.",
        "Key concepts include rewards, policies, and value functions.",
        "Applications range from game playing to robotics."
    ],
    "diffusion_models": [
        "Diffusion models generate data by reversing a gradual noise process.",
        "Key applications: Image generation, text-to-image synthesis.",
        "Popular implementations: DALL-E, Stable Diffusion, Imagen."
    ],
    
    # Emerging Tech
    "quantum": [
        "Quantum computing uses qubits in superposition states.",
        "Potential applications: Drug discovery, cryptography, optimization.",
        "Major players: IBM, Google, startups in quantum space."
    ],
    
    # Cloud/DevOps
    "cloud": [
        "Major platforms: AWS (33% market share), Azure, Google Cloud.",
        "Key services: Compute, storage, databases, serverless.",
        "Trends: Hybrid cloud, cost optimization, sustainability."
    ],
    
    # Data
    "data_science": [
        "Workflow: Data cleaning, exploration, modeling, visualization.",
        "Essential skills: SQL, Python, statistics, domain knowledge.",
        "Common tools: Pandas, NumPy, Matplotlib, Jupyter."
    ],
    
    # Specialized
    "cybersecurity": [
        "Zero trust architecture: Never trust, always verify.",
        "Emerging threats: AI-powered attacks, supply chain risks.",
        "Defense strategies: MFA, encryption, regular patching."
    ]
}

def get_tech_response(question):
    """Generate precise, multi-topic responses with context awareness"""
    time.sleep(1.2)  # Realistic processing delay
    
    question = question.lower()
    
    # Specific technical term matching
    if "reinforcement" in question and "learning" in question:
        return random.choice(TECH_KNOWLEDGE["reinforcement_learning"])
    if "diffusion" in question and "model" in question:
        return random.choice(TECH_KNOWLEDGE["diffusion_models"])
    
    # General topic matching
    for topic, answers in TECH_KNOWLEDGE.items():
        if any(keyword in question 
              for keyword in topic.split('_')):
            return random.choice(answers)
    
    # Default response listing available topics
    available_topics = "\n".join(
        f"- {topic.replace('_', ' ').title()}" 
        for topic in TECH_KNOWLEDGE.keys()
    )
    return (f"I specialize in these technology areas:\n{available_topics}\n\n"
           "Try asking about specific topics like 'reinforcement learning' or 'cloud computing'")

def main():
    print("\n=== Tech Knowledge Chatbot v5 ===")
    print("Ask about any technology topic or type 'exit'\n")
    
    while True:
        question = input("Your question: ").strip()
        if question.lower() in ['exit', 'quit']:
            break
            
        print("\nProcessing...")
        response = get_tech_response(question)
        print(f"\n{response}\n")

if __name__ == "__main__":
    main()
