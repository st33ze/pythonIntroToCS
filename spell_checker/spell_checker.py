# Implementation of automated spell checker used to analize documents and locate
# words that might be misspelled. The program loads txt file with over 58 000
# words and compares them with given word. If comparison fails, it is marked
# as potentially incorrect word. Program uses binary search algorithm. To change
# dictionary simply change the DICTIONARY variable, remeber that words must be 
# alphabetically sorted.

DICTIONARY = 'words.txt'


def main():
    ''' Prints if the word is correct or potentially incorrect. '''

    # Get word and validate input.
    word = input('Type word containing only letters: ')
    while not word or not word.isalpha():
        word = input('Type word containing only letters: ')
    word = word.lower()

    # Load txt file with words as list and strip its items from new line characters.
    with open(DICTIONARY, 'r') as txt_file: 
        words_dict = []
        
        for line in txt_file:
            words_dict.append(line.strip())

    # Check if the word matches with words in dictionary.
    row = 0
    if check_letter(row, word, words_dict): print('Word is correct.')
    else: print('Word is incorrect.')


def check_letter(row, word, words_dict, mid_num=None):
    ''' Checks each letter of given word, each time comparing it to the word from
        dictionary and discarding half of it, if letter is bigger or smaller. Returns
        True if word is found or False if there is no such word in dictionary. '''
    
    if not words_dict: return False
    
    # Get dictionary mid value, if needed.
    if not mid_num: mid_num = len(words_dict) // 2 
    mid_word = words_dict[mid_num]
    
    if word == mid_word: return True
    
    # Check if word or mid_word are not too short to compare and discard not 
    # needed half.
    if row + 1 > len(word):
        words_dict = words_dict[:mid_num]
        row = 0
        return check_letter(row, word, words_dict)
    
    elif row + 1 > len(mid_word):
        words_dict = words_dict[mid_num+1:]
        row = 0
        return check_letter(row, word, words_dict)
    
    # Compare letters.
    # If letters match, update row and check next letter.
    if word[row] == mid_word[row]:
        row += 1
        return check_letter(row, word, words_dict, mid_num)

    # If letter is smaller than dict letter, discard upper part of dict.
    elif word[row] < mid_word[row]:
        words_dict = words_dict[:mid_num]
        row = 0
        return check_letter(row, word, words_dict)

    # If letter is bigger than dict letter, discard lower part of dict.
    elif word[row] > mid_word[row]:
        words_dict = words_dict[mid_num+1:]
        row = 0
        return check_letter(row, word, words_dict)
    

if __name__ == "__main__":
    main()