
def word_mesh(words: list[str]) -> str:
    # Write your code here.
        
    # Declare empty string to stored as temp and return value
    empty_string = ""
    mesh_string = ""
    # Stored length of input list
    list_length = len(words)
    # Count use for check all words in list are matched
    match_count = 1

    # Loop on words list to compare each string
    for list_no in range(list_length-1):

        # Stored string with lowercase and length of words from list based on index as first value and index+1 as second value
        first_string = str.lower(words[list_no])
        first_string_length = len(first_string)
        second_string = str.lower(words[list_no+1])
        second_string_length = len(second_string)

        # loop through first value by using list slicing start with incremental index to length of words
        for first_index in range(first_string_length):
            #test print first_string 
            #print(first_index, first_string[first_index:first_string_length])
            
            # nested loop through second value by using list slicing start with index 0 to incremental index
            for second_index in range(second_string_length):
                #test print second_string for loop compare 
                #print(second_index, second_string[0:second_index])
                
                # Compare string with nested loop from first_string and second_string
                if first_string[first_index:first_string_length] == second_string[0:second_index]:
                    #test print if compare with both string correct
                    #print( first_string[first_index:first_string_length], second_string[0:second_index])
                    
                    # stored matched string into empty string and increase count matched
                    empty_string += second_string[0:second_index]
                    match_count += 1

    # Use to check if all words in list are match if not then replace with "failed to mesh"
    if match_count == list_length:
        mesh_string = empty_string
    else:
        mesh_string= "failed to mesh"
        
    return mesh_string
    pass

# Run this file for test
assert word_mesh(["beacon", "condominium", "umbilical", "california"]) == "conumcal"
assert word_mesh(["allow", "lowering", "ringmaster", "terror"]) == "lowringter"
assert word_mesh(["abandon", "donation", "onion", "ongoing"]) == "dononon"
assert word_mesh(["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"]) == "ownhippuscartpher"
assert word_mesh(["kingdom", "dominator", "notorious", "usual", "allegory"] ) == "failed to mesh"