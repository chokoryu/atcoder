# ABC123 A

def main():

    antennas = []
    for _ in range(5):
        char = int(input())
        antennas.append(char)
    
    k = int(input())
    result = 'Yay!'
    
    for antenna in antennas[::-1]:
        if antenna - antennas[0] > k:
            result = ':('
            break
    
    print(result)

if __name__ == '__main__':
    main()