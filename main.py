def main():

    #initializes book list, calls to the the txt file, creates new file if one doesnt exist

    try:
        bookList = []
        infile = open("theBookList.txt", "r")
        line = infile.readline()
        while line:
            bookList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        print("theBookList.txt file does not exist,\nCreating a new book list")
        bookList = []

    choice = 0

    #keeps running until user quits
    while choice != 4:
        print("\n*** Book Manager *** \n1) Add a book\n2) Lookup a book\n3) Display all books\n4) Quit")
        choice = int(input("\n"))

        #adds book
        if choice == 1:
            repeat = True
            #checks if more books wants to be added
            while repeat == True:
                print("Adding book...")
                nBook = input("Enter Book Name: ")
                nAuthor = input("Enter Author Name:")
                nPages = input("Enter Number of Pages:")
                bookList.append([nBook, nAuthor, nPages])
                ans = input("Would you like to add another? (y/n) ")
                if "n" in ans.lower():
                    repeat = False
        
        #looks for book
        elif choice == 2:
            print("Looking for a book...")
            keyword = input("Enter Search Term: ")
            for book in bookList:
                if keyword in book:
                    print(f"{" | ".join(book[:2])} | {book[2]} pages")
                    break


        #displays all book
        elif choice == 3:
            x = 1
            for book in bookList:
                print(f"{x}) {" | ".join(book[:2])} | {book[2]} pages")
                x += 1
        
        #ends program
        elif choice == 4:
            print("Quitting...")
        

        else:
            print("\nEnter a valid choice.")
    print("Ended")

    #Saving to external txt file

    outfile = open("theBookList.txt", "w")
    for book in bookList:
        outfile.write(",".join(book) + "\n")
    outfile.close()


if __name__ == "__main__":
    main()