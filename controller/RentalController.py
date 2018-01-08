from datetime import date, timedelta, datetime

from controller.Statistics import Statistics
from domain.Rental import Rental
from repository.repository import Repository, RepositoryException
from utils.utilities import createDateFromString
from validation.validator import Validator

import random


class RentalController:
    def __init__(self, bookRepo, clientRepo, rentalRepo,  stats):
        self.__bookRepo = bookRepo
        self.__clientRepo = clientRepo
        self.__rentalRepo = rentalRepo
        self.__validator = Validator()
        # self.__stats = Statistics(bookRepo)
        self.__stats = stats
        self.__date = datetime.now()

    def __isBookRented(self, bookId):
        """

        :param bookId: the Id of the book to check
        :return: if the books is rented or not
        """
        for rental in self.__rentalRepo.getAll():
            if rental.getBookId() == bookId:
                return True
        return False

    def __dateToString(self, date):
        """

        :param date: date object
        :return: a string dd.mm.yyyy built from the date object
        """
        output = ""
        output += str(date.day)
        output += "."
        output += str(date.month)
        output += "."
        output += str(date.year)
        return output

    def populateRentals(self):
        """
        Populate the rental Repo with some rentals
        :return:
        """
        for i in range(500):
            bookId = random.randint(1, 100)
            clientId = random.randint(1, 100)
            rentDay = random.randint(1, 30)

            rentDate = date(2017, 12, rentDay)

            rentLength = random.randint(-10, 30)

            dueDate = rentDate + timedelta(days=rentLength)

            if self.__clientRepo.existsById(clientId) and self.__bookRepo.existsById(bookId):
                self.rentBook(bookId, clientId, rentDate, self.__dateToString(dueDate))

    def rentBook(self, bookId, clientId, currentDate, dueDate):
        """
        
        :param currentDate:
        :param bookId: int
        :param clientId: int
        :param dueDate: date
        :return: a list of errors if any
        """
        rentedDate = currentDate
        dueDate = createDateFromString(dueDate)
        # returnedDate = createDateFromString(returnedDate)

        if bookId == -1 or clientId == -1 or currentDate is None:
            return "Invalid input"

        if rentedDate is None or dueDate is None:
            return "Invalid date(s)"

        if rentedDate > dueDate:
            return "Inconsistent dates"

        if self.__isBookRented(bookId):
            return "Book already rented"

        try:
            book = self.__bookRepo.getById(bookId)
            client = self.__clientRepo.getById(clientId)
        except Exception as re:
            return str(re)

        rental = Rental(Rental.getNextId(), book.getId(), client.getId(), rentedDate, dueDate, None)
        self.__rentalRepo.add(rental)
        self.__bookRepo.getById(bookId).setRented(True)

        self.__stats.addBookToStats(self.__bookRepo.getById(bookId))

        return ""

    def returnBook(self, bookId):
        """
        Marks a book as available
        :param bookId: the bookId to be returned
        :return: nothing
        """
        for rental in self.__rentalRepo.getAll():
            if rental.getBookId() == bookId:
                self.__stats.addReturnedBookToStats(self.__bookRepo.getById(bookId), rental.getRentedDate(), self.__date)
                self.__stats.addReturningClientToStats(self.__clientRepo.getById(rental.getClientId()), rental.getRentedDate(), self.__date)
                break

        for rental in self.__rentalRepo.getAll():
            if rental.getBookId() == bookId:
                self.__bookRepo.getById(rental.getBookId()).setRented(False)
                self.__rentalRepo.remove(rental)

    def getRentals(self):
        """
        :return: a list of all rentals
        """
        return self.__rentalRepo.getAll()

    def updateDate(self, currentDate):
        """
        Updates the overdue books at each date update
        :param currentDate: date
        :return: nothing
        """

        # update the overdue books
        self.__date = currentDate
        self.__stats.clearLateRentals()
        for rental in self.__rentalRepo.getAll():
            if rental.getDueDate() < currentDate:
                self.__stats.addLateRental(rental)

                # TODO update the other stats
