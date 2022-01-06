def main():
  A, B, C = map(int, input().split())
  credits = sorted([A, B, C])

  if (isTravelBack(credits)):
    print('S')
  else:
    print('N')


def isTravelBack(credits):
  if credits[0] == credits[1]:
    return True
  elif credits[1] == credits[2]:
    return True
  elif credits[0]+credits[1] == credits[2]:
    return True
  else:
    return False


if __name__ == '__main__':
  main()
