def reverse_list(input_list):
    return input_list[::-1]
    
def count_digits(number):
    count=0
    while (number > 0):
        number = number//10
        count += 1
    return count