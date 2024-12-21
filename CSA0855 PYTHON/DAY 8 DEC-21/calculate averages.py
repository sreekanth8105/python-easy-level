def calculate_averages():
    positive_sum = 0
    negative_sum = 0
    positive_count = 0
    negative_count = 0

    while True:
        number = int(input("Enter a number (-1 to stop): "))
        if number == -1:
            break
        elif number > 0:
            positive_sum += number
            positive_count += 1
        elif number < 0:
            negative_sum += number
            negative_count += 1

    if positive_count > 0:
        positive_average = positive_sum / positive_count
        print(f"Average of positive numbers: {positive_average}")
    else:
        print("No positive numbers were entered.")

    if negative_count > 0:
        negative_average = negative_sum / negative_count
        print(f"Average of negative numbers: {negative_average}")
    else:
        print("No negative numbers were entered.")

calculate_averages()
