booksPrice = int(input())
books = [int(input()) for _ in range(9)]

lastBookPrice = booksPrice - sum(books)

print(lastBookPrice)
