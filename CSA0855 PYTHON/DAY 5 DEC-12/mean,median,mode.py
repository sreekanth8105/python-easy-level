import statistics

def calculate_statistics(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    mode = statistics.mode(data)
    
    return mean, median, mode


data = [16, 18, 27, 16, 23, 21, 19]
mean, median, mode = calculate_statistics(data)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
