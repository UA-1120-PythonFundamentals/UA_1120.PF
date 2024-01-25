

def count_letter(some_str):
    """
        Count the occurrences of each letter in the given string.

        Parameters:
            - some_str (str): The input string for which letter occurrences need to be counted.

        Returns:
            - dict: A dictionary containing each unique letter as a key
                    and its count as the corresponding value.
    """
    res_dict = {}
    for i in some_str:
        if i not in res_dict.keys():
            res_dict[i] = some_str.count(i)
    return res_dict


print(count_letter('hello'))