import pickle

from repository.repository import Repository


class PickleRepository(Repository):
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__repo = Repository()
        self.__clear(fileName)
        self.__loadFromFile()

    def add(self, elem):
        self.__repo.add(elem)
        self.__storeToFile()

    def remove(self, elem):
        self.__repo.remove(elem)
        self.__storeToFile()

    def removeById(self, id):
        self.__repo.removeById(id)
        self.__storeToFile()

    def update(self, elem):
        self.__repo.update(elem)
        self.__storeToFile()

    def __len__(self):
        return self.__repo.size()

    def getById(self, id):
        return self.__repo.getById(id)

    def findById(self, id):
        return self.__repo.findById(id)

    def getAll(self):
        return self.__repo.getAll()

    def existsById(self, id):
        return self.__repo.existsById(id)

    def size(self):
        return self.__repo.size()

    def __storeToFile(self):
        f = open(self.__fileName, "wb")
        pickle.dump(self.__repo.getAll(), f)
        f.close()

    def __loadFromFile(self):
        f = open(self.__fileName, "rb")
        try:
            self.__repo._elems = pickle.load(f)
        except EOFError:
            return []
        f.close()

    def __clear(self, fileName):
        """
        Clear the file
        :param fileName:
        :return: None
        """
        open(fileName, "w").close()
