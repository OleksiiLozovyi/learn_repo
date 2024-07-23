import pathlib

path = pathlib.Path(__file__).parent

def total_salary(path):
    try:
        with open(path / "salary.txt", "r", encoding="utf-8") as file:
            salary = list()
            line: str = file.readline()
            salary.append(line.split(',')[1])
            total = sum(salary)

    except FileNotFoundError:
        return "File not exist."


total, average = total_salary("path/to/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")