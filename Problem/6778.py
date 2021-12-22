def main():
    antenna = int(input())
    eyes = int(input())
    if isTroyMartian(antenna, eyes):
        print('TroyMartian')
    if isVladSaturnian(antenna, eyes):
        print('VladSaturnian')
    if isGraemeMercurian(antenna, eyes):
        print('GraemeMercurian')


def isTroyMartian(antenna, eyes):
    if antenna >= 3 and eyes <= 4:
        return True
    else:
        return False


def isVladSaturnian(antenna, eyes):
    if antenna <= 6 and eyes >= 2:
        return True
    else:
        return False


def isGraemeMercurian(antenna, eyes):
    if antenna <= 2 and eyes <= 3:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
