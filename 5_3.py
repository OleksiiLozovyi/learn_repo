def parse_log_line(line):
    date, time, level, message = line.strip().split(' ', 3)
    return {"date": date, "time": time, "level": level, "message": message}


def load_logs(file_path: str) -> list:
    data = []
    with open(file_path, "r") as log:
        for line in log:
            data.append(parse_log_line(line))
    return data


def filter_logs_by_level(logs, level):
    return [log for log in logs if log['level'] == level]


def count_logs_by_level(logs: list) -> dict:
    count = {}
    for log in logs:
        level = log['level']
        if level in count:
            count[level] += 1
        else:
            count[level] = 1
    return count


def display_log_counts(counts: dict):
    print(f"Рівень логування | Кількість")
    print(f'{"_" * 28}')
    for level, count in counts.items():
        print(f"{level}{" "*(17-len(level))}| {count}")


logs = load_logs("path/to/logfile.log")
log_counts = count_logs_by_level(logs)
display_log_counts(log_counts)
