class Client:
    """
    A client has an id and a name
    """

    def __init__(self, clientId, name):
        self.__clientId = clientId
        self.__name = name

    def getId(self):
        """
        :return: The id of the client
        """
        return self.__clientId

    def getName(self):
        """
        :return: The name of the client
        """
        return self.__name

    def __str__(self):
        return "CLIENT ID: " + str(self.__clientId) + "| Name: " + self.__name

    def __eq__(self, other):
        if isinstance(other, Client):
            return self.__clientId == other.getId()
        else:
            return False