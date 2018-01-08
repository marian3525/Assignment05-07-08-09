from controller.Statistics import Statistics
from domain.Book import Book
from domain.Client import Client
from domain.Rental import Rental
from repository.CustomListRepository import CustomRepository
from repository.CSVRepository import CSVRepository
from repository.PickleRepository import PickleRepository
from repository.repository import Repository
from ui.uiModule import Ui
from validation.validator import Validator
from controller.BookController import BookController
from controller.ClientController import ClientController
from controller.RentalController import RentalController

f = open("settings.properties", "r")

mode = f.readline().split("=")
mode = mode[1].strip()

path = f.readline().split("=")
path = path[1].strip()

f.close()

if mode == "memory":
    bookRepo = Repository()
    clientRepo = Repository()
    rentalRepo = Repository()
elif mode == "text":
    bookRepo = CSVRepository(path + "bookRepo.csv", Book)
    clientRepo = CSVRepository(path + "clientRepo.csv", Client)
    rentalRepo = CSVRepository(path + "rentalRepo.csv", Rental)
elif mode == "binary":
    bookRepo = PickleRepository(path + "binaryBookRepo.pickle")
    clientRepo = PickleRepository(path + "binaryClientRepo.pickle")
    rentalRepo = PickleRepository(path + "binaryRentalRepo.pickle")
elif mode == "custom":
    bookRepo = CustomRepository(Book)
    clientRepo = CustomRepository(Client)
    rentalRepo = CustomRepository(Rental)
else:
    raise ValueError("Invalid option")

validator = Validator()
stats = Statistics(bookRepo)
bookController = BookController(bookRepo, stats)
bookController.populateBookRepository()

clientController = ClientController(clientRepo, stats)
clientController.populateClientRepository()

rentalController = RentalController(bookRepo, clientRepo, rentalRepo, stats)
#rentalController.populateRentals()

ui = Ui(bookController, clientController, rentalController, validator, stats)

ui.runUi()