import time
import random

KNOWLEDGE_BASE = {
    # AI/ML Domain
    "ai": [
        "Current AI trends include transformer architectures and diffusion models.",
        "Researchers are focusing on making AI systems more interpretable and safe.",
        "Multimodal AI combining text, images and audio is gaining popularity."
    ],
    "machine_learning": [
        "Machine learning involves training algorithms to learn patterns from data.",
        "Popular ML frameworks include TensorFlow, PyTorch and Scikit-learn.",
        "ML models can be supervised, unsupervised, or use reinforcement learning."
    ],
    "deep_learning": [
        "Deep learning uses neural networks with multiple hidden layers.",
        "CNNs are great for image processing while RNNs work well for sequential data.",
        "Transformer architectures have revolutionized NLP tasks."
    ],

    # Emerging Technologies
    "quantum": [
        "Quantum computing uses qubits that can exist in superposition states.",
        "Quantum supremacy refers to solving problems classical computers can't.",
        "Major companies are investing heavily in quantum research."
    ],
    "blockchain": [
        "Blockchain provides decentralized, tamper-proof record keeping.",
        "Smart contracts enable automated transactions on blockchains.",
        "Web3 is the next evolution of the internet using blockchain."
    ],
    "iot": [
        "IoT connects physical devices to collect and exchange data.",
        "5G networks are enabling faster IoT implementations.",
        "Smart cities use IoT for traffic management and utilities."
    ],

    # Software & Cloud
    "cloud": [
        "Major cloud providers are AWS, Azure and Google Cloud.",
        "Serverless computing eliminates infrastructure management.",
        "Multi-cloud strategies are becoming more popular."
    ],
    "devops": [
        "CI/CD pipelines automate testing and deployment processes.",
        "Infrastructure as Code (IaC) tools include Terraform and Ansible.",
        "Observability is key for modern distributed systems."
    ],
    "programming": [
        "Python remains the fastest growing programming language.",
        "Rust is gaining popularity for system programming.",
        "TypeScript adds type safety to JavaScript development."
    ],

    # Data Domain
    "data_science": [
        "Data science combines statistics, programming and domain expertise.",
        "Pandas and NumPy are essential Python libraries for data analysis.",
        "Feature engineering is crucial for model performance."
    ],
    "big_data": [
        "Hadoop and Spark handle large-scale data processing.",
        "Data lakes store raw data in its native format.",
        "Stream processing frameworks handle real-time data."
    ],

    # Specialized Fields
    "cybersecurity": [
        "Zero-trust architecture is becoming the security standard.",
        "AI is being used to detect novel attack patterns.",
        "Cloud security is a growing concern with adoption."
    ],
    "computer_vision": [
        "Computer vision enables machines to interpret visual data.",
        "Applications include facial recognition and medical imaging.",
        "YOLO and ResNet are popular CV architectures."
    ],
    "nlp": [
        "NLP enables machines to understand human language.",
        "BERT and GPT models have advanced NLP capabilities.",
        "Applications include translation and sentiment analysis."
    ]
}

def get_response(question):
    """Generate intelligent responses based on question context"""
    time.sleep(1.3)  # Simulate processing time
    
    question = question.lower()
    
    # AI/ML Domain
    if any(w in question for w in ["ai", "artificial intelligence"]):
        return random.choice(KNOWLEDGE_BASE["ai"])
    elif any(w in question for w in ["machine learning", "ml"]):
        return random.choice(KNOWLEDGE_BASE["machine_learning"])
    elif any(w in question for w in ["deep learning", "neural network"]):
        return random.choice(KNOWLEDGE_BASE["deep_learning"])
        
    # Emerging Tech
    elif "quantum" in question:
        return random.choice(KNOWLEDGE_BASE["quantum"])
    elif any(w in question for w in ["blockchain", "crypto", "web3"]):
        return random.choice(KNOWLEDGE_BASE["blockchain"])
    elif any(w in question for w in ["iot", "internet of things"]):
        return random.choice(KNOWLEDGE_BASE["iot"])
        
    # Software & Cloud
    elif "cloud" in question:
        return random.choice(KNOWLEDGE_BASE["cloud"])
    elif any(w in question for w in ["devops", "ci/cd"]):
        return random.choice(KNOWLEDGE_BASE["devops"])
    elif any(w in question for w in ["programming", "code", "developer"]):
        return random.choice(KNOWLEDGE_BASE["programming"])
        
    # Data Domain
    elif any(w in question for w in ["data science", "data analysis"]):
        return random.choice(KNOWLEDGE_BASE["data_science"])
    elif "big data" in question:
        return random.choice(KNOWLEDGE_BASE["big_data"])
        
    # Specialized Fields
    elif any(w in question for w in ["cyber", "security"]):
        return random.choice(KNOWLEDGE_BASE["cybersecurity"])
    elif any(w in question for w in ["computer vision", "cv", "image processing"]):
        return random.choice(KNOWLEDGE_BASE["computer_vision"])
    elif any(w in question for w in ["nlp", "natural language", "language processing"]):
        return random.choice(KNOWLEDGE_BASE["nlp"])
        
    # Default response
    else:
        topics = "\n".join([f"- {t.replace('_', ' ').title()}" 
                          for t in KNOWLEDGE_BASE.keys()])
        return f"I can discuss these technology topics:\n{topics}\n\nTry asking about specific areas!"

def main():
    print("Enhanced Technology Knowledge Chatbot")
    print("Type 'exit' to quit\n")
    print("I can discuss these technology domains:")
    print("- Artificial Intelligence & Machine Learning")
    print("- Quantum Computing & Blockchain")
    print("- Cloud Computing & DevOps")
    print("- Data Science & Big Data")
    print("- Cyber Security & Computer Vision")
    print("- Natural Language Processing\n")
    
    while True:
        question = input("\nYour question: ")
        if question.lower() in ['exit', 'quit']:
            break
            
        print("\nProcessing...")
        print(f"\n{get_response(question)}\n")

if __name__ == "__main__":
    main()
