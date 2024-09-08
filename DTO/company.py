class Company:
    def __init__(self, Name="Shopify Distribution", Address="GP9-Route de la Marsa-Km11-Ain Zaghouan", MF="17583323C", Phone=52100162) -> None:
        self._Name = Name
        self._Address = Address
        self._MF = MF
        self._Phone = Phone

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, value):
        self._Name = value

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, value):
        self._Address = value

    @property
    def MF(self):
        return self._MF

    @MF.setter
    def MF(self, value):
        self._MF = value

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, value):
        self._Phone = value
    def __str__(self):
        return f"Name : {self._Name}\n Adress : {self._Address}\n Phone Number : {self._Phone}\n Matricule : {self._MF}"