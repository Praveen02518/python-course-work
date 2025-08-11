# -------------------------
# File: main.py
# -------------------------
"""
This is the menu-driven entry point. It imports my_programs, shows a menu
with the 15 programs and allows the user to choose a number (1-15) to view
that program's code, test cases and explanation. Enter 0 to exit.
"""

if __name__ == '__main__':
    import my_programs

    programs = my_programs.available_programs()

    while True:
        print('\n------ FUNCTION MENU ------')
        for num, title, _ in programs:
            print(f"{num}. {title}")
        print('0. Exit')
        print('----------------------------')

        choice = input('Enter your choice (0-15): ').strip()
        if not choice:
            print('Please enter a number.')
            continue
        if not choice.isdigit():
            print('Invalid input. Enter digits only.')
            continue

        choice = int(choice)
        if choice == 0:
            print('Exiting program. Goodbye!')
            break

        matches = [t for (n, t, fn) in programs if n == choice]
        if not matches:
            print('Invalid choice. Choose a number between 0 and 15.')
            continue

        # find function and call it
        for (n, title, fn) in programs:
            if n == choice:
                fn()  # function will print code, test cases, explanation
                break

        input('\nPress Enter to return to the menu...')
