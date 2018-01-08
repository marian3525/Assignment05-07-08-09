import random

from domain.Client import Client
from repository.repository import RepositoryException
from validation.validator import Validator


class ClientController:
    def __init__(self, clientRepo, stats):
        self.__clientRepo = clientRepo
        self.__validator = Validator()
        self.__stats = stats

    def addClient(self, id, name):
        """
        Adds a client to the list of clients
        :param id: int
        :param name: string
        :return: a string of errors if any
        """
        errorString = self.__validator.validateNewClient(id, name)
        if len(errorString) != 0:
            return errorString

        client = Client(id, name)

        try:
            self.__clientRepo.add(client)
        except RepositoryException as re:
            return str(re)
        return ""

    def removeClient(self, id):
        """
        Remove a client from the list
        :param id: int
        :return: a string of errors if any
        """
        id = int(id)
        if self.__clientRepo.existsById(id):
            self.__clientRepo.removeById(id)
            return ""
        else:
            return "The provided ID does not exist"

    def updateClient(self, id, newName):
        """
        Update a client's name
        :param id:
        :param newName:
        :return:
        """
        try:
            self.__clientRepo.removeById(id)
            updatedClient = Client(id, newName)
            self.__clientRepo.add(updatedClient)
        except RepositoryException as re:
            pass

    def getClients(self):
        """
        :return: a list of all clients
        """
        return self.__clientRepo.getAll()

    def populateClientRepository(self):
        """
        Populate the repo with some random values
        :return: None
        """

        for i in range(100):
            id = random.randint(1, 100)
            name = "Name" + str(random.randint(1, 100))

            if not self.__clientRepo.existsById(id):
                self.addClient(id, name)

    def searchClientById(self, id):
        """
        Return the cliet with the Id id
        :param id: int
        :return: list
        """
        filteredClientsList = []

        for client in self.getClients():
            if client.getId() == id:
                filteredClientsList.append(client)

        return filteredClientsList

    def searchClientByName(self, name):
        """
        Returns a list of clients whose name contains name, case insensitive
        :param name: string
        :return: list
        """
        filteredClientsList = []

        for client in self.getClients():
            if name in client.getName().lower():
                filteredClientsList.append(client)
        return filteredClientsList


class ClientRemovalException(Exception):
    pass
