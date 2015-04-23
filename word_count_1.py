#####********************************************************************************#####
#####                       Functions and Dictionaries                               #####
#####********************************************************************************#####
import itertools
nums_dict = { '1' : {(0, 2) : 'one',      (1,) :                {'0' : 'ten',
                                                                 '1' : 'eleven',
                                                                 '2' : 'twelve',
                                                                 '3' : 'thirteen',
                                                                 '4' : 'fourteen',
                                                                 '5' : 'fifteen',
                                                                 '6' : 'sixteen',
                                                                 '7' : 'seventeen',
                                                                 '8' : 'eighteen',
                                                                 '9' : 'ninteen',}},
              '2' : {(0, 2) : 'two',      (1,) : 'twenty'},
              '3' : {(0, 2) : 'three',    (1,) : 'thirty'},
              '4' : {(0, 2) : 'four',     (1,) : 'fourty'},
              '5' : {(0, 2) : 'five',     (1,) : 'fifty'},
              '6' : {(0, 2) : 'six',      (1,) : 'sixty'},
              '7' : {(0, 2) : 'seven',    (1,) : 'seventy'},
              '8' : {(0, 2) : 'eight',    (1,) : 'eighty'},
              '9' : {(0, 2) : 'nine',     (1,) : 'ninty'}
            }

def get_number(message1, message2):
    """
    message1 : string
    message2 : string
    return   : string

    Returns user input string if capable of being cast to integer, and between minus
    2 billon and positive 2 billion, else self.
    """
    user_input = raw_input(message1)
    try:
        if int(user_input) < -2000000000 or int(user_input) > 2000000000:
            print message2
            return get_number(message1, message2)
    except ValueError:
        print 'That was not valid input'
        return get_number(message1, message2)   
    return user_input

def zero_padding(user_input):
    """
    user_input : string
    return     : string

    Returns user input stripped of a minus sign (if present) and padded to the extent
    necessary with zeros to ensure that the returned string is 12 characters in length.
    """
    if user_input[0] == '-':
        user_input = user_input[1:]
    modified_input = ('0'*(12 - len(user_input))) + user_input
    return modified_input   

def convert_to_tuple_list(modified_input):
    """
    modified_input : string
    return         : tuple

    Returns tuple with four elements, each a tuple with three elements.
    Assumes modified_input has length 12.
    """
    tuple_list = tuple((tuple(modified_input[x:x+3]) for x in xrange(0, 10, 3)))
    return tuple_list

def tuple_to_text(single_tuple, unit_string, nums_dict = nums_dict):
    """
    single_tuple  : tuple 
    unit_string   : string
    nums_dict     : dict
    return        : list

    Returns list of alpha strings that represent text of numerical string characters found 
    in single_tuple. The final element of the list is the unit_sting.
    """
    word_list = [[],[]]
    if ''.join(single_tuple) == '000': # if all characters are '0' return empty list
        return list(itertools.chain(*word_list))
    if single_tuple[0] != '0': # if the fist element of the tuple is not '0'
        word_list[0].extend([nums_dict[single_tuple[0]][(0, 2)], 'hundred'])
    if single_tuple[1] != '0': # if the second element of the tuple is not '0'
        if single_tuple[1] == '1': # Special case where second character is '1'
            word_list[1].extend(['and', nums_dict['1'][(1,)][single_tuple[2]], unit_string])
        else:
            try: #if third element is zero then this will generate an error below as zero
                 #is not in the nums_dict. 
                word_list[1].extend(['and', nums_dict[single_tuple[1]][(1,)], 
                                     nums_dict[single_tuple[2]][(0, 2)], unit_string])
            except KeyError: 
                word_list[1].extend(['and', nums_dict[single_tuple[1]][(1,)], unit_string])             
    else:
        if single_tuple[2] != '0': # if first element of tuple is zero but the second is not
            word_list[1].extend(['and', nums_dict[single_tuple[2]][(0, 2)], unit_string])
        else:
            word_list[1].append(unit_string)

    if len(word_list[0]) == 0: # if no 'hundreds' then remove 'and'
        word_list[1].remove('and')
    return list(itertools.chain(*word_list))

def create_text_representation(tuple_list):
    """
    tuple_list : tuple
    return     : string

    Returns string of words found in each list created by calling the tuple_to_text
    function.
    """ 
    list1 = tuple_to_text(tuple_list[0], 'billion')
    list2 = tuple_to_text(tuple_list[1], 'million')
    list3 = tuple_to_text(tuple_list[2], 'thousand')
    list4 = tuple_to_text(tuple_list[3], '')

    #If any of the lists 1/2/3 are not empty, but list4 contains no hundred value, 
    #insert an 'and' into list4 at index position 1 if tuple_list[3] does not contain
    #elements all of which are equal to '0'
    if any([len(list1) != 0, len(list2) != 0, len(list3) != 0])\
    and 'hundred' not in list4 and ''.join(tuple_list[3]) != "000":
        list4.insert(0, 'and')

    complete_list = itertools.chain(*[list1, list2, list3, list4])
    complete_list = [elem for elem in complete_list if not type(elem) is list]
    return " ".join(complete_list)

def message(user_input, text_representation):
    """
    user_input          : string of numerical characters (possible including the minus sign)
    text_representation : string of alphas
    return              : formatted string

    Returns string formatted to include 'minus' where necessary, the original number
    provided, and the textual representation of that number.
    """
    message = \
    """
    The number {0} written as text is : 
    {1}{2}
    """
    if user_input[0] == '-':
        return message.format(user_input, 'minus ', text_representation)
    return message.format(user_input, '', text_representation)

#####********************************************************************************#####
#####                                Run Method                                      #####
#####********************************************************************************#####  
user_input = get_number("Please enter a number between -2 billion and 2 billion: ",
                        "That number is out of range")
modified_input = zero_padding(user_input)
tuple_list = convert_to_tuple_list(modified_input)
text_representation = create_text_representation(tuple_list)
print message(user_input, text_representation) 
