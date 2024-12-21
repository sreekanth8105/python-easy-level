def find_mth_max_nth_min(numbers, M, N):
    
    unique_numbers = sorted(set(numbers))
    
    
    if M <= len(unique_numbers) and N <= len(unique_numbers):
        mth_max = unique_numbers[-M]
        nth_min = unique_numbers[N-1]
        
     
        total_sum = mth_max + nth_min
        difference = mth_max - nth_min
        
        return mth_max, nth_min, total_sum, difference
    else:
        return "M or N is out of bounds."


numbers = [3, 1, 4, 4, 5, 2]
M = 2  
N = 3  
result = find_mth_max_nth_min(numbers, M, N)
print(result)
