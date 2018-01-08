import unittest
from datetime import date

from controller.BookController import BookController
from controller.ClientController import ClientController
from controller.RentalController import RentalController
from controller.Statistics import Statistics
from domain.Book import Book
from domain.Client import Client
from domain.Rental import Rental
from repository.CSVRepository import CSVRepository
from repository.CustomListRepository import CustomRepository
from repository.PickleRepository import PickleRepository
from repository.repository import Repository
from utils.utilities import createDateFromString
from validation.validator import Validator


class Tester(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDomainBook(self):
        book = Book(1, "Title", "Description", "Author")
        self.assertTrue(book.getTitle() == "Title")
        self.assertTrue(book.getDescription() == "Description")
        self.assertTrue(book.getAuthor() == "Author")
        self.assertTrue(book.getId() == 1)
        self.assertTrue(book.isRented() != True)
        self.assertTrue(not (book == 1))

        book.setRented(True)
        self.assertTrue(book.isRented())

    def testDomainClient(self):
        client = Client(1, "Client Name")
        self.assertTrue(client.getId() == 1)
        self.assertTrue(client.getName() == "Client Name")
        self.assertTrue(not (client == 1))

    def testDomainRental(self):
        rental = Rental(Rental.getNextId(), 2, 3, createDateFromString("11.12.2017"),
                        createDateFromString("20.12.2017"), None)
        self.assertTrue(rental.getBookId() == 2)
        self.assertTrue(rental.getClientId() == 3)
        self.assertTrue(rental.getRentedDate() == date(2017, 12, 11))
        self.assertTrue(rental.getDueDate() == date(2017, 12, 20))
        self.assertTrue(rental.getReturnDate() is None)

        rental.setReturnDate(date(2017, 12, 15))
        x = str(rental)
        self.assertTrue(rental.getReturnDate() == date(2017, 12, 15))

    def testRepositoryBooks(self):
        repoBooks = Repository()
        repoText = CSVRepository("bookRepo.csv", Book(1, "e", "s", "w"))
        repoBinary = PickleRepository("binaryBookRepo.pickle")
        repoCustom = CustomRepository(Book)

        book = Book(1, "Title", "Description", "Author")
        book1 = Book(2, "Title1", "Description1", "Author1")

        self.assertEqual(repoBooks.size(), 0)
        self.assertEqual(repoBinary.size(), 0)
        self.assertEqual(repoText.size(), 0)
        self.assertEqual(repoCustom.size(), 0)

        repoBooks.add(book)
        repoBooks.add(book1)
        repoText.add(book)
        repoText.add(book1)
        repoBinary.add(book)
        repoBinary.add(book1)
        repoCustom.add(book)
        repoCustom.add(book1)

        self.assertTrue(repoBooks.existsById(1))
        self.assertTrue(repoBooks.size() == 2)
        self.assertTrue(repoBooks.getById(1) == book)
        self.assertTrue(repoBooks.existsById(2))
        self.assertTrue(repoBooks.getById(2) == book1)

        self.assertTrue(repoText.existsById(1))
        self.assertTrue(repoText.size() == 2)
        self.assertTrue(repoText.getById(1) == book)
        self.assertTrue(repoText.existsById(2))
        self.assertTrue(repoText.getById(2) == book1)

        self.assertTrue(repoBinary.existsById(1))
        self.assertTrue(repoBinary.size() == 2)
        self.assertTrue(repoBinary.getById(1) == book)
        self.assertTrue(repoBinary.existsById(2))
        self.assertTrue(repoBinary.getById(2) == book1)

        self.assertTrue(repoCustom.existsById(1))
        self.assertTrue(repoCustom.size() == 2)
        self.assertTrue(repoCustom.getById(1) == book)
        self.assertTrue(repoCustom.existsById(2))
        self.assertTrue(repoCustom.getById(2) == book1)

        repoBooks.removeById(1)
        repoBooks.remove(book1)
        repoText.removeById(1)
        repoText.remove(book1)
        repoBinary.removeById(1)
        repoBinary.remove(book1)
        repoCustom.removeById(1)
        repoCustom.remove(book1)

        self.assertTrue(repoBooks.size() == 0)
        self.assertTrue(repoBooks.existsById(1) == False)
        self.assertTrue(repoText.size() == 0)
        self.assertTrue(repoText.existsById(1) == False)
        self.assertTrue(repoBinary.size() == 0)
        self.assertTrue(repoBinary.existsById(1) == False)
        self.assertTrue(repoCustom.size() == 0)
        self.assertTrue(repoCustom.existsById(1) == False)

        repoBooks.add(book)
        repoBooks.update(Book(1, "Updated Title", "Updated Desc", "Updated Author"))

        repoText.add(book)
        repoText.update(Book(1, "Updated Title", "Updated Desc", "Updated Author"))

        repoBinary.add(book)
        repoBinary.update(Book(1, "Updated Title", "Updated Desc", "Updated Author"))

        repoCustom.add(book)
        repoCustom.update(Book(1, "Updated Title", "Updated Desc", "Updated Author"))

        self.assertTrue(repoBooks.findById(1) == 0)
        self.assertTrue(repoText.findById(1) == 0)
        self.assertTrue(repoBinary.findById(1) == 0)
        self.assertTrue(repoCustom.findById(1) == 0)

        self.assertTrue(repoBooks.getById(1).getTitle() == "Updated Title")
        self.assertTrue(repoText.getById(1).getTitle() == "Updated Title")
        self.assertTrue(repoBinary.getById(1).getTitle() == "Updated Title")
        self.assertTrue(repoCustom.getById(1).getTitle() == "Updated Title")

        self.assertTrue(repoBooks.getById(1).getDescription() == "Updated Desc")
        self.assertTrue(repoText.getById(1).getDescription() == "Updated Desc")
        self.assertTrue(repoBinary.getById(1).getDescription() == "Updated Desc")
        self.assertTrue(repoCustom.getById(1).getDescription() == "Updated Desc")

        self.assertTrue(repoBooks.getById(1).getAuthor() == "Updated Author")
        self.assertTrue(repoText.getById(1).getAuthor() == "Updated Author")
        self.assertTrue(repoBinary.getById(1).getAuthor() == "Updated Author")
        self.assertTrue(repoCustom.getById(1).getAuthor() == "Updated Author")

        self.assertTrue(str(repoBooks.getById(1)) == "BOOK ID: " + str(repoBooks.getById(1).getId()) + "| Title: " + \
                        repoBooks.getById(1).getTitle() + "| Description: " + \
                        repoBooks.getById(1).getDescription() + \
                        "| Author: " + repoBooks.getById(1).getAuthor())
        self.assertTrue(str(repoText.getById(1)) == "BOOK ID: " + str(repoText.getById(1).getId()) + "| Title: " + \
                        repoText.getById(1).getTitle() + "| Description: " + \
                        repoText.getById(1).getDescription() + \
                        "| Author: " + repoText.getById(1).getAuthor())
        self.assertTrue(str(repoBinary.getById(1)) == "BOOK ID: " + str(repoBinary.getById(1).getId()) + "| Title: " + \
                        repoBinary.getById(1).getTitle() + "| Description: " + \
                        repoBinary.getById(1).getDescription() + \
                        "| Author: " + repoBinary.getById(1).getAuthor())
        self.assertTrue(str(repoCustom.getById(1)) == "BOOK ID: " + str(repoCustom.getById(1).getId()) + "| Title: " + \
                        repoCustom.getById(1).getTitle() + "| Description: " + \
                        repoCustom.getById(1).getDescription() + \
                        "| Author: " + repoCustom.getById(1).getAuthor())

    def testRepositoryClients(self):
        repoClient = Repository()
        client = Client(1, "Name")
        client1 = Client(2, "Name1")

        self.assertTrue(repoClient.size() == 0)
        repoClient.add(client)
        self.assertTrue(repoClient.size() == 1)
        repoClient.add(client1)

        self.assertTrue(repoClient.existsById(1))
        self.assertTrue(repoClient.existsById(2))
        self.assertTrue(repoClient.getById(1).getName() == "Name")

        repoClient.removeById(1)
        self.assertTrue(repoClient.size() == 1)
        repoClient.remove(client1)
        self.assertTrue(repoClient.size() == 0)

        self.assertTrue(repoClient.existsById(1) == False)

        repoClient.add(client)
        repoClient.update(Client(1, "Updated Name"))

        self.assertTrue(repoClient.findById(1) == 0)
        self.assertTrue(repoClient.getById(1).getName() == "Updated Name")

        self.assertTrue(str(repoClient.getById(1)) == "CLIENT ID: " + str(
            repoClient.getById(1).getId()) + "| Name: " + repoClient.getById(1).getName())

    def testValidator(self):
        validator = Validator()

        msg = validator.validateNewBook(1, "Title", "Desc", "Author")
        self.assertTrue(len(msg) == 0)

        msg = validator.validateNewBook(-1, "", "", "")
        self.assertTrue(
            msg == "Invalid ID, must be an integer \nThe title cannot be empty \nThe description cannot be empty \n" \
                   "The author name cannot be empty \n")

        msg = validator.validateNewClient(1, "Name")
        self.assertTrue(len(msg) == 0)

        msg = validator.validateNewClient(-1, "")
        self.assertTrue(msg == "Invalid ID, must be an integer \nName cannot be empty")

    def testAddBook(self):
        book1 = Book(1, "Title", "Description", "Author")
        book2 = Book(2, "Title1", "Description1", "Author1")
        book3 = Book(1, "Title2", "Description2", "Author2")
        repo = Repository()
        functions = BookController(repo, Statistics(repo))

        msg1 = functions.addBook(book1.getId(), book1.getTitle(), book1.getDescription(), book1.getAuthor())

        self.assertTrue(msg1 == "")
        self.assertTrue(functions.getBooks()[0].getId() == book1.getId())
        self.assertTrue(functions.getBooks()[0].getTitle() == book1.getTitle())
        self.assertTrue(functions.getBooks()[0].getDescription() == book1.getDescription())
        self.assertTrue(functions.getBooks()[0].getAuthor() == book1.getAuthor())

        msg2 = functions.addBook(book2.getId(), book2.getTitle(), book2.getDescription(), book2.getAuthor())

        self.assertTrue(msg2 == "")
        self.assertTrue(functions.getBooks()[1].getId() == book2.getId())
        self.assertTrue(functions.getBooks()[1].getTitle() == book2.getTitle())
        self.assertTrue(functions.getBooks()[1].getDescription() == book2.getDescription())
        self.assertTrue(functions.getBooks()[1].getAuthor() == book2.getAuthor())

        msg3 = functions.addBook(book3.getId(), book3.getTitle(), book3.getDescription(), book3.getAuthor())

        self.assertTrue(msg3 == "Cannot add an existing element")

        self.assertTrue(functions.getBooks()[1].getId() == book2.getId())
        self.assertTrue(functions.getBooks()[1].getTitle() == book2.getTitle())
        self.assertTrue(functions.getBooks()[1].getDescription() == book2.getDescription())
        self.assertTrue(functions.getBooks()[1].getAuthor() == book2.getAuthor())

        self.assertTrue(functions.getBooks()[0].getId() == book1.getId())
        self.assertTrue(functions.getBooks()[0].getTitle() == book1.getTitle())
        self.assertTrue(functions.getBooks()[0].getDescription() == book1.getDescription())
        self.assertTrue(functions.getBooks()[0].getAuthor() == book1.getAuthor())

    def testRemoveBook(self):
        book1 = Book(1, "Title", "Description", "Author")
        book2 = Book(2, "Title1", "Description1", "Author1")
        book3 = Book(3, "Title2", "Description2", "Author2")
        repo = Repository()
        functions = BookController(repo, Statistics(repo))

        functions.addBook(book1.getId(), book1.getTitle(), book1.getDescription(), book1.getAuthor())
        functions.addBook(book2.getId(), book2.getTitle(), book2.getDescription(), book2.getAuthor())
        functions.addBook(book3.getId(), book3.getTitle(), book3.getDescription(), book3.getAuthor())

        msg1 = functions.removeBook(1)

        self.assertTrue(len(msg1) == 0)
        self.assertTrue(functions.getBooks()[0].getId() == book2.getId())
        self.assertTrue(functions.getBooks()[0].getTitle() == book2.getTitle())
        self.assertTrue(functions.getBooks()[0].getDescription() == book2.getDescription())
        self.assertTrue(functions.getBooks()[0].getAuthor() == book2.getAuthor())

        msg2 = functions.removeBook(1)

        self.assertTrue(msg2 == "The provided ID does not exist")
        self.assertTrue(functions.getBooks()[0].getId() == book2.getId())
        self.assertTrue(functions.getBooks()[0].getTitle() == book2.getTitle())
        self.assertTrue(functions.getBooks()[0].getDescription() == book2.getDescription())
        self.assertTrue(functions.getBooks()[0].getAuthor() == book2.getAuthor())

    def testAddClient(self):
        client1 = Client(1, "Name1")
        client2 = Client(1, "Name2")
        repo = Repository()
        functions = ClientController(repo, Statistics(repo))

        msg1 = functions.addClient(client1.getId(), client1.getName())
        self.assertTrue(len(msg1) == 0)
        self.assertTrue(functions.getClients()[0].getId() == 1)

        msg2 = functions.addClient(client2.getId(), client2.getName())
        self.assertTrue(msg2 == "Cannot add an existing element")

        self.assertTrue(functions.getClients()[0].getId() == 1)

    def testUtils(self):
        bList = []
        self.assertTrue(len(bList) == 0)
        bookRepo = Repository()
        bc = BookController(bookRepo, Statistics(bookRepo))
        bc.populateBookRepository()

        self.assertTrue(0 < len(bookRepo.getAll()) < 100)

    def testRemoveClient(self):
        client1 = Client(1, "Name1")
        client2 = Client(2, "Name2")
        repo = Repository()
        functions = ClientController(repo, Statistics(repo))

        functions.addClient(client1.getId(), client1.getName())
        functions.addClient(client2.getId(), client2.getName())

        msg1 = functions.removeClient(1)

        self.assertTrue(len(msg1) == 0)
        self.assertTrue(functions.getClients()[0].getId() == client2.getId())
        self.assertTrue(functions.getClients()[0].getName() == client2.getName())

        msg2 = functions.removeClient(1)

        self.assertTrue(msg2 == "The provided ID does not exist")
        self.assertTrue(functions.getClients()[0].getId() == client2.getId())
        self.assertTrue(functions.getClients()[0].getName() == client2.getName())

    def testRentBook(self):
        client1 = Client(1, "Name1")
        client2 = Client(2, "Name2")

        book1 = Book(1, "Title", "Description", "Author")
        book2 = Book(2, "Title1", "Description1", "Author1")

        clientRepo = Repository()
        bookRepo = Repository()
        functions = ClientController(clientRepo, Statistics(clientRepo))
        functiom = BookController(bookRepo, Statistics(bookRepo))

        functions.addClient(client2.getId(), client2.getName())
        functions.addClient(client1.getId(), client1.getName())

        functiom.addBook(book1.getId(), book1.getTitle(), book1.getDescription(), book1.getAuthor())
        functiom.addBook(book2.getId(), book2.getTitle(), book2.getDescription(), book2.getAuthor())
        rentalRepo = Repository()
        functionsr = RentalController(bookRepo, clientRepo, rentalRepo, Statistics(rentalRepo))

        msg1 = functionsr.rentBook(book1.getId(), client1.getId(), createDateFromString("23.11.2017"), "30.11.2017")

        self.assertTrue(len(msg1) == 0)
        self.assertTrue(functionsr.getRentals()[0].getBookId() == book1.getId())
        self.assertTrue(functionsr.getRentals()[0].getClientId() == client1.getId())

        msg2 = functionsr.rentBook(book2.getId, client2.getId(), createDateFromString("20.11.2017"), "19.11.2017")
        self.assertTrue(msg2 == "Inconsistent dates")

    def testUpdateBook(self):
        bookRepo = Repository()
        bc = BookController(bookRepo, Statistics(bookRepo))
        bc.populateBookRepository()
        bc.addBook(101, "Title", "Description", "Author")
        bc.updateBook(101, "title", "description", "author")

        self.assertTrue(bookRepo.getById(101).getTitle() == "title")
        self.assertTrue(bookRepo.getById(101).getAuthor() == "author")
        self.assertTrue(bookRepo.getById(101).getDescription() == "description")
