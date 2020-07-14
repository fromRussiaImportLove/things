letters = input("enter letters: ",)
#how_long_word = int(input("enter length of word: ",))

words_list=[]
dictionary=[]

with open("words_alpha.txt") as file_handler:
    for line in file_handler:
        dictionary.append(line.strip())

#print(dictionary)


def gen2(chars,length,wi=0,word=[],dc = {},word_list=[],initial_func=0):
   
    if initial_func == 0:
        if len(chars) < length:
            return print('is too large word, try more chars or shorter word')
        wi=0
        word=0
        word_list=[]
        dc={}
        dl = len(chars)
        for l in set(chars):
            dc[l] = list(chars).count(l)
        word = [0 for i in range(length)]

#    print('=====  ',wi+1,length, chars)

    for c in sorted(set(chars)):
#        print('='*wi+'=>',wi,c,dc[c])
        if dc[c] != 0:
            word[wi] = c
#            print('@',word)
            if wi == len(word)-1:
#                print('###word generated',''.join(word))
                word_list.append(''.join(word))
            else:    
                dc[c] -= 1
                gen2(chars,length,wi+1,word,dc,word_list,1)
                dc[c] += 1
#                print('---else_gen', dc)


#return back index position
    word[wi]=0
    wi = wi-1
#    print('-----exit func:', wi+1, word ,dc)
    return word_list


def genM(chars):

    if len(chars)<3:
        print("not enough chars, please enter 3 and more")
    chars = sorted(chars)
    print("[=]Generating words...")
    for l in range(3,len(chars)+1):
            wlist=gen2(chars,l)
            words_list.append(wlist)
    return words_list


    if initial_func == 0:
        if len(chars) < length:
            return print('is too large word, try more chars or shorter word')
#        print(chars)
        
        dl = len(chars)
        for l in set(letters):
            dc[l] = list(letters).count(l)
        word = [0 for i in range(length)]

#    print('=====  ',wi+1,length, chars)

    for c in set(chars):
#        print('='*wi+'=>',wi,c,dc[c])
        if dc[c] != 0:
            word[wi] = c
#            print('@',word)
            if wi == len(word)-1:
#                print('###word generated',''.join(word))
                word_list.append(''.join(word))
            else:    
                dc[c] -= 1
                gen2(chars,length,wi+1,word,dc,1)
                dc[c] += 1
#                print('---else_gen', dc)


#return back index position
    word[wi]=0
    wi = wi-1
#    print('-----exit func:', wi+1, word ,dc)
    return word_list


def gen(chars,length,wi=0,word=[],initial_func=0):

    if initial_func == 0:
        if len(chars) < length:
            return print('is too large word, try more chars or shorter word')
#        print(chars)
        word = [0 for i in range(length)]

#    print('=====  ',wi+1,length, chars)

    for c in chars:
        print(wi,chars[wi:],c)
        if c not in word:
            word[wi] = c
#            print('%try: ',word)
            if wi == len(word)-1:
#                print('###word generated',''.join(word))
                word_list.append(''.join(word))
            else:    
                gen(chars,length,wi+1,word,1)
#                print('---else_gen')

#return back index position
    word[wi]=0
    wi = wi-1
#    print('-----exit func:', wi+1, word)
    return word_list

#gen2(letters,how_long_word)
##print("==find words in dictionary:")
##
##for w in words_list:
##    if w in dict:
##        print(w)

        
genM(letters)

import textwrap

print("==find words in dictionary:")

for ww in range(len(words_list)):
    print("\n"+"=finding",ww+3,"letters words: ")
    t=0
    T=""
    for w in words_list[ww]:
        if w in dictionary:
            if (len(words_list[ww])>10 and w[0] != T
                and ww < 3):
                t = 0
                print("\n",w[0],":\t",end="",sep="")
            if ww == 0:
                print(w,"\t",end="")
                t += 1
                if t == 9:
                    print("\n\t",end="")
                    t = 0
            elif ww == 1:
                print(w,"\t",end="")
                t += 1
                if t == 7:
                    print("\n\t",end="")
                    t = 0
            elif ww == 2:
                print(w,"\t",end="")
                t += 1
                if t == 5:
                    print("\n\t",end="")
                    t = 0
            else:
                print(w)
            T = w[0]
        
print("[+] Mission accomplished!")
