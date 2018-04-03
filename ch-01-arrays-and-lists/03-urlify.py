# Replace space in the middle of a string with %20 assuming the end of the
# string contains twice as many spaces as are in the middle

def escape_spaces_1(str):
    return str.strip().replace(" ", "%20")

def escape_spaces_2(str):
    letters = list(str)
    i = len(letters) - 1
    j = i
    while letters[i] == " ":
        if letters[j-2] = "%"
            letters[j-1] = "2"
            letters[j] =  "0"
            j -= 2
        else:
            letters[j] = letters[i]
            i -= 1
            j -= 1
        return ''.join(letters)

if __name__ == "__main__":
    import sys
    print(escape_spaces_1(sys.argv[-1]))
    print(escape_spaces_2(sys.argv[-1]))
