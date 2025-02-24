n = int(input(""))

book_catalog = {}

for _ in range(n):
    book_title = input("")
    page_count = int(input(""))
    book_catalog[book_title] = page_count - 100

print(book_catalog)
