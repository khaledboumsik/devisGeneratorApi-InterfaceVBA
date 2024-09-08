from DTO.product import Product
from DTO.company import Company
from DTO.client import Client
from Handlers.clientHandler import ClientHandler
from Handlers.companyHandler import CompanyHandler
from Handlers.productHandler import ProductHandler
class InputConstructor:
    def __init__(self) -> None:
        self._CommandNumber = 0
        self._Client: Client = Client()
        self._Company: Company = Company()
        self._Products: list[Product] = []
        self._ProductHandler=ProductHandler()
        self._clientHandler=ClientHandler(self._Client)
        self._companyHandler=CompanyHandler(self._Company)
        self.userCommand()
    def userCommand(self):
        while True:
            try:
                self._CommandNumber = int(input(
                    "What would you like to do? \n1. Input/Modify Client Information \n2. Change Company Information \n3. Add Product \n4. Display Current Information\n5. Modify Product\n6. Quit\n"
                ))

                if 1 <= self._CommandNumber <= 6:
                    if self._CommandNumber == 1:
                        self._clientHandler.handleClientModification()
                        self._Client = self._clientHandler.Client()
                    elif self._CommandNumber == 2:
                        self._companyHandler.handleCompanyModification()
                        self._companyHandler.Company()
                    elif self._CommandNumber == 3:
                        self._ProductHandler.addProduct()
                    elif self._CommandNumber == 4:
                        self.displayInformation()
                    elif self._CommandNumber == 5:
                        self._ProductHandler.modifyProducts()
                    elif self._CommandNumber == 6:
                        break  
                else:
                    print("Please enter a number between 1 and 6.")

            except ValueError:
                print("Invalid input. Please enter a valid number between 1 and 6.")
               
    def displayInformation(self):
       print("Client Information :\n",self._Client ,"\nCompany Information :\n",self._Company, "\nProducts Information :\n",self._ProductHandler)