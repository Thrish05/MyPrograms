
numbers = int(input("Let's start calculating!"+ "\n" + "Enter the total number of terms to be operated on: "))
max_numbers = 10
if numbers == 1:
    print("Please enter two or more numbers!")
elif 2 <= numbers <= 10:
    user_input = input("Please enter the type of mathematical operation: ")
    final_input = user_input.lower()
    if final_input == "add" or final_input == "addition":
        sum = 0
        for i in range(1, numbers+1):
            input_for_adding = int(input(f"Please enter number {i}: "))
            sum+=input_for_adding
        print(sum)
    elif(final_input == "subtract" or final_input == "subtraction" or final_input == "sub"):
        subtraction_list = []
        for i in range(1, numbers+1):
            input_for_subtracting = int(input(f"Please enter number {i}: "))
            subtraction_list.append(input_for_subtracting)
        result = subtraction_list[0]
        for a in subtraction_list[1:]:
            result -= a
        print(result)
    elif(final_input == "divide" or final_input == "division" or final_input == "div"):
        division_list = []
        for i in range(1, numbers + 1):
            input_for_dividing = int(input(f"Please enter number {i}: "))
            division_list.append(input_for_dividing)
        result = division_list[0]
        for a in division_list[1:]:
            result /= a
        print(result)
    elif(final_input == "multiply" or final_input == "multiplication" or final_input == "mul"):
        multi = 1
        for i in range(1, numbers + 1):
            input_for_multiplying = int(input(f"Please enter number {i}: "))
            multi *= input_for_multiplying
        print(multi)
    elif(final_input == "exponent" or final_input == "exponential" or final_input == "expo"):
        exponent_list = []
        for i in range(1, numbers + 1):
            input_for_exponential = int(input(f"Please enter number {i}: "))
            exponent_list.append(input_for_exponential)
        result = exponent_list[0]
        for a in exponent_list[1:]:
            result = result ** a
        print(result)
    else:
        print("Please enter a valid operation keyword")
elif numbers >10:
    print("Please limit terms to maximum of 10")
else:
    print("Please enter a valid number")
