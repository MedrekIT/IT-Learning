def revvowels(s):
    vowels = []
    inp = []
    for i in s:
        inp.append(i)
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowels.append(i)
    s = ""
    for i in range(len(inp)):
        if inp[i] == 'a' or inp[i] == 'e' or inp[i] == 'i' or inp[i] == 'o' or inp[i] == 'u':
            inp[i] = vowels[len(vowels) - 1]
            vowels.pop()
        s += inp[i]
    print(s)
    return s

if __name__ == '__main__':
    s = input()
    revvowels(s)