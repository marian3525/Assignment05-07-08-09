from utils.utilities import createDateFromString
from datetime import datetime


class Ui:
    def __init__(self, bookController, clientController, rentalController, validator, stats):

        self.__bookController = bookController
        self.__clientController = clientController
        self.__rentalController = rentalController
        self.__currentDate = createDateFromString(self.__reverseDate(datetime.now()))
        self.__validator = validator
        self.__stats = stats

    def runUi(self):

        while True:
            print("\n")
            self.__updateDate()
            self.showMenu()
            command = self.__readInt("Command:")
            if command not in range(0, 14):
                self.onInvalidData("Invalid input data: must be an int between 0 and 13")
                continue

            elif command == 1:  # add book: id, title, desc, author
                # fully working
                id = self.__readInt("Book id: ")
                title = self.__readString("Book title: ")
                description = self.__readString("Book description: ")
                author = self.__readString("Book author: ")

                str = self.__bookController.addBook(id, title, description, author)

                if len(str) != 0:
                    print(str)

            elif command == 2:  # add client: id, name
                # fully working
                id = self.__readInt("Client Id: ")
                name = self.__readString("Client name: ")

                str = self.__clientController.addClient(id, name)
                if len(str) != 0:
                    print(str)

            elif command == 3:  # remove book: id
                # fully working
                id = self.__readInt("Remove book with Id: ")

                errorMsg = self.__bookController.removeBook(id)

                if len(errorMsg) != 0:
                    print(errorMsg)

            elif command == 4:  # remove client: id
                # fully working
                id = self.__readInt("Remove client with Id: ")
                errorMsg = self.__clientController.removeClient(id)

                if len(errorMsg) != 0:
                    print(errorMsg)

            elif command == 5:  # update client: id, newName
                # fully working
                id = self.__readInt("Enter the id of the client to be updated: ")
                newName = self.__readString("Enter the new client name: ")
                if len(newName) == 0 or id == -1:
                    print("Invalid input")
                else:
                    self.__clientController.updateClient(id, newName)

            elif command == 6:  # update book
                # fully working

                id = self.__readInt("Enter the id of the book to be updated")
                newTitle = self.__readString("Enter the new title: ")
                newDesc = self.__readString("Enter the new description: ")
                newAuthor = self.__readString("Enter the new author: ")

                if len(newTitle) == 0 or len(newDesc) == 0 or len(newAuthor) == 0:
                    print("Invalid input")
                else:
                    self.__bookController.updateBook(id, newTitle, newDesc, newAuthor)

            elif command == 7:  # list books
                # fully working
                self.uiShowBooks(self.__bookController.getBooks())

            elif command == 8:  # list clients
                # fully working
                self.uiShowClients(self.__clientController.getClients())

            elif command == 9:  # rent book: book id, client id, start date, end date
                # fully working
                bookId = self.__readInt("Book to be rented Id: ")
                clientId = self.__readInt("Client Id who rents the book: ")
                dueDate = self.__readDateString("Due date: ")

                errorMsg = self.__rentalController.rentBook(bookId, clientId, self.__currentDate, dueDate)

                if len(errorMsg) != 0:
                    print(errorMsg)

            elif command == 10:  # return rented book
                bookId = self.__readInt("Enter the id of the book you wish to return")
                if bookId == -1:
                    print("Invalid id")
                else:
                    self.__rentalController.returnBook(bookId)

            elif command == 11:  # set current date
                # fully working
                self.__updateCurrentDate()

            elif command == 12:  # search books/clients
                # fully working
                result = [""]
                mode = self.__readInt("1. Search books\n2. Search clients")

                if mode == -1:
                    print("Invalid option")

                elif mode == 1:  # search in books
                    key = self.__readString("Search book by (id/title/description/author): ")
                    if key not in ["id", "title", "description", "author"]:
                        print("Invalid key!")
                    elif key == "id":
                        id = self.__readInt("ID to search: ")
                        result = self.__bookController.searchBookById(id)
                    elif key == "title":
                        title = self.__readString("Title to search for:")
                        result = self.__bookController.searchBookByTitle(title)
                    elif key == "description":
                        description = self.__readString("Description for search: ")
                        result = self.__bookController.searchBookByDescription(description)
                    elif key == "author":
                        author = self.__readString("Author to search: ")
                        result = self.__bookController.searchBookByAuthor(author)
                    self.uiShowBooks(result)

                elif mode == 2:  # search for clients
                    key = self.__readString("Search clients by id/name")
                    if key not in ["id", "name"]:
                        print("Invalid key")
                    elif key == "id":
                        id = self.__readInt("ID to search: ")
                        result = self.__clientController.searchClientById(id)
                    elif key == "name":
                        name = self.__readString("Name to search for:")
                        result = self.__clientController.searchClientByName(name)
                    self.uiShowClients(result)

            elif command == 13:
                # done: show late rentals,
                self.showStats()

            elif command == 0:  # exit
                break
        exit(0)

    def __showMostRentedBooksByTimes(self, list):
        print("Most rented books:\n")
        for pair in list:
            print(pair[0])
            print("Rented " + str(pair[1]) + " times")
            print("\n")

    def __showMostRentedAuthors(self, list):
        print("Most rented authors:\n")
        for pair in list:
            print(pair[0])
        print("\n")

    def __showLateRentals(self, list):
        print("Late rentals:\n")
        for book in list:
            print(book)
            print("\n")

        print("\n")

    def __showRentedBooksByDays(self, list):
        print("Longest rented books:\n")
        for pair in list:
            print(str(pair[0]) + "---" + str(pair[1]) + "days total")
        print("\n")

    def __showActiveClients(self, list):
        print("Most active clients:\n")
        for pair in list:
            print(str(pair[0]) + "---" + str(pair[1]) + "days total")
        print("\n")

    def showStats(self):

        mostRentedBooksByTimes = self.__stats.getMostRentedBooksByTimes()  # working
        mostRentedAuthors = self.__stats.getMostRentedAuthors()  # working
        lateRentals = self.__stats.getLateBooks()  # working
        mostRentedBooksByDays = self.__stats.getMostRentedBooksByDays() # working
        mostActiveClients = self.__stats.getActiveClients() # working

        self.__showMostRentedBooksByTimes(mostRentedBooksByTimes)  # working
        self.__showMostRentedAuthors(mostRentedAuthors)  # working
        self.__showLateRentals(lateRentals)  # working
        self.__showRentedBooksByDays(mostRentedBooksByDays) # working
        self.__showActiveClients(mostActiveClients) # working

    def __updateDate(self):
        self.__rentalController.updateDate(self.__currentDate)

    def __updateCurrentDate(self):
        """

        :return:
        """
        dateString = self.__readDateString("Enter the current updated date: ")
        newDate = createDateFromString(dateString)

        if newDate < self.__currentDate:
            print("Time only flows in one direction, cannot go back in time!")
        else:
            self.__currentDate = newDate
            self.__rentalController.updateDate(newDate)

    def __readInt(self, msg):
        """
        :param msg: message to print when reading data
        :return: the int value of the read string or -1 if an invalid number string was provided
        """
        cmd = input(msg)
        try:
            cmd = int(cmd)
        except ValueError:
            return -1
        return cmd

    def __readString(self, msg):
        """
        :param msg: message to print when reading data
        :return: the read string
        """
        str = input(msg)
        return str

    def onInvalidData(self, errorMsg):
        print("Error! " + errorMsg)

    @staticmethod
    def uiShowBooks(books):
        for book in books:
            print(book)

    @staticmethod
    def uiShowClients(clients):
        for client in clients:
            print(client)

    def __readDateString(self, string):
        date = None
        while date is None:
            dateString = input(string)
            date = createDateFromString(dateString)
            if date is None:
                print("Invalid date")
        return dateString

    def __reverseDate(self, date):
        dateString = ""
        dateString += str(date.day)
        dateString += "."
        dateString += str(date.month)
        dateString += "."
        dateString += str(date.year)

        return dateString

    def showMenu(self):
        s = "0.Exit \n"
        s += "1.Add book \n"
        s += "2.Add client \n"
        s += "3.Remove book \n"
        s += "4.Remove client \n"
        s += "5.Update client \n"
        s += "6.Update book \n"
        s += "7.List books \n"
        s += "8.List clients \n"
        s += "9.Rent book\n"
        s += "10.Return rented book\n"
        s += "11.Set current date\n"
        s += "12.Search for books/clients\n"
        s += "13.Show statistics\n"

        print(s)
