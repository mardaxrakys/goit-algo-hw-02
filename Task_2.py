from collections import deque

def is_palindrome(s):
    # Приводимо рядок до нижнього регістру та видаляємо пробіли
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Додаємо символи рядка до двосторонньої черги
    char_deque = deque(s)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  # Якщо символи не співпадають, рядок не є паліндромом
    
    return True  # Якщо всі символи співпали, рядок є паліндромом

# Приклад використання функції
test_string = "I ate cutlet with puree and drank compote"

if is_palindrome(test_string):
    print(f'"{test_string}" є паліндромом.')
else:
    print(f'"{test_string}" не є паліндромом.')
