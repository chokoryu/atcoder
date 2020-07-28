# ABC122 A

def main():
    b = input()

    pairs = {
        "A": "T",
        "C": "G",
        "G": "C",
        "T": "A"
    }

    print(pairs[b])

if __name__ == '__main__':
    main()