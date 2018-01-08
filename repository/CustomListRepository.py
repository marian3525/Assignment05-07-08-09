from utils.CustomList import CustomList


class RepositoryException(Exception):
    pass


class CustomRepository:
    def __init__(self, type):
        self._elems = CustomList(type)

    def add(self, elem):
        """

        :param elem: element to be added
        :return: None
        :raises RepositoryException when trying to add a duplicate (by id)
        """
        if elem in self._elems:
            raise RepositoryException("Cannot add an existing element")
        else:
            self._elems.append(elem)

    def remove(self, elem):
        """

        :param elem: element to be removed
        :return: None
        :raises RepositoryException when trying to delete a nonexistent element
        """
        if elem not in self._all():
            raise RepositoryException("Cannot remove a nonexistent element")
        else:
            self._elems.remove(elem)

    def removeById(self, id):
        """

        :param id: int
        :return: None
        :raises RepositoryException when id does not exist
        """
        for elem in self._all():
            if elem.getId() == id:
                self._elems.pop(self._elems.index(elem))
                return
        raise RepositoryException("Cannot remove a nonexistent element")

    def update(self, elem):
        """

        :param elem: the element to be updated
        :return: None
        :raises RepositoryException when trying to update a nonexistent element
        """
        if elem not in self._all():
            raise RepositoryException("Cannot update a nonexistent element")
        else:
            self._elems[self._elems.index(elem)] = elem

    def __len__(self):
        """
        :return: The length of the element list
        """
        return len(self._elems)

    def getById(self, id):
        """

        :param id: int
        :return: the element with the provided id
        :raises RepositoryException when the provided id does not exist in the list
        """
        for elem in self._all():
            if elem.getId() == id:
                return elem
        raise RepositoryException("No value with the given ID was found")

    def findById(self, id):
        """

        :param id: int
        :return: the element with the provided id
        :raises RepositoryException when the provided id does not exist in the list
        """
        for elem in self._all():
            if elem.getId() == id:
                return self._elems.index(elem)
        raise RepositoryException("No value with the given ID was found")

    def getAll(self):
        """
        Returns a list with all elements in the repository
        :return: None
        """
        return self._all() # TODO

    def existsById(self, id):
        """

        :param id: int
        :return: True if the element exists in the repository, False otherwise
        """
        for elem in self._all():
            if elem.getId() == id:
                return True
        return False
    '''
    def exists(self, elem):
        for e in self.__elems:
            if e == elem:
                return True
        return False
    '''
    def size(self):
        """

        :return: The size of the repository
        """
        return len(self._elems)

    def _all(self):
        return self._elems.all()
