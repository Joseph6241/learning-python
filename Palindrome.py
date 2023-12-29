while 1 == 1:

    word = tuple(input("What word?"))

    if (len(word)/2).is_integer():
        if (word[:(len(word)//2)]) == (tuple(reversed(word[(len(word)//2):]))):
            palindrome = True
        else:
            palindrome = False

    else:
        if (word[:(len(word)//2)]) == (tuple(reversed(word[(len(word)//2)+1:]))):
            palindrome = True
        else:
            palindrome = False

    print(palindrome)
