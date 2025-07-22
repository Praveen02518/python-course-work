#
data = {
    1: {'name': 'Rice', 'price': 60},
    2: {'name': 'Wheat Flour', 'price': 45},
    3: {'name': 'Sugar', 'price': 160},
    4: {'name': 'Milk', 'price': 30},
    5: {'name': 'Eggs', 'price': 40},
    6: {'name': 'Cooking Oil', 'price': 200},
    7: {'name': 'Tea Powder', 'price': 150},
    8: {'name': 'Salt', 'price': 90},
    9: {'name': 'Bread', 'price': 20},
    10: {'name': 'Soap', 'price': 25},
}

print("Available Products:\n")
for i in data:
    print(f'{i}. {data[i]["name"]} - ₹{data[i]["price"]}')

items = list(map(int, input("\nEnter the product indexes (e.g., 1 2 3 1): ").split()))

total = 0
s = set()
print("\nYour Bill:")
for i in items:
    if i not in s:
        count = items.count(i)
        name = data[i]['name']
        price = data[i]['price']
        print(f'{name} - {count} * ₹{price} = ₹{count * price}')
        total += price * count
        s.add(i)

print(f"\nTotal Bill: ₹{total}")
total=0

data={'milk':30,'bread':50,'sugar':40,'oil':20}
print(data)
while True:
    product_name=input("Enter the product name(0-Exit): ")
    if product_name=='0':
        print("Thank You Myaan")
        break
    quantity=int(input("Enter the quantity: "))
    total+=data[product_name]*quantity
print("Total Amount:",total)
#
# leadership board
import random

# Initialize the leaderboard with random scores
leaderboard = [random.randint(100, 500) for _ in range(5)]

# Game loop
while True:
    print("\n--- Game Leaderboard Management ---")
    print("1. Add a New Score")
    print("2. Remove a Score")
    print("3. Sort Leaderboard (High to Low)")
    print("4. Sort Leaderboard (Low to High)")
    print("5. Reverse Leaderboard")
    print("6. Find Player Rank")
    print("7. Show Highest & Lowest Score")
    print("8. Count a Score")
    print("9. Clear Leaderboard")
    print("10. Exit")

    choice = input("Enter your choice (1-10): ")

    # 1. Add a score
    if choice == "1":
        score = int(input("Enter new score: "))
        leaderboard.append(score)
        print("Score added.")

    # 2. Remove a score
    elif choice == "2":
        score = int(input("Enter score to remove: "))
        if score in leaderboard:
            leaderboard.remove(score)
            print("Score removed.")
        else:
            print("Score not found.")

    # 3. Sort High to Low
    elif choice == "3":
        leaderboard.sort(reverse=True)
        print("Leaderboard sorted (high to low).")

    # 4. Sort Low to High
    elif choice == "4":
        leaderboard.sort()
        print("Leaderboard sorted (low to high).")

    # 5. Reverse order
    elif choice == "5":
        leaderboard.reverse()
        print("Leaderboard order reversed.")

    # 6. Find rank
    elif choice == "6":
        score = int(input("Enter score to find rank: "))
        sorted_board = sorted(leaderboard, reverse=True)
        if score in sorted_board:
            rank = sorted_board.index(score) + 1
            print(f"Score {score} is ranked #{rank}.")
        else:
            print("Score not found.")

    # 7. Show highest and lowest
    elif choice == "7":
        if leaderboard:
            print("Highest score:", max(leaderboard))
            print("Lowest score:", min(leaderboard))
        else:
            print("Leaderboard is empty.")

    # 8. Count a score
    elif choice == "8":
        score = int(input("Enter score to count: "))
        count = leaderboard.count(score)
        print(f"Score {score} appears {count} times.")

    # 9. Clear leaderboard
    elif choice == "9":
        leaderboard.clear()
        print("Leaderboard cleared.")

    # 10. Exit
    elif choice == "10":
        print("Exiting program.")
        break

    else:
        print("Invalid choice, try again.")

    # Show leaderboard
    if leaderboard:
        print("\nCurrent Leaderboard (High to Low):")
        for i, score in enumerate(sorted(leaderboard, reverse=True), start=1):
            print(f"{i}. Score: {score}")
    else:
        print("\nLeaderboard is empty.")
    print("-" * 30)
