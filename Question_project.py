import pandas as pd
from datetime import datetime

# -----------------------------
# 1. Quiz Questions
# -----------------------------
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is primarily used for data science?",
        "options": ["A) Python", "B) Java", "C) C++", "D) Ruby"],
        "answer": "A"
    },
    {
        "question": "What does SQL stand for?",
        "options": ["A) Structured Query Language", "B) Simple Query Logic", "C) Sequential Query List", "D) None"],
        "answer": "A"
    }
]

# -----------------------------
# 2. Run Quiz
# -----------------------------
def run_quiz():
    score = 0
    responses = []

    print("\n📘 Welcome to the Quiz!\n")
    for i, q in enumerate(questions, start=1):
        print(f"Q{i}: {q['question']}")
        for opt in q["options"]:
            print(opt)
        user_ans = input("Your answer (A/B/C/D): ").strip().upper()
        correct = user_ans == q["answer"]
        responses.append({"question": q["question"], "your_answer": user_ans, "correct_answer": q["answer"], "result": "Correct" if correct else "Wrong"})
        if correct:
            score += 1
        print("✅ Correct!\n" if correct else f"❌ Wrong! Correct answer: {q['answer']}\n")

    print(f"🎉 Final Score: {score}/{len(questions)}")

    # Save attempt history
    save_history(score, responses)

# -----------------------------
# 3. Save Results
# -----------------------------
def save_history(score, responses):
    try:
        df = pd.read_csv("quiz_history.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["date", "score", "details"])

    attempt = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "score": f"{score}/{len(questions)}",
        "details": str(responses)
    }

    df = pd.concat([df, pd.DataFrame([attempt])], ignore_index=True)
    df.to_csv("quiz_history.csv", index=False)
    print("\n Attempt saved to history!")

# -----------------------------
# 4. View History
# -----------------------------
def view_history():
    try:
        df = pd.read_csv("quiz_history.csv")
        print("\n Quiz Attempt History:")
        print(df)
    except FileNotFoundError:
        print("\nNo history found yet.")

# -----------------------------
# Run the program
# -----------------------------
if __name__ == "__main__":
    run_quiz()
    view_history()

#thats all lol, yep 😎
