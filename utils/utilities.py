from domain.Book import Book
from domain.Client import Client
from domain.Rental import Rental
from datetime import date


class ListingException(Exception):
    pass


class UpdateException(Exception):
    pass

"""
def populateBooksList(bList):

    bList.append(Book(101, "The title", "Description", "Author"))
    for i in range(10):
        bList.append(Book(i, "Title" + str(i), "Description " + str(i), "Author " + str(i)))


def populateClientsList(cList):
    cList.append(Client(101, "The client name"))
    for i in range(3):
        cList.append(Client(i + 2, "Name " + str(i)))


def populateRentalList(rList):
    for i in range(5):
        if i % 2 == 0:
            rList.append(Rental(i + 5, 6, 3, date(2017, 12, i + 1), date(2017, 12, i + 15), None))
        else:
            rList.append(Rental(i + 5, 6, 3, date(2017, 12, i + 1), date(2017, 12, i + 15), date(2017, 12, i + 10)))
"""

def createDateFromString(dateString):
    """
    :param dateString: string in the format dd.mm.yyyy
    :return: a date object built from the string
    """
    dateString = dateString.split(".")
    for x in dateString:
        x.strip(".")
    try:
        return date(int(dateString[2]), int(dateString[1]), int(dateString[0]))
    except Exception as ve:
        return None