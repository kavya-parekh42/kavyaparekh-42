import math
import random

# 1. Demonstrating math module (basic mathematical operations)
def math_operations():
    print("=== Math Operations ===")
    x = 16
    y = 4

    # Square root of x
    print(f"Square root of {x}: {math.sqrt(x)}")

    # Logarithm of x (natural logarithm)
    print(f"Natural log of {x}: {math.log(x)}")

    # Exponentiation (x raised to the power y)
    print(f"{x} raised to the power {y}: {math.pow(x, y)}")

    # Factorial of y
    print(f"Factorial of {y}: {math.factorial(y)}")

    # Hypotenuse of a right triangle with sides x and y
    print(f"Hypotenuse of a right triangle with sides {x} and {y}: {math.hypot(x, y)}")


# 2. Demonstrating random module (random number generation)
def random_operations():
    print("\n=== Random Operations ===")
    
    # Generate a random integer between 1 and 100
    rand_int = random.randint(1, 100)
    print(f"Random integer between 1 and 100: {rand_int}")

    # Generate a random float between 0 and 1
    rand_float = random.random()
    print(f"Random float between 0 and 1: {rand_float}")

    # Pick a random item from a list
    items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    rand_item = random.choice(items)
    print(f"Random choice from list: {rand_item}")

    # Shuffle the list
    random.shuffle(items)
    print(f"Shuffled list: {items}")


# Main function to demonstrate all operations
def main():
    math_operations()
    random_operations()


if __name__ == "__main__":
    main()
