from domain.Book import Book
from domain.Client import Client
from domain.Rental import Rental
from repository.repository import Repository, RepositoryException
from utils.utilities import createDateFromString


class CSVRepository(Repository):
    def __init__(self, fileName, objectType):
        self.__fileName = fileName
        self.__repo = Repository()
        self.__clear(fileName)
        self.type = objectType
        self.__loadFromFile(objectType)

    def __clear(self, fileName):
        """
        Clear the file
        :param fileName:
        :return: None
        """
        open(fileName, "w").close()

    def add(self, elem):
        """
        Write the updated list to the file
        :param elem: elem to be added
        :return:
        """
        self.__repo.add(elem)
        self.__storeToFile(elem)

    def remove(self, elem):
        """
        Remove elem from the repo
        :param elem:
        :return:
        """
        self.__repo.remove(elem)
        self.__storeToFile(elem)

    def removeById(self, id):
        """
        :param id: int
        :return: The element with the id id
        """
        self.__repo.removeById(id)
        self.__storeToFile(self.type)     #TODO

    def update(self, elem):
        """
        Update an element
        :param elem:
        :return: None
        """
        self.__repo.update(elem)
        self.__storeToFile(elem)

    def __len__(self):
        return len(self.__repo)

    def getById(self, id):
        """
        :param id: int
        :return: The element with the id id
        """
        return self.__repo.getById(id)

    def findById(self, id):
        """

        :param id: int
        :return: the index of the elem with the id id
        """
        return self.__repo.findById(id)

    def getAll(self):
        """

        :return: a list of all elements
        """
        return self.__repo.getAll()

    def existsById(self, id):
        """

        :param id: int
        :return: True if the element with the id is in the repo
        """
        return self.__repo.existsById(id)

    def size(self):
        """
        :return: The number of elements in the repo
        """
        return self.__repo.size()

    def __storeToFile(self, type):
        """
        :param elemSample: element
        :return: None
        """
        f = open(self.__fileName, "w")

        # handle each type of object accordingly
        if type == Book:
            for book in self.__repo.getAll():
                output = str(book.getId()) + ","
                output += book.getTitle() + ","
                output += book.getDescription() + ";"
                output += book.getAuthor()
                output += "\n"
                f.write(output)

        if type == Client:
            for client in self.__repo.getAll():
                output = str(client.getId()) + ","
                output += client.getName()
                output += "\n"
                f.write(output)

        if type == Rental:
            for rental in self.__repo.getAll():
                output = str(rental.getRentalId()) + ","
                output += str(rental.getBookId()) + ","
                output += str(rental.getClientId()) + ","
                output += str(rental.getRentedDate()) + ","
                output += str(rental.getDueDate()) + ","
                output += str(rental.getReturnDate())
                output += "\n"
                f.write(output)

        f.close()

    def __loadFromFile(self, type):
        """
        :param sample: Element
        :return: None
        :raises RepositoryException when the file cannot be read for some reason
        """
        try:
            f = open(self.__fileName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")

                if type == Book:
                    book = Book(int(attrs[0]), attrs[1], attrs[2], attrs[3])
                    self.__repo.add(book)
                    line = f.readline().strip()

                if type == Client:
                    client = Client(int(attrs[0]), attrs[1])
                    self.__repo.add(client)
                    line = f.readline().strip()

                if type == Rental:
                    rental = Rental(int(attrs[0]), int(attrs[1]), int(attrs[2]),
                                    createDateFromString(self.__reverseDate(attrs[3])),
                                    createDateFromString(self.__reverseDate(attrs[4])),
                                    createDateFromString(self.__reverseDate(attrs[5])))
                    self.__repo.add(rental)
                    line = f.readline().strip()
        except IOError:
            raise RepositoryException()
        finally:
            f.close()
