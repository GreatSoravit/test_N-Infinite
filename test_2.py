
def reverse_string(s: str) -> str:
    # Write your code here.
    # Do not use list reverse method
    
    # Declare empty string and stored as return string
    reverse_str = ""
    # Stored length of input string to use in for loop
    string_length = len(s)
    
    # for loop which start from length of string minus one as string index then decrement by one until 0
    for index in range(string_length-1, -1, -1) :
        # python treat string as list of character that start from index 0, so use this with last index to reverse whole string
        reverse_str += s[index]
    
    return reverse_str 
    pass

assert reverse_string("abcd") == "dcba"
assert reverse_string("a3bE5dQPos") == "soPQd5Eb3a"
assert reverse_string("aka$aka") == "aka$aka"