def main():
    target = "hello world"
    keys = "abcdefghijklmnopqrstuvwxyz"
    word = " "
    i = 0
    j = 0
    while word != target:
        word += ' '
        while True:
            word = word[:i] + keys[j] + word[i+1:]
            if target[i] == keys[j]:
                break
            print(word)
            j += 1
        j = 0
        i += 1
    print(word)

if __name__ == "__main__":
    main()
