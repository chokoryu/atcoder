# ABC132 A

def main():
    s = input()

    result = 'Yes'

    for char in set(s):
        if s.count(char) != 2:
            result = "No"
    
    print(result)

if __name__ == '__main__':
    main()