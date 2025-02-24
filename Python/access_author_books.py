n = int(input())

authors = []


for _ in range(n):
    book_name = input()  # Read the book name (not used further)
    author_name = input()  # Read the author's name
    authors.append(author_name)  # Store the author's name in the list


print(", ".join(authors))
