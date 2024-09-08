import json
from DTO.product import Product
from DTO.company import Company
from DTO.client import Client

class InformationProcessorJson:
    def __init__(self,JsonPath=None):
        self._JsonPath:str=JsonPath
        self._Client:Client=None
        self._Company:Company=Company()
        self._Products: list[Product]=[] 
        self._ReceiptNumber:int=None
    def Total(self):
        Total=0
        for product in self._Products:
            Total+=product.Total
        return Total
    @property
    def JsonPath(self):
        return self._JsonPath

    @JsonPath.setter
    def JsonPath(self, value):
        self._JsonPath = value

    # Getter and Setter for _Client
    @property
    def Client(self):
        return self._Client

    @Client.setter
    def Client(self, value):
        self._Client = value

    # Getter and Setter for _Company
    @property
    def Company(self):
        return self._Company

    @Company.setter
    def Company(self, value):
        self._Company = value

    # Getter and Setter for _Products
    @property
    def Products(self):
        return self._Products

    @Products.setter
    def Products(self, value):
        self._Products = value

    # Getter and Setter for _ReceiptNumber
    @property
    def ReceiptNumber(self):
        return self._ReceiptNumber

    @ReceiptNumber.setter
    def ReceiptNumber(self, value):
        self._ReceiptNumber = value
    def fillByJsonObject(self,information):
        self._ReceiptNumber=information["Number"]
        self._Client = Client(information["Client"]["Name"], information["Client"]["Adress"], information["Client"]["Phone"])
        for ProductInfo in information["Products"]:
            self._Products.append(Product(ProductInfo["Name"], ProductInfo["Quantity"], ProductInfo["PricePerUnit"]))
        self._Company = Company(information["Seller"]["Name"], information["Seller"]["Adress"], information["Seller"]["MF"], information["Seller"]["Phone"])

    def fillByJsonPath(self):
        assert self._JsonPath is not None, "Fill the Class Via Json"
        
        with open(self._JsonPath, 'r') as file:
            information = json.load(file)
        self._ReceiptNumber=information["Number"]
        self._Client = Client(information["Client"]["Name"], information["Client"]["Adress"], information["Client"]["Phone"])
        for ProductInfo in information["Products"]:
            self._Products.append(Product(ProductInfo["Name"], ProductInfo["Quantity"], ProductInfo["PricePerUnit"]))
        self._Company = Company(information["Seller"]["Name"], information["Seller"]["Adress"], information["Seller"]["MF"], information["Seller"]["Phone"])

    def jsonInfo(self):
        assert self._JsonPath is not None, "Fill the Class Via Json"

        with open(self._JsonPath, 'r') as file:
            information = json.load(file)
        
        return information
ip=InformationProcessorJson("Information.json")
print(ip.jsonInfo())