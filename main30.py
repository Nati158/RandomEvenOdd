import random

def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

if __name__ == "__main__":
    random_number = random.randint(1, 10)
    print("Generated random number:", random_number)
    result = check_even_odd(random_number)
    print("The number is", result)
