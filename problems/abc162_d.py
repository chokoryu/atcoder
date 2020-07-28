# ABC162 D

import math

def main():
    n = int(input())
    s = input()

    res = 0

    for i in range(len(s)):
        firstChar = s[i]

        for j in range(i+1, len(s)):
            if s[j] != firstChar:
                secondChar = s[j]
                
                for k in range(j+1, len(s)):
                    if j - i == k - j:
                        continue
                    elif s[k] != firstChar and s[k] != secondChar:
                        thirdChar = s[k]
                        res += 1

    print(res)                        

if __name__ == '__main__':
    main()