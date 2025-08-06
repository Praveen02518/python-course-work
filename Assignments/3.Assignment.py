# Python Quiz Game — 10 Questions with Emoji and Score Feedback

questions = [
    {
        "question": "What is the output of print(type([]))?",
        "options": ["<class 'list'>", "<class 'dict'>", "<class 'set'>", "<class 'tuple'>"],
        "answer": "a"
    },
    {
        "question": "What does 10 // 3 return?",
        "options": ["3.33", "3", "4", "Error"],
        "answer": "b"
    },
    {
        "question": "What is the result of bool(\"\")?",
        "options": ["True", "False", "None", "Error"],
        "answer": "b"
    },
    {
        "question": "What does 'abc'.replace('a', 'z') return?",
        "options": ["zbc", "azc", "abc", "Error"],
        "answer": "a"
    },
    {
        "question": "What is the output of print(2 ** 4)?",
        "options": ["6", "16", "8", "4"],
        "answer": "b"
    },
    {
        "question": "Which one is a mutable data type?",
        "options": ["Tuple", "List", "String", "Integer"],
        "answer": "b"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "lambda"],
        "answer": "c"
    },
    {
        "question": "Which loop runs at least once in Python?",
        "options": ["while", "for", "do-while", "None of the above"],
        "answer": "d"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".pyth", ".pt", ".py", ".python"],
        "answer": "c"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["^", "**", "//", "*"],
        "answer": "b"
    }
]

score = 0

print("🧪 Welcome to the Python Quiz Game!")
print("-" * 40)

for idx, q in enumerate(questions, 1):
    print(f"\nQuestion {idx}: {q['question']}")
    for i, opt in zip("abcd", q["options"]):
        print(f"{i}) {opt}")
    user_ans = input("Your answer (a/b/c/d): ").lower()
    
    if user_ans == q["answer"]:
        print("✅ Correct! 😊")
        score += 1
    else:
        correct_opt = q["options"][ord(q["answer"]) - 97]
        print(f"❌ Wrong! 😢 The correct answer was '{q['answer']}) {correct_opt}'")

# Final result
print("\n🎯 Quiz Completed!")
print(f"Your Score: {score} out of {len(questions)}")

# Evaluation
if score > 7:
    print("🟢 Excellent! 👏")
elif score > 5:
    print("🟡 Average — You need a little bit of practice. 🙂")
else:
    print("🔴 Poor — You need to practice more. 😓")
