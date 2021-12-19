def main():
    speedLimit = int(input())
    speedOfCar = int(input())
    overTheLimit = speedOfCar - speedLimit

    if 1 <= overTheLimit <= 20:
        print("You are speeding and your fine is $100.")
    elif 21 <= overTheLimit <= 30:
        print("You are speeding and your fine is $270.")
    elif 31 <= overTheLimit:
        print("You are speeding and your fine is $500.")
    else:
        print("Congratulations, you are within the speed limit!")


if __name__ == '__main__':
    main()
