# Determine weather or not a given string contains no dublicate characters.

def contains_no_duplicates(str):
    letters = {}
    for letter in str:
        if letter in letters:
            return False
        letters[letter] = True
    return True

if __name__ == '__main__':
    import sys
    print(contains_no_duplicates(sys.argv[-1]))

