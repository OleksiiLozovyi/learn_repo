pattern = input("Введіть назву оператора (наприклад, Test1): ")
with open("1.txt", "r") as file:
    for line in file:
        if pattern in line:
            ip = line[:line.find('1;')].strip()
            print(ip)