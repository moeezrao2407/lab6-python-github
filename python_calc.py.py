def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def check_even_odd(n):
    if not n.is_integer():
        return "not a whole number, so it is neither even nor odd"

    if int(n) % 2 == 0:
        return "even"
    else:
        return "odd"


def percentage(a, b):
    if b == 0:
        return None
    return (a / b) * 100


def show_menu():
    print("\n===== PYTHON CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "7":
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Invalid choice. Please select a number from 1 to 7.")
            continue

        if choice == "5":
            num = get_number("Enter a number: ")
            print(f"{num} is {check_even_odd(num)}.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == "2":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == "3":
            print(f"{num1} x {num2} = {multiply(num1, num2)}")

        elif choice == "4":
            result = divide(num1, num2)
            if result is None:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"{num1} / {num2} = {result}")

        elif choice == "6":
            result = percentage(num1, num2)
            if result is None:
                print("Error: Cannot calculate percentage with respect to zero.")
            else:
                print(f"{num1} is {result:.2f}% of {num2}")


if __name__ == "__main__":
    main()
