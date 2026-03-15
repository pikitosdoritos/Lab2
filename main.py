#1 
# Створіть програму, яка запитує користувача два цілих числа a і b, після чого виводить на екран результати наступних математичних операцій (результат округлити до 2-х знаків після коми):
# суму;
# різницю між a і b;
# добуток;
# ділення a на b;
# залишок від ділення a на b;
# десятковий логарифм числа a;
# результат піднесення числа a в ступінь b; квадратний корінь з числа a;
# поміняти значення цих чисел місцями (значення числа b запам’ятати в
# змінній з ім’ям a та навпаки).
import math

print("==" * 80)
print("Task 1")

while True:
    

    try:
        a = int(input("Введіть перше число: "))
        b = int(input("Введіть друге число: "))
        
        print(f"Сума: {round(a + b, 2)}")
        print(f"Різниця: {round(a - b, 2)}")
        print(f"Добуток: {round(a * b, 2)}")
        print(f"Ділення: {round(a / b, 2)}")
        print(f"Залишок від ділення: {round(a % b, 2)}")
        
        if a <= 0:
            print("Логарифм і корінь визначені тільки для додатних чисел.")
        else:
            print(f"Десятковий логарифм числа a: {round(math.log10(a), 2)}")
            print(f"Квадратний корінь з числа a: {round(math.sqrt(a), 2)}")
            
        print(f"Результат піднесення числа a в ступінь b: {round(a ** b, 2)}")

        a, b = b, a

        print(f"Поміняні значення: a = {a}, b = {b}")
        
        break
    
    except (ValueError, ZeroDivisionError):
        print("Будь ласка, введіть коректні числа.")

# 2
# Дано тризначне число
# піднести це число до 3-го ступеня. Вважаючи, що результат – це розмір
# файлу кілобайтах, використовуючи операцію ділення націло,
# визначити, скільки це буде повних мегабайт, гігабайт
# у ньому закреслили першу зліва цифру і приписали її справа. Вивести
# отримане число;
# знайти суму і добуток його цифр;
# вивести число, отримане при перестановці цифр сотень і десятків
# вихідного числа (наприклад, 123 перейде в 213).

print("==" * 80)
print("Task 2")


while True:
    try:
        number = int(input("Введіть тризначне число: "))
        
        if not (100 <= number < 1000):
            print("Будь ласка, введіть тризначне число.")
            continue
        
        size_kb = number ** 3
        size_mb = size_kb // 1024
        size_gb = size_kb // (1024 * 1024)

        print("Size in KB:", size_kb)
        print("Full MB:", size_mb)
        print("Full GB:", size_gb)

        first = number // 100
        rest = number % 100

        new_number = rest * 10 + first

        print("New number:", new_number)

        print(f"Sum of digits: {sum(map(int, str(number)))}")
        
        hundreds = number // 100
        tens = (number // 10) % 10
        ones = number % 10
        
        product_digits = hundreds * tens * ones

        print(f"Product of digits: {product_digits}")

        swapped = tens * 100 + hundreds * 10 + ones

        print(f"Swapped hundreds and tens: {swapped}")
        
        break
    
    except ValueError:
        print("Будь ласка, введіть коректне число.")