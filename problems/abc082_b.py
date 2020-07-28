# ABC082 B

def main():
    s = input()
    t = input()

    list_s = []
    list_t = []

    for char in s:
        list_s.append(char)
    
    for char in t:
        list_t.append(char)
    
    if ''.join(sorted(list_s)) < ''.join(sorted(list_t)[::-1]):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()