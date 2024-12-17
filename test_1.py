
def accum(s: str) -> str:
    # Write your code here.
    
    # Declare empty string to store as return string 
    accum_str = ""
    # Stored length of input string to use in if case
    string_length = len(s)
    
    # Use for loop with enumerate on input string to use both iteration counter and value of single string
    for loop_times, value in enumerate(s):
        # As python can use repeat string with * operator, so the first value is uppercase then the rest is repeatable lowercase
        accum_str += str.upper(value) + str.lower(value * loop_times)  
        # Add string "-" in the end of every loop except last loop using if case with string_lengtgh to determine
        if loop_times != string_length-1:
            accum_str += "-"           
            
    return accum_str
    pass


# Run this file for test
assert accum("ZpglnRxqenU") == "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
assert accum("NyffsGeyylB") == "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
assert accum("MjtkuBovqrU") == "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu"
assert accum("EvidjUnokmM") == "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm"
assert accum("HbideVbxncC") == "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc"