def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip() != "":    # .strip is used to make sure the input is not all blank space
            return user_input     # returns user_input to the call
        print("Input cannot be empty. Please try again.")


def validate_and_convert(num_str):
    try:
        return float(num_str)
        #num = float(num_str)
        #if num == 0:
            #except ZeroDivisionError as e:    # this shit didnot work
                #print("cannot divide by zero")
        #return num

    except ValueError as e:
            print("Invalid number: " + str(e))
    return None


def perform_calculation(x, y, symbol):
    if symbol == "*":
        return x * y
    elif symbol == "/":
        if y == 0:    # this is added to make sure and not overcomplicate
            return "Cannot divide by zero."  # using Zero division error worked but i needed it here and not in the validate part
        return x / y        #could make a loop but i don't wanna or i will make it then comment it
    elif symbol == "+":
        return x + y
    elif symbol == "-":
        return x - y
    else:
        return "Invalid operation symbol."


def main():
    while True:
        num1 = get_user_input("Enter the first number: ")
        num2 = get_user_input("Enter the second number: ")

        x = validate_and_convert(num1)
        y = validate_and_convert(num2)

        if x is None or y is None:
            print("Both inputs need to be valid numbers. Please try again.")
            continue

        symbol = input("Enter an operation (*, /, +, -): ")

        result = perform_calculation(x, y, symbol)
        print("Result: " + result)

        continue_prompt = input("Do you want to perform another calculation? (yes to continue): ").strip().lower()
        if continue_prompt != 'yes':
            break

print("Thanks for using!")
