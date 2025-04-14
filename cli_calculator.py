from calculator import Calculator
calc = Calculator()
def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Exit")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7): ")
        
        if choice == '7':
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {calc.add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {calc.subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {calc.multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {calc.divide(num1, num2)}")
            elif choice == '5':
                print(f"Result: {calc.power(num1, num2)}")
            elif choice == '6':
                print(f"Result: {calc.square_root(num1)}")
            else:
                print("Invalid choice. Please try again.")  
        except ValueError as e:
            print(f"Error: {e}. Please enter valid numbers.")

if __name__ == "__main__":
    main()

    