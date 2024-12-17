def reverse_num(num: int) -> int:
    # Write your code here.

    # Declare empty int value to stored as return value
    reverse_int = 0
    # Store input num to use in finding digits of number
    temp_number = num
    # Use in counting input number digit
    digits = 0
    
    # Counting the digit by using "//" operator as floor division
    while temp_number > 0:
        temp_number = temp_number // 10
        digits += 1
        
    # To reverse the number, first step is knowing the digit of input number like 1234 is 4 digits
    # Then the last digit which is 4 need to be the first digit as per value 4 need to be 4000 as 1 digit convert to 4 digits
    # To get 4 from 1234 the mod is used as 1234 mod 10 = 4, then use 4 * 1000 which formula can be 4 * 10^3(digits(4)-1)
    # but if we want 3 which is 1234 mod 100 = 34, the 34 need to be divied by 10 to get 3, then use 3 * 10^2
    # Therefore the formula can be describe with two parts as (extraction_of_number) * (digits_adjustment)
    # (extraction_of_number) = [input_number mod 10^(current_digit) // 10^(digit_before)] 
    # (digits_adjustment) = [10^(wanted_digits)] 
    # For example 17215 want to convert 7000 to 70 [17215 mod 10^4 // 10^3] * [10^1] => 7 * 10 => 70
    
    # Use range for loop then use i and digits in reverse digits formula
    for i in range(1, digits+1):
        #test number parameter for formula
        #print(num, 10**i, 10**(i-1), 10**(digits-i)) 
        extraction_of_number = (num % 10**i) // 10**(i-1)
        digits_adjustment = 10**(digits-i)
        reverse_int += extraction_of_number * digits_adjustment

    return reverse_int
    pass

# Run this file for test
assert reverse_num(1234) == 4321
assert reverse_num(20903) == 30902
assert reverse_num(1_000_234) == 4320001
assert reverse_num(4444) == 4444
assert reverse_num(1) == 1
assert reverse_num(0) == 0