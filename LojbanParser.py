import re

# Assuming these patterns are defined at the module level
cmavo_pattern = re.compile(r"\b[a-z][aeiou]\b")
gismu_pattern = re.compile(r"\b([a-z]{2}[aeiou][a-z][aeiou]|[a-z][aeiou][a-z]{2}[aeiou])\b")
number_pattern = re.compile(r"\b\d+\b")
name_pattern = re.compile(r"\.[a-z]+\.")


def parse_input(input_str):
    statements = [stmt.strip() for stmt in input_str.split("i") if stmt.strip()]
    return [parse_statement(stmt) for stmt in statements]


def parse_statement(statement):
    # Splitting the statement into words, ensuring we strip leading/trailing whitespace
    words = [word.strip() for word in statement.split()]
    parsed_words = []

    for word in words:
        # Check each word against the regex patterns
        if cmavo_pattern.match(word):
            parsed_words.append(("cmavo", word))
        elif gismu_pattern.match(word):
            parsed_words.append(("gismu", word))
        elif number_pattern.match(word):
            parsed_words.append(("number", word))
        elif name_pattern.match(word):
            parsed_words.append(("name", word))
        else:
            # If no pattern matches, raise an error with the specific word
            raise ValueError(f"Invalid word type: '{word}'")

    return parsed_words
