def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    F = int(input())

    scienceScore = sum([A, B, C, D]) - min(A, B, C, D)
    literatureScore = max(E, F)

    print(scienceScore + literatureScore)


if __name__ == '__main__':
    main()
