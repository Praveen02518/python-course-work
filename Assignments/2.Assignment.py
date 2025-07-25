import re
from collections import Counter, defaultdict

# Sample WhatsApp-style chat
def get_sample_chat():
    return [
        "Praveen: Hey Babu! Are you free this weekend?",
        "Babu: Yeah bro, what's up?",
        "Praveen: Thinking about a short trip to Ooty.",
        "Babu: That sounds cool! How many days?",
        "Praveen: Maybe two or three days. What do you say?",
        "Babu: I'm in! Should we ask others too?",
        "Praveen: Sure, the more the merrier!",
        "Babu: I’ll talk to Ravi and Suresh.",
        "Praveen: Awesome. Let’s fix the dates soon.",
        "Babu: Alright! Can’t wait for it!",
        "Praveen: message deleted",
        "Babu: message deleted",
        "Praveen: Thinking about a short trip to Ooty.",
        "Babu: Yeah bro, what's up?"
    ]

# Helper to split user/message
def parse_message(msg):
    parts = msg.split(":", 1)
    return parts[0].strip(), parts[1].strip()

# Features
def count_messages(messages):
    print(f"\nTotal messages: {len(messages)}")

def unique_users(messages):
    users = {parse_message(msg)[0] for msg in messages}
    print(f"\nUnique users: {users}")

def total_words(messages):
    total = sum(len(parse_message(msg)[1].split()) for msg in messages)
    print(f"\nTotal words: {total}")

def avg_words_per_message(messages):
    total = sum(len(parse_message(msg)[1].split()) for msg in messages)
    avg = total / len(messages)
    print(f"\nAverage words per message: {round(avg, 2)}")

def longest_message(messages):
    longest = max(messages, key=lambda m: len(parse_message(m)[1]))
    print(f"\nLongest message: \"{longest}\"")

def most_active_user(messages):
    counter = Counter(parse_message(msg)[0] for msg in messages)
    user, count = counter.most_common(1)[0]
    print(f"\nMost active user: {user} ({count} messages)")

def most_frequent_word_by_user(messages):
    user = input("\nEnter user name: ")
    words = []
    for msg in messages:
        name, text = parse_message(msg)
        if name.lower() == user.lower():
            words += re.findall(r'\b\w+\b', text.lower())
    if words:
        word = Counter(words).most_common(1)[0][0]
        print(f"Most frequent word by {user}: \"{word}\"")
    else:
        print(f"No messages from {user}.")

def extract_questions(messages):
    print("\nQuestions in chat:")
    for msg in messages:
        if '?' in parse_message(msg)[1]:
            print(msg)

def sort_messages(messages):
    print("\nSorted messages (A–Z):")
    for msg in sorted(messages, key=lambda x: x.lower()):
        print(msg)

def check_user_present(messages):
    name_set = {parse_message(m)[0].lower() for m in messages}
    name = input("Enter username to check: ").lower()
    if name in name_set:
        print(f"{name.title()} is present in the chat.")
    else:
        print(f"{name.title()} is not present in the chat.")

def common_repeated_words(messages):
    words = []
    for msg in messages:
        words += re.findall(r'\b\w+\b', parse_message(msg)[1].lower())
    print("\nMost repeated words:")
    for word, count in Counter(words).most_common(5):
        if count > 1:
            print(f"{word}: {count} times")

def user_with_longest_avg_message(messages):
    user_lengths = defaultdict(list)
    for msg in messages:
        name, text = parse_message(msg)
        user_lengths[name].append(len(text))
    user_avg = {user: sum(lengths)/len(lengths) for user, lengths in user_lengths.items()}
    top_user = max(user_avg, key=user_avg.get)
    print(f"\nUser with longest average message: {top_user} ({round(user_avg[top_user], 2)} characters)")

def count_mentions(messages):
    mention = input("Enter name to check mentions: ").lower()
    count = 0
    for msg in messages:
        if mention in parse_message(msg)[1].lower():
            count += 1
    print(f"Messages mentioning '{mention}': {count}")

def remove_duplicates(messages):
    unique_msgs = list(dict.fromkeys(messages))
    print(f"\nUnique messages count: {len(unique_msgs)}")
    for msg in unique_msgs:
        print(msg)

def reply_ratio(messages):
    user1 = input("Enter first user: ").strip()
    user2 = input("Enter second user: ").strip()
    count1 = sum(1 for m in messages if parse_message(m)[0].lower() == user1.lower())
    count2 = sum(1 for m in messages if parse_message(m)[0].lower() == user2.lower())
    if count2 == 0:
        print("No messages from second user.")
        return
    ratio = round(count1 / count2, 2)
    print(f"Reply ratio ({user1}/{user2}): {ratio}")

def deleted_messages(messages):
    print("\nDeleted messages:")
    for msg in messages:
        if "message deleted" in parse_message(msg)[1].lower():
            print(msg)

# === Menu ===
def menu(messages):
    while True:
        print("\n======= WhatsApp Chat Analysis =======\n")
        print("\nChoose analysis option:")
        print("1. Count total messages")
        print("2. Unique users in chat")
        print("3. Total words")
        print("4. Average words per message")
        print("5. Longest message")
        print("6. Most active user")
        print("7. Most frequent word by user")
        print("8. Extract questions")
        print("9. Sort messages alphabetically")
        print("10. Check if user is present")
        print("11. Common repeated words")
        print("12. User with longest average message")
        print("13. Count messages mentioning a user")
        print("14. Remove duplicate messages")
        print("15. Reply ratio between two users")
        print("16. Check deleted messages")
        print("0. Exit")

        choice = re.sub(r"[^\d]", "", input("\nEnter option: "))
        if not choice.isdigit():
            print("Invalid choice. Please enter a valid number (0–16).")
            continue

        choice = int(choice)
        if choice == 0: break
        elif choice == 1: count_messages(messages)
        elif choice == 2: unique_users(messages)
        elif choice == 3: total_words(messages)
        elif choice == 4: avg_words_per_message(messages)
        elif choice == 5: longest_message(messages)
        elif choice == 6: most_active_user(messages)
        elif choice == 7: most_frequent_word_by_user(messages)
        elif choice == 8: extract_questions(messages)
        elif choice == 9: sort_messages(messages)
        elif choice == 10: check_user_present(messages)
        elif choice == 11: common_repeated_words(messages)
        elif choice == 12: user_with_longest_avg_message(messages)
        elif choice == 13: count_mentions(messages)
        elif choice == 14: remove_duplicates(messages)
        elif choice == 15: reply_ratio(messages)
        elif choice == 16: deleted_messages(messages)
        else: print("Invalid choice. Please choose between 0 and 16.")

# Run
if __name__ == "__main__":
    chat_data = get_sample_chat()
    menu(chat_data)
