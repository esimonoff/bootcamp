def longest_common_substring(str1, str2):
    """Take str1 and str2 and find the longest common substring between them"""

    # Make sure str1 is the shorter of the two strings
    if len(str1) > len(str2):
        str1, str2 =  str2, str1

    # Initialize substring length
    substring_length = 0

    for i in range(len(str1)):
        for j in range(len(str1)):
            # Start testing all valid ranges of shorter string
            if i <= j:
                # Test if substring contained in larger string
                if str2.find(str1[i:j+1]) > 0:
                    # If substring does exist, create new substring
                    # length and position
                    if (j + 1) - i > substring_length:
                        substring_length = (j + 1) - i
                        substring_position_end = j
                        substring_position_start = i

    if substring_length > 0:
        return(str1[substring_position_start:substring_position_end+1])
    else:
        return ''
