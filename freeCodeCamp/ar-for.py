def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = ""
    line2 = ""
    dashes = ""
    answers = ""

    for problem in problems:
        elements = problem.split()
        operand1, operator, operand2 = elements[0], elements[1], elements[2]

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        width = max(len(operand1), len(operand2)) + 2
        line1 += operand1.rjust(width)
        line2 += operator + operand2.rjust(width - 1)
        dashes += "-" * width

        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answers += answer.rjust(width)

        if problem != problems[-1]:
            line1 += "    "
            line2 += "    "
            dashes += "    "
            answers += "    "

    arranged_problems = line1 + "\n" + line2 + "\n" + dashes
    if show_answers:
        arranged_problems += "\n" + answers

    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print('------------------')
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))