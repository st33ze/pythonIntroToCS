# A palidrome is a sentence that contains the same sequence of letters reading
# it either forwards or backwards. Example: "Able was I, ere I saw Elba.". 
# Program below tries to assess if given sentence is a palidrome using recursive
# functions.

def main():

    # Get user input.
    sentence = input('Type sentence: ')
    while not sentence: sentence = input('Type sentence: ')

    if is_palidrome(sentence): print('The sentence is a palidrome!')
    else: print('The sentence is not a palidrome!')
    

def is_palidrome(sentence):
    ''' Sentence is a palidrome if first and last letter are the same and content
        between these letters is also a palidrome. '''

    first_letter, last_letter, sentence = find_letter(sentence)
    
    # If there is only one letter or no letters left, the sentence is 
    # a palidrome.
    if first_letter is None or last_letter is None: return True
    elif first_letter == last_letter: return is_palidrome(sentence)
    
    return False


def find_letter(sentence):
    ''' Returns first and last letter of given sentence. Strips sentence from
        those letters and content before and after those letters and returns it. '''
    
    first_letter, last_letter = None, None
    
    # Find first letter.
    while sentence:
        if sentence[0].isalpha():
            first_letter = sentence[0].lower()
            sentence = sentence[1:]
            break
        sentence = sentence[1:]

    # Find last letter.
    idx = len(sentence)
    while sentence:
        if sentence[idx-1].isalpha():
            last_letter = sentence[idx-1].lower()
            sentence = sentence[:idx-1]
            break
        idx -= 1
        sentence = sentence[:idx]

    return(first_letter, last_letter, sentence)
    

if __name__ == "__main__":
    main()