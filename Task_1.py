import re


pattern = r"\n"
removing = ""

def total_salary(path):
    number_of_lines = 0
    total_salaries = 0
    try:
        with open(path, "r", encoding='utf-8') as file:
            text_in_file = file.readlines()
            for ln in text_in_file:
                line_data = re.split(',', ln)
                number_in_line = int(re.sub(pattern, removing, line_data[1]))
                total_salaries += number_in_line
                number_of_lines += 1
            
        average_salary = int(total_salaries / number_of_lines)
        return total_salaries, average_salary
    except FileNotFoundError:  
        return print("file doesn't exist")


total, average = total_salary("Salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")