class Product:
    def __init__(self, Name=None, Quantity=1, PricePerUnit=0) -> None:
        self._Name = Name
        self._Quantity = Quantity
        self._PricePerUnit = PricePerUnit
        self._Total = self.calculateTotal()

    def calculateTotal(self):
        return self._Quantity * self._PricePerUnit

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, value):
        self._Name = value

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, value):
        self._Quantity = value
        self._Total = self.calculateTotal() 
    @property
    def PricePerUnit(self):
        return self._PricePerUnit

    @PricePerUnit.setter
    def PricePerUnit(self, value):
        self._PricePerUnit = value
        self._Total = self.calculateTotal() 

    @property
    def Total(self):
        return self._Total
    def __str__(self):
        return f"Name : {self._Name} | Quantity : {self._Quantity} | Price Per Unit : {self._PricePerUnit} | Total : {self._Total}"