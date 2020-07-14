from itertools import permutations as pm

letters = 'aadbcer'
WORDSDICT_FILE = 'words_alpha.txt'

def wowbruteforcer(letters, wordsdict=WORDSDICT_FILE):
    generated_fixtures = set()
    dictionary = set()
    print('[=] Generating words...')
    for _ in range(3, len(letters)):
        generated_fixtures.update(set(map("".join, pm(letters,_))))
    print('[=] Loading dictionary...')
    with open(WORDSDICT_FILE, 'r') as file_handler:
        for line in file_handler:
            dictionary.add(line.strip())
    print('[?] Finding words in dictionary...')
    return generated_fixtures.intersection(dictionary)
    

# words = wowbruteforcer(letters)

def pretty_output(words):
    lenword_dict = dict()
    for word in words:
        lenword = len(word)
        lenword_dict.setdefault(lenword, [])
        lenword_dict[lenword].append(word)
    print('[=] Sorting word in alfabet')
    limit_words_in_line = {3: 10, 4:8, 5:6, 6:5, 7:4}

    for lenword in sorted(lenword_dict.keys()):
        first_letter = ''
        
        print(f'\n------------\n[{lenword}] letters words found:', end='')
        for word in sorted(lenword_dict[lenword]):
            if first_letter != word[0]:
                first_letter = word[0]
                print(f'\n{first_letter}:', end='\t')
                words_in_line = 0
            words_in_line = 1
            if words_in_line % (limit_words_in_line[lenword]) == 0:
                print('\n\t', end='')
            
            print(word, end='\t')

    print('\n[] Mission accomplished!')
            

# pretty_output(words)

if __name__ == '__main__':
    letters = input("enter letters: ",)
    if not letters:
        letters = 'aadbcer'
    pretty_output(wowbruteforcer(letters))
