log_counts = {"INFO": 0, "ERROR": 0, "WARNING": 0}
first_error_time = None

with open("log.txt", "r") as file:
    for line in file:
        if "INFO" in line:
            log_counts["INFO"] += 1
        elif "ERROR" in line:
            log_counts["ERROR"] += 1
            if first_error_time is None:
                first_error_time = line.split("]")[0].strip("[")
        elif "WARNING" in line:
            log_counts["WARNING"] += 1

print("Số lượng log:", log_counts)
if first_error_time:
    print("Thời gian lỗi đầu tiên:", first_error_time)
