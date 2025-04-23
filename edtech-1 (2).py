# Simple simulation engine
def run_simulation(topic):
    print(f"\n[Simulation] Running virtual experiment on: {topic}...")
    print("[Simulation] Experiment completed successfully.\n")
    return f"Simulation on {topic} completed."

# Rule-based tutor chatbot
def tutor_chatbot(query):
    rules = {
        "gravity": "Gravity is a force that attracts two bodies toward each other.",
        "photosynthesis": "Photosynthesis helps plants convert light into energy.",
        "electricity": "Electricity is the flow of electric charge, often through wires.",
    }

    for keyword in rules:
        if keyword in query.lower():
            return rules[keyword]
    return "I'm not sure about that topic. Try asking about gravity, electricity, or photosynthesis."

# Quiz logic
def generate_quiz(topic):
    quizzes = {
        "gravity": {
            "question": "What is the value of acceleration due to gravity on Earth?",
            "options": ["9.8 m/s²", "10 m/s²", "5 m/s²", "12 m/s²"],
            "answer": "9.8 m/s²"
        },
        "photosynthesis": {
            "question": "Which gas is absorbed during photosynthesis?",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
            "answer": "Carbon Dioxide"
        }
    }

    quiz = quizzes.get(topic.lower())
    if not quiz:
        return "No quiz available for this topic."

    print("\n[Quiz]")
    print("Q:", quiz["question"])
    for i, opt in enumerate(quiz["options"], 1):
        print(f"{i}. {opt}")
    choice = int(input("Enter your answer (1-4): "))
    selected = quiz["options"][choice - 1]

    if selected == quiz["answer"]:
        return "Correct! 🎉"
    else:
        return f"Incorrect. The correct answer is: {quiz['answer']}"

# Main program
def main():
    print("=== Interactive Simulation & AI Tutor Platform ===")
    topic = input("Enter experiment topic (gravity/photosynthesis/electricity): ")
    result = run_simulation(topic)
    print(result)

    query = input("\nAsk the AI tutor a question: ")
    feedback = tutor_chatbot(query)
    print("[Tutor Response]:", feedback)

    report = generate_quiz(topic)
    print("[Quiz Result]:", report)

if __name__ == "__main__":
    main()
