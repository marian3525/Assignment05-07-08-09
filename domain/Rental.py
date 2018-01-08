class Rental:
    """
    A rental has an ID, the rented book's ID, the client's ID, the rental date, the due date, and the date in which it
    was returned
    """
    id = 0

    def __init__(self, rentalID, bookID, clientID, rentedDate,
                 dueDate, returnedDate):
        self.__rentalID = rentalID
        self.__bookID = bookID
        self.__clientID = clientID
        self.__rentedDate = rentedDate
        self.__dueDate = dueDate
        self.__returnedDate = returnedDate

    def getRentalId(self):
        """
        :return: The id of the rental
        """
        return self.__rentalID

    def getBookId(self):
        """
        :return: The name of the rented book
        """
        return self.__bookID

    def getClientId(self):
        """
        :return: The id of the client who rented the book
        """
        return self.__clientID

    def getRentedDate(self):
        """
        :return: the date when the rental was performed
        """
        return self.__rentedDate

    def getDueDate(self):
        """
        :return: dueDate
        """
        return self.__dueDate

    def getReturnDate(self):
        return self.__returnedDate

    def setReturnDate(self, date):
        """
        :param date: date when the rental was completed by returning the book
        :return:
        """
        self.__returnedDate = date

    @staticmethod
    def getNextId():
        """
        :return: Next integer to be used as an id for building other rentals
        """

        Rental.id = Rental.id + 1
        return Rental.id

    def __str__(self):
        return str("Rental ID: " + str(self.__rentalID) + "| Book ID: " + str(self.__bookID) + "| Client ID:" +
                   str(self.__clientID) + "| Rented Date: " + str(self.__rentedDate) + "| Due date: " +
                   str(self.__dueDate) + "| Returned Date: " + str(self.__returnedDate))
