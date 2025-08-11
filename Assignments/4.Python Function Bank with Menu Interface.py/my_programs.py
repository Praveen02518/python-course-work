# -------------------------
# File: my_programs.py
# -------------------------

def armstrong_number():
    print("\n🧠 Program: Armstrong Number")
    print('''
def is_armstrong(n):
    s = str(n)
    power = len(s)
    total = sum(int(d)**power for d in s)
    return total == n
''')
    print("🧪 Test Case 1: is_armstrong(153) -> True")
    print("🧪 Test Case 2: is_armstrong(9474) -> True")
    print("📝 Explanation: Convert the number to string to count digits (power), then sum each digit raised to that power and compare with original number.")

def swap_numbers():
    print("\n🧠 Program: Swap Two Numbers")
    print('''
def swap(a, b):
    a, b = b, a
    return a, b
''')
    print("🧪 Test Case 1: swap(10, 20) -> (20, 10)")
    print("🧪 Test Case 2: swap(-5, 3) -> (3, -5)")
    print("📝 Explanation: Python tuple unpacking swaps values without using a temporary variable.")

def count_vowels():
    print("\n🧠 Program: Count Vowels in String")
    print('''
def count_vowels(s):
    vowels = set('aeiouAEIOU')
    return sum(1 for ch in s if ch in vowels)
''')
    print("🧪 Test Case 1: count_vowels('hello world') -> 3")
    print("🧪 Test Case 2: count_vowels('AEIOU') -> 5")
    print("📝 Explanation: Use a set of vowel characters and count characters that appear in that set.")

def gcd_two_numbers():
    print("\n🧠 Program: GCD (Greatest Common Divisor)")
    print('''
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
''')
    print("🧪 Test Case 1: gcd(48, 18) -> 6")
    print("🧪 Test Case 2: gcd(-54, 24) -> 6")
    print("📝 Explanation: Uses Euclidean algorithm to find the GCD.")

def custom_sort():
    print("\n🧠 Program: Custom Sorting")
    print('''
def custom_sort(lst):
    return sorted(lst, key=lambda x: (len(x), x))
''')
    print("🧪 Test Case 1: custom_sort(['apple','bat','ball','a']) -> ['a','bat','ball','apple']")
    print("🧪 Test Case 2: custom_sort(['aa','b','ab']) -> ['b','aa','ab']")
    print("📝 Explanation: Sort by length first, then lexicographically.")

def reverse_number():
    print("\n🧠 Program: Reverse a Number")
    print('''
def reverse_num(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n:
        rev = rev*10 + n%10
        n //= 10
    return sign*rev
''')
    print("🧪 Test Case 1: reverse_num(1200) -> 21")
    print("🧪 Test Case 2: reverse_num(-345) -> -543")
    print("📝 Explanation: Rebuild number by extracting last digit and appending.")

def sum_of_digits():
    print("\n🧠 Program: Sum of Digits")
    print('''
def sum_digits(n):
    return sum(int(d) for d in str(abs(n)))
''')
    print("🧪 Test Case 1: sum_digits(999) -> 27")
    print("🧪 Test Case 2: sum_digits(-805) -> 13")
    print("📝 Explanation: Convert to string and sum digits.")

def count_words():
    print("\n🧠 Program: Count Words in a Sentence")
    print('''
def count_words(sentence):
    words = [w for w in sentence.strip().split() if w]
    return len(words)
''')
    print("🧪 Test Case 1: count_words('Hello world') -> 2")
    print("🧪 Test Case 2: count_words('  multiple   spaces  here ') -> 3")
    print("📝 Explanation: split() handles spaces and counts words.")

def title_case():
    print("\n🧠 Program: Convert String to Title Case")
    print('''
def to_title(s):
    return ' '.join(word.capitalize() for word in s.split())
''')
    print("🧪 Test Case 1: to_title('the quick brown fox') -> 'The Quick Brown Fox'")
    print("🧪 Test Case 2: to_title('  MULTIPLE   SPACES ') -> 'Multiple Spaces'")
    print("📝 Explanation: Capitalize each word and join with spaces.")

def palindrome_check():
    print("\n🧠 Program: Palindrome Check")
    print('''
def is_palindrome(s):
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]
''')
    print("🧪 Test Case 1: is_palindrome('racecar') -> True")
    print("🧪 Test Case 2: is_palindrome('Hello') -> False")
    print("📝 Explanation: Remove non-alphanumeric chars, lowercase, compare to reverse.")

def factorial():
    print("\n🧠 Program: Factorial")
    print('''
def factorial(n):
    if n < 0:
        raise ValueError('Negative numbers not allowed')
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
''')
    print("🧪 Test Case 1: factorial(5) -> 120")
    print("🧪 Test Case 2: factorial(0) -> 1")
    print("📝 Explanation: Multiply all integers up to n.")

def fibonacci_series():
    print("\n🧠 Program: Fibonacci Series")
    print('''
def fibonacci(n):
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
''')
    print("🧪 Test Case 1: fibonacci(1) -> [0]")
    print("🧪 Test Case 2: fibonacci(6) -> [0, 1, 1, 2, 3, 5]")
    print("📝 Explanation: Append sum of last two elements until length reached.")

def prime_check():
    print("\n🧠 Program: Prime Check")
    print('''
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
''')
    print("🧪 Test Case 1: is_prime(2) -> True")
    print("🧪 Test Case 2: is_prime(15) -> False")
    print("📝 Explanation: Check divisibility up to square root of number.")

def convert_decimal_to_binary():
    print("\n🧠 Program: Convert Decimal to Binary")
    print('''
def dec_to_bin(n):
    if n == 0:
        return '0'
    sign = ''
    if n < 0:
        sign = '-'
        n = -n
    bits = []
    while n:
        bits.append(str(n % 2))
        n //= 2
    return sign + ''.join(reversed(bits))
''')
    print("🧪 Test Case 1: dec_to_bin(0) -> '0'")
    print("🧪 Test Case 2: dec_to_bin(-5) -> '-101'")
    print("📝 Explanation: Divide by 2 and collect remainders.")

def calculate_lcm():
    print("\n🧠 Program: LCM of Two Numbers")
    print('''
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)
''')
    print("🧪 Test Case 1: lcm(4, 6) -> 12")
    print("🧪 Test Case 2: lcm(0, 5) -> 0")
    print("📝 Explanation: lcm = |a*b| / gcd(a, b).")

def available_programs():
    return [
        (1, 'Armstrong Number', armstrong_number),
        (2, 'Swap Two Numbers', swap_numbers),
        (3, 'Count Vowels in String', count_vowels),
        (4, 'GCD of Two Numbers', gcd_two_numbers),
        (5, 'Custom Sorting', custom_sort),
        (6, 'Reverse a Number', reverse_number),
        (7, 'Sum of Digits', sum_of_digits),
        (8, 'Count Words in a Sentence', count_words),
        (9, 'Convert String to Title Case', title_case),
        (10, 'Palindrome Check', palindrome_check),
        (11, 'Factorial', factorial),
        (12, 'Fibonacci Series', fibonacci_series),
        (13, 'Prime Check', prime_check),
        (14, 'Convert Decimal to Binary', convert_decimal_to_binary),
        (15, 'LCM of Two Numbers', calculate_lcm),
    ]