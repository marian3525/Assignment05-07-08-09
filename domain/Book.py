class Book:
    """
    A book has an id, title, description and author. Its rented state should be set to True when being added to a rental
    """

    def __init__(self, bookID, title, description, author):
        self.__bookID = bookID
        self.__title = title
        self.__description = description
        self.__author = author
        self.__rented = False

    def getId(self):
        """
        :return: int The id of the book
        """
        return self.__bookID

    def getTitle(self):
        """
        :return: string The title of the book
        """
        return self.__title

    def getDescription(self):
        """
        :return: string The description of the book
        """
        return self.__description

    def getAuthor(self):
        """
        :return: string The author of the book
        """
        return self.__author

    def setRented(self, rentState):
        """
        :param rentState: is the book rented or not
        :return: nothing
        """
        self.__rented = rentState

    def isRented(self):
        """
        :return: if the book is rented or not
        """
        return self.__rented

    def __str__(self):
        return "BOOK ID: " + str(self.__bookID) + "| Title: " + self.__title + "| Description: " + self.__description + \
               "| Author: " + self.__author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.__bookID == other.getId()
        else:
            return False
