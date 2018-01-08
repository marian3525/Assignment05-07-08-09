class Statistics:
    def __init__(self, bookRepo):
        self.__bookRepo = bookRepo
        self.__rentedBookFrequency = []  # holds pairs [book, timesRented]
        self.__activeClients = []  # holds pairs [client, noOfDaysRented]
        self.__rentedBookDays = []  # holds pairs [book, daysRented]
        self.__rentedAuthorFrequency = []  # holds pairs [authorId, NoOfRentedBooks]
        self.__lateRentals = []  # holds rentals with the due date in the past

    def addReturningClientToStats(self, client, startDate, endDate):
        """
        :param client: Client who returned the book
        :param startDate: date
        :param endDate: date
        :return: none
        """
        delta = endDate - startDate
        delta = delta.days

        for stat in self.__activeClients:
            if stat[0] == client:  # if the client exists in the list, update the day counter
                stat[1] += delta
                return
        # if it isn't, add a new entry to the list]
        self.__activeClients.append([client, delta])

    def getActiveClients(self):
        """
        :return: a sorted list containing the most active clients sorted by no. of books rented
        """
        return sorted(self.__activeClients, key=lambda stat: stat[1])

    def addReturnedBookToStats(self, book, startDate, endDate):
        """
        :param book: Book rented
        :param startDate: date
        :param endDate: date
        :return: None
        """
        delta = endDate - startDate
        delta = delta.days

        for stat in self.__rentedBookDays:
            if book == stat[0]:  # if the book is already in the stats, update its days rented
                stat[1] += delta
                return
        # if it isn't, add a new entry to the stats
        self.__rentedBookDays.append([book, delta])

    def getMostRentedBooksByDays(self):
        """
        :return: a list of books sorted by the number of days rented
        """
        return sorted(self.__rentedBookDays, key=lambda stat: stat[1])

    def __addAuthorToStats(self, book):
        """
        Add a book author to the stats and update them
        :param book: the author's book
        :return: nothing
        """
        for stat in self.__rentedAuthorFrequency:
            if stat[0] == book.getAuthor():  # if the author is already in the list, increase its rentals
                stat[1] += 1
                return
        # if not, create a new pair [author, noOfRentals] and append it to to list
        self.__rentedAuthorFrequency.append([book.getAuthor(), 1])

    def getMostRentedAuthors(self):
        """
        :return: A list of authors, in descending order by the number of books they rented
        """
        # returns a list of authors in descending order of the book rentals they have
        return sorted(self.__rentedAuthorFrequency, key=lambda elem: elem[1])

    def addBookToStats(self, book):
        """
        Add the rented books to the rental counter and its author to the author rental counter
        :param book: book to added
        :return:
        """
        self.__addAuthorToStats(book)

        for stat in self.__rentedBookFrequency:
            if stat[0].getId() == book.getId():  # if the book is in the stats, increase its frequency and get out
                stat[1] += 1
                return
        self.__rentedBookFrequency.append(
            [book, 1])  # if the book is not in the stats, add a pair[bookId, frequency] to it

    def getMostRentedBooksByTimes(self):
        """
        :return: a sorted list of [book, timesRented] by timesRented
        """
        sorted(self.__rentedBookFrequency, key=lambda stat: stat[1])

        listBooks = self.__rentedBookFrequency[:]
        for pair in listBooks:
            try:
                pair[0] = self.__bookRepo.getById(pair[0])
            except Exception as e:
                pass

        return listBooks

    def addLateRental(self, rental):
        """
        :param rental: the rental containing the overdue book
        :return: nothing
        """
        self.__lateRentals.append(rental)

    def getLateBooks(self):
        """
        :return: A list of books which are overdue
        """
        lateBooks = []
        for rental in self.__lateRentals:
            lateBooks.append(self.__bookRepo.getById(rental.getBookId()))
        return lateBooks

    def clearLateRentals(self):
        """
        Deletes all late rentals
        :return: None
        """
        self.__lateRentals.clear()
