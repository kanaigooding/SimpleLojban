from LojbanParser import parse_input

# Placeholder for a simple database of predicates and their values
predicates = {}


# Function to evaluate parsed statements - simplified version
def evaluate_statements(parsed_statements):
    # Initialize a context to hold variable values and other state
    context = {"variables": {}, "facts": []}

    # Define handlers for each predefined predicate
    def handle_fatci(args, context):
        # 'fatci' asserts the existence of its argument (fact)
        context["facts"].append(args[0])
        return True

    def handle_sumji(args, context):
        # 'sumji' calculates the sum of the second and third arguments and assigns it to the first
        try:
            sum_result = int(args[1]) + int(args[2])
            context["variables"][args[0]] = sum_result
            return True
        except ValueError:
            return False  # In case of invalid numbers

    def handle_dunli(args, context):
        # 'dunli' asserts equality between its two arguments
        return context["variables"].get(args[0], None) == context["variables"].get(args[1], None)

    # Add more handlers for other predicates as needed

    # Mapping of predicate names to their handlers
    predicate_handlers = {
        "fatci": handle_fatci,
        "sumji": handle_sumji,
        "dunli": handle_dunli,
        # Map other predicates to their handlers
    }

    # Process each statement
    for statement in parsed_statements:
        predicate_name = statement[1][1]  # Assuming the predicate is always the second word for simplicity
        args = [word[1] for word in statement if
                word[0] != "gismu"]  # Extract arguments, excluding the predicate itself

        # Check if a swap operation ('se') is requested and swap the first two arguments if so
        if "se" in args:
            args.remove("se")
            args[0], args[1] = args[1], args[0]

        # Call the appropriate handler based on the predicate name
        if predicate_name in predicate_handlers:
            result = predicate_handlers[predicate_name](args, context)
            print(f"Statement '{' '.join([word for _, word in statement])}' evaluated to {result}")
        else:
            print(f"Unknown predicate: {predicate_name}")

    return context


def main():
    # Example input strings for test cases
    test_inputs = [
        "i lo .Brook. fatci i lo .coffee. fatci i lo pinxe cmavo lo steko lo .Brook. lo steko lo .coffee. lo steni i lo .X. pinxe lo .coffee.",
        "i lo .number. sumji 1 2 i 3 dunli lo .number.",
        "i lo .list. steko 1 lo steko 2 lo steni i lo steni fatci"
    ]

    # Process and evaluate each test input
    for input_str in test_inputs:
        print("\nProcessing input:", input_str)
        parsed_statements = parse_input(input_str)
        result = evaluate_statements(parsed_statements)
        print(result)


if __name__ == "__main__":
    main()
