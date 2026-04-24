# This line starts a loop that will keep the calculator running again and again until the user chooses to quit.
# We use a loop so the program can do more than one calculation without needing to be started over each time.
while True:
    # This line starts another loop that will keep asking for the first number until the user types a valid number.
    # We do this so the program does not crash if someone accidentally types letters or symbols instead of a number.
    while True:
        # This line asks the user to type the first number and stores whatever they type in a variable named first_input.
        # We store the answer as text first so we can safely check it and handle mistakes in a friendly way.
        first_input = input("Enter the first number: ")

        # This line starts a try block, which means Python will attempt the next line and let us catch errors if the input is not a real number.
        # We use try here because beginners often type unexpected input, and we want the program to stay calm and helpful.
        try:
            # This line converts the user's text into a number with decimals if needed and saves it in a variable named first_number.
            # We use float so the calculator can work with whole numbers like 5 and decimal numbers like 2.5.
            first_number = float(first_input)

            # This line stops the first-number loop because the user entered a valid number.
            # We break here so the program can move on to asking for the operation.
            break

        # This line catches the error that happens if the text cannot be turned into a number.
        # We catch this specific error so we can show a kind message instead of showing a confusing crash message.
        except ValueError:
            # This line shows a friendly message telling the user to enter a real number.
            # We print this so the user understands what went wrong and can try again.
            print("That was not a number. Please enter a number like 5 or 2.5.")

    # This line starts a loop that keeps asking for the math operation until the user enters one of the allowed choices.
    # We use a loop here so the user can fix a typo without restarting the whole program.
    while True:
        # This line asks the user to choose an operation and stores the answer in a variable named operation.
        # We need to know which math action to perform before we can calculate a result.
        operation = input("Choose an operation (+, -, *, /): ")

        # This line checks whether the user typed one of the four allowed operation symbols.
        # We check this now so only valid choices move forward.
        if operation in ["+", "-", "*", "/"]:
            # This line stops the operation loop because the user made a valid choice.
            # We break here so the program can move on to asking for the second number.
            break

        # This line runs if the user typed something other than +, -, *, or /.
        # We use else so we can give clear feedback when the choice is not valid.
        else:
            # This line prints a friendly reminder showing the allowed operation symbols.
            # We show the valid choices so the user knows exactly what to type next.
            print("Please choose one of these operations: +, -, *, or /.")

    # This line starts another loop that keeps asking for the second number until the user enters a valid number.
    # We use this for the same reason as the first number: to prevent crashes and allow easy correction.
    while True:
        # This line asks the user to type the second number and stores the answer as text in a variable named second_input.
        # We collect the input as text first so we can safely convert it and handle errors if needed.
        second_input = input("Enter the second number: ")

        # This line starts another try block so Python can attempt to turn the second input into a number.
        # We use try again because users can accidentally type letters here too.
        try:
            # This line converts the second input from text into a number and stores it in a variable named second_number.
            # We use float again so decimal answers are supported.
            second_number = float(second_input)

            # This line stops the second-number loop because the input was a valid number.
            # We break so the program can move on to doing the math.
            break

        # This line catches the error that happens if the second input is not a valid number.
        # We catch it so the program can stay friendly and keep running.
        except ValueError:
            # This line prints a helpful message asking the user to enter a real number.
            # We do this so the mistake is easy to understand and fix.
            print("That was not a number. Please enter a number like 5 or 2.5.")

    # This line checks whether the user chose addition.
    # We need an if statement so the program can decide which math formula to use.
    if operation == "+":
        # This line adds the first number and the second number together and stores the answer in a variable named result.
        # We store the answer so we can print it in the next step.
        result = first_number + second_number

        # This line prints the finished answer for the addition problem.
        # We show the result so the user can see the outcome of the calculation.
        print("Result:", result)

    # This line checks whether the user chose subtraction.
    # We use elif so Python checks this only if the earlier addition check was false.
    elif operation == "-":
        # This line subtracts the second number from the first number and stores the answer in result.
        # We keep using the same result variable so the program stays simple and consistent.
        result = first_number - second_number

        # This line prints the finished answer for the subtraction problem.
        # We print the result right away so the user gets immediate feedback.
        print("Result:", result)

    # This line checks whether the user chose multiplication.
    # We use another elif because only one math operation should happen each time through the loop.
    elif operation == "*":
        # This line multiplies the first number by the second number and stores the answer in result.
        # We save it in result so it can be displayed clearly.
        result = first_number * second_number

        # This line prints the finished answer for the multiplication problem.
        # We do this so the user can see the result of their chosen operation.
        print("Result:", result)

    # This line runs if the operation was not +, -, or *, which means it must be division because we already validated the choices earlier.
    # We use else here to handle the final allowed math operation.
    else:
        # This line checks whether the second number is zero.
        # We must check this because dividing by zero is not allowed in math and would cause an error.
        if second_number == 0:
            # This line prints a friendly message explaining that division by zero cannot be done.
            # We show this message instead of crashing so the user can understand the problem and try again.
            print("You cannot divide by zero. Please try another calculation.")

        # This line runs if the second number is not zero.
        # We use else so division only happens when it is safe.
        else:
            # This line divides the first number by the second number and stores the answer in result.
            # We only do this after checking for zero to avoid an error.
            result = first_number / second_number

            # This line prints the finished answer for the division problem.
            # We print the result so the user can see the final answer.
            print("Result:", result)

    # This line asks the user whether they want to do another calculation or quit, and it also changes their answer to lowercase.
    # We use lower so answers like QUIT, Quit, or quit are all treated the same way.
    again = input("Type 'quit' to stop, or press Enter to do another calculation: ").lower()

    # This line checks whether the user typed the word quit.
    # We use this check to decide whether to end the main loop.
    if again == "quit":
        # This line prints a friendly goodbye message.
        # We do this so the program ends in a clear and welcoming way.
        print("Thanks for using the calculator. Goodbye!")

        # This line stops the main loop and ends the program.
        # We break here because the user asked to quit.
        break
