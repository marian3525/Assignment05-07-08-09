class CustomList:
    def __init__(self, type):
        self.__data = []
        self.__type = type  # the type of elements to be stored
        self.__index = 0  # current index

    def sort(self, key):  # comb sort
        """
        sorts the list
        :param key: a function to decide the order of the elements
        :return: nothing
        """
        gap = len(self.__data)
        shrink = 1.3
        swapped = False

        while not swapped:
            gap = int(gap / shrink)

            if gap > 1:
                swapped = False
            else:
                gap = 1
                swapped = True

            i = 0
            while i + gap < len(self.__data):
                if key(self.__data[i], self.__data[i + gap]):
                    self.__data[i], self.__data[i + gap] = self.__data[i + gap], self.__data[i]
                    swapped = False
                i += 1

    def append(self, elem):
        """
        :param elem: the element to be appended to the list
        :return: nothing
        :raise: TypeError if the type of elem is not the same as the type of the array
        """
        if isinstance(elem, self.__type):
            self.__data.append(elem)
        else:
            raise TypeError()

    def pop(self, index):
        del self.__data[index]

    def all(self):
        return self.__data[:]

    def index(self, elem):

        for ele in self.__data:
            if ele == elem:
                return self.__data.index(ele)

    def remove(self, elem):
        for i in range(len(self.__data)):
            if self.__data[i] == elem:
                self.__data.pop(i)

    def filter(self, isValid):
        """

        :param isValid: a function which returns true if an element passes the filter
        :return: None
        """
        result = CustomList(self.__type)

        for elem in self.__data:
            if isValid(elem):
                result.append(elem)
        return result

    def __setitem__(self, key, value):  # l[key] = value
        self.__data[key] = value

    def __getitem__(self, i):  # x = l[i]
        return self.__data[i]

    def __delitem__(self, key):  # del l[key]
        self.__data.pop(key)

    def __next__(self):  # next(iterator)
        try:
            elem = self.__data[self.__index]
        except IndexError:
            raise StopIteration()
        self.__index += 1
        return elem

    def __iter__(self):  # iterator = iter(customList)
        return self

    def __len__(self):  # len(customList)
        return len(self.__data)

    def __str__(self):  # str(customList)
        return str(self.__data)
