# ABC119 A

def main():
    s = input()
    
    month = int(s.split('/')[1])

    if month <= 4:
        print('Heisei')
    else:
        print('TBD')

if __name__ == '__main__':
    main()

