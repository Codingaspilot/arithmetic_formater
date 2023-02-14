



def arithmetic_arranger(problems, show_answer=False):

    if len(problems) > 5:
            return "Error: Too many problems."
    results = []

    for problem in problems:
        num1, operator, num2 = problem.split()

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
                
        num1 = int(num1)
        num2 = int(num2)

        if num1 > 9999 or num2 > 9999:
            return "Error: Numbers cannot be more than four digits."

        if operator == "+":
            result = num1 + num2
            operator = " + "
        elif operator == "-":
            result = num1 - num2
            operator = " - "
        
        
        results.append(f"{num1} {operator} {num2}")

        if show_answer == True:
            for i, problem in enumerate(problems):
                results[i] = results[i] + f" = {results[i]}"
    return "\n".join(results)







print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))