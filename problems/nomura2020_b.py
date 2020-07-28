def main():
    t = list(input())

    q_list = []

    for i in range(len(t)):
        if t[i] == '?':
            q_list.append(i)

    for q in q_list:
        if q != 0 and t[q-1] == 'P':
            t[q] = 'D'
        elif q != len(t)-1 and t[q+1] == 'D':
            t[q] = 'P'
        else:
            t[q] = 'D'

    print(''.join(t))
    #score = t.count('P') + t.count('D') + t.count('PD')

if __name__ == '__main__':
    main()