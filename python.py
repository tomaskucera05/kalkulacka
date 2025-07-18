expression = input()
expression = expression.replace(" ", "")
def tokenize(expression):
    tokens = []
    operators = "+-*/"
    current_number = ""
    i = 0
    if i == 0 and expression[i] in "+-":
        plus_count = 0
        minus_count = 0
        while i < len(expression) and expression[i] in "+-":
            if expression[i] == "+":
                plus_count += 1
            else:
                minus_count += 1
            i += 1
        operator_sequence = "+" if minus_count % 2 == 0 else "-"
        current_number += operator_sequence
    while i < len(expression):
        char = expression[i]
        if char.isnumeric() or char == ".":
            current_number += char
        elif char in operators:
            if char in "+-":
                plus_count = 0
                minus_count = 0
                while i < len(expression) and expression[i] in "+-":
                    if expression[i] == "+":
                        plus_count +=1
                    else:
                        minus_count +=1
                    i += 1
                operator_sequence = "+" if minus_count % 2 == 0 else "-"

                if tokens and tokens[-1] in "*/":
                    current_number += operator_sequence
                else:
                    if current_number:
                        tokens.append(current_number)
                        current_number = ""
                    tokens.append(operator_sequence)
                continue    
            else:
                if current_number:
                    tokens.append(current_number)
                    current_number = ""
                tokens.append(char)
        else:
            raise ValueError
        i += 1
    if current_number:
        tokens.append(current_number)
    return tokens

def evaluate_multiplication_division(tokens):
    operators = "*/"
    i = 1
    while i < len(tokens) - 1:
        element = tokens[i]
        if element in operators:
            a = float(tokens[i-1])
            b = float(tokens[i+1])
            if element == "*":
                tokens[i-1:i+2] = [str(a*b)]
            else:
                 if b == 0:
                    raise ZeroDivisionError
                 tokens[i-1:i+2] = [str(a/b)]
            i = 1
        else:
            i +=2        
    return tokens        

def evaluate_addition_subtraction(converted_numbers_and_operators):
    result = float(converted_numbers_and_operators[0])
    i = 1
    while i < len(converted_numbers_and_operators) - 1:
        operator = converted_numbers_and_operators[i]
        if operator == "+":
            result += float(converted_numbers_and_operators[i+1])
        elif operator == "-":
            result -= float(converted_numbers_and_operators[i+1])
        i += 2
    return result

while "(" in expression:
    if ")" not in expression:
        raise ValueError("Unclosed parenthesis")
    start = expression.rfind("(")
    end = expression.find(")", start)
    inner_expression = expression[start + 1:end]
    inner_tokens = tokenize(inner_expression)
    simplified_tokens = evaluate_multiplication_division(inner_tokens)
    inner_result = str(evaluate_addition_subtraction(simplified_tokens))
    expression = expression[:start] + inner_result + expression[end + 1:]
try:
    final_tokens = tokenize(expression)
    simplified_tokens = evaluate_multiplication_division(final_tokens)
    final_result = evaluate_addition_subtraction(simplified_tokens)
    print(final_result)
except ValueError:
    print("Enter a valid input")
except ZeroDivisionError:
    print("Division by zero is impossible")
