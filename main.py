def main():

    #initializes book list
    bookList = []

    choice = 0

    #keeps running until user quits
    while choice != 4:
        print("*** Book Manager *** \n1) Add a book\n2) Lookup a book\n3) Display all books\n4) Quit")
        choice = int(input())

        #adds book
        if choice == 1:
            print("Adding book...")
            nBook = input("Enter Book Name: ")
            nAuthor = input("Enter Author Name:")
            nPages = input("Enter Number of Pages:")
            bookList.append([nBook, nAuthor, nPages])
        
        #looks for book
        elif choice == 2:
            print("Looking for a book...")
            keyword = input("Enter Search Term: ")
            for book in bookList:
                if keyword in book:
                    print(book)
                else:
                    print("Book cannot be found.")

        #displays all book
        elif choice == 3:
            x = 1
            for book in bookList:
                print(f"{x}) {" | ".join(book[:2])} | {book[2]} pages")
                x += 1


if __name__ == "__main__":
    main()