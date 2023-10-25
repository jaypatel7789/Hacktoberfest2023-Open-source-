import cmath

def complex_calculator():
    print("Complex Number Calculator")
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Exiting the calculator.")
            break
        
        real_part1 = float(input("Enter the real part of the first complex number: "))
        imag_part1 = float(input("Enter the imaginary part of the first complex number: "))
        num1 = complex(real_part1, imag_part1)
        
        real_part2 = float(input("Enter the real part of the second complex number: "))
        imag_part2 = float(input("Enter the imaginary part of the second complex number: "))
        num2 = complex(real_part2, imag_part2)
        
        if choice == '1':
            result = num1 + num2
            print(f"Result: {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"Result: {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"Result: {result}")
        elif choice == '4':
            try:
                result = num1 / num2
                print(f"Result: {result}")
            except ZeroDivisionError:
                print("Division by zero is not allowed.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    complex_calculator()
