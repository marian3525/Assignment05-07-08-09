from utils.utilities import ListingException, UpdateException


class Validator:
    def validateNewBook(self, id, title, desc, author):
        """
        :param id: int
        :param title: string
        :param desc: string
        :param author: author
        :return: "" if the input data is correct, an error string otherwise
        """
        errorString = ""

        if id == -1:
            errorString += "Invalid ID, must be an integer \n"
        if len(title) == 0:
            errorString += "The title cannot be empty \n"
        if len(desc) == 0:
            errorString += "The description cannot be empty \n"
        if len(author) == 0:
            errorString += "The author name cannot be empty \n"

        return errorString

    def validateNewClient(self, id, name):
        """

        :param id: int
        :param name: string
        :return:  "" if the data was correct, an error string otherwise
        """
        errorString = ""

        if id == -1:
            errorString += "Invalid ID, must be an integer \n"
        if len(name) == 0:
            errorString += "Name cannot be empty"

        return errorString
