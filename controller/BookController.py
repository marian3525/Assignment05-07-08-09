import random

from domain.Book import Book
from repository.repository import RepositoryException
from validation.validator import Validator


class BookController:
    def __init__(self, bookRepo, stats):
        self.__bookRepo = bookRepo
        self.__validator = Validator()
        self.__stats = stats

    def addBook(self, id, title, description, author):
        """
        
        :param id: int
        :param title: string
        :param description: string
        :param author: string
        :return: a string of errors if any
        """
        errorString = ""
        errorString += self.__validator.validateNewBook(id, title, description, author)
        if len(errorString) != 0:
            return errorString

        book = Book(id, title, description, author)

        try:
            self.__bookRepo.add(book)

        except RepositoryException as re:
            return str(re)
        return ""

    def removeBook(self, id):
        """
        
        :param id: int
        :return: a string of errors if any
        """
        id = int(id)
        if self.__bookRepo.existsById(id):
            self.__bookRepo.removeById(id)
            return ""
        else:
            return "The provided ID does not exist"

    def getBooks(self):
        """
        :return: a list of all books
        """
        return self.__bookRepo.getAll()

    def updateBook(self, id, newTitle, newDesc, newAuthor):
        """
        :param id: int
        :param newTitle: string
        :param newDesc: string
        :param newAuthor: string
        :return: None
        """
        try:
            self.__bookRepo.removeById(id)
            updatedBook = Book(id, newTitle, newDesc, newAuthor)
            self.__bookRepo.add(updatedBook)
        except RepositoryException as re:
            pass

    def populateBookRepository(self):
        """
        Populate the repo with some random entities
        :return: None
        """

        for i in range(100):
            id = random.randint(1, 100)
            title = "Title" + str(random.randint(1, 100))
            desc = "Description" + str(random.randint(1, 100))
            author = "Author" + str(random.randint(1, 100))

            if not self.__bookRepo.existsById(id):
                book = Book(id, title, desc, author)
                self.addBook(id, title, desc, author)

    def searchBookById(self, id):
        """
        :param id: int
        :return: The book with the id id or a empty list if it doesn't exist
        """
        filteredBooksList = []

        for book in self.getBooks():
            if book.getId() == id:
                filteredBooksList.append(book)
        return filteredBooksList

    def searchBookByTitle(self, title):
        """
        :param title: string
        :return: All books which contain title in their title, case insensitive
        """
        filteredBooksList = []

        for book in self.getBooks():
            if title.lower() in book.getTitle().lower():
                filteredBooksList.append(book)
        return filteredBooksList

    def searchBookByDescription(self, desc):
        """
        :param desc: string
        :return: All books which contain desc in their description, case insensitive
        """
        filteredBooksList = []

        for book in self.getBooks():
            if desc.lower() in book.getDescription().lower():
                filteredBooksList.append(book)
        return filteredBooksList

    def searchBookByAuthor(self, author):
        """
        :param author: string
        :return: All books which contain author in their author, case insensitive
        """
        filteredBooksList = []

        for book in self.getBooks():
            if author.lower() in book.getAuthor().lower():
                filteredBooksList.append(book)
        return filteredBooksList


class BookRemovalException(Exception):
    pass
