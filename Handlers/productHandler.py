from DTO.product import Product
class ProductHandler:
    def __init__(self,Products=[]) -> None:
        self._Products=Products
        self._ProductToModify=-1
        self.calculateGlobalTotal()
        self._Total=0
    def calculateGlobalTotal(self):
        for subtotal in self._Products:
            self._Total+=subtotal.Total
        pass

    def modifyProoducts(self):
        print(self._Products)
        if self._Products==[]:
            print("THERE IS NO PRODUCTS TO MODIFY")
        elif len(self._Products)==1:
            self.handleSingleProduct()
        else:
            self.handleMultipleProducts()
    def handleSingleProduct(self):
        Command = 0
        while True:
            try:
                Command = int(input("What would you like to do?\n1. Change the product's Name\n2. Change the product's quantity\n3. Change the product's price\n4. All of the above\n5. Quit\n"))
                
                if 1 <= Command <= 5:
                    if Command == 1:
                        self._Products[0].Name = input("What is the new name of the product?\n")
                    elif Command == 2:
                        self._Products[0].Quantity = input("What is the new quantity of the product?\n")
                    elif Command == 3:
                        self._Products[0].Price = input("What is the new price of the product?\n")
                    elif Command == 4:
                        self._Products[0].Name = input("What is the new name of the product?\n")
                        self._Products[0].Quantity = input("What is the new quantity of the product?\n")
                        self._Products[0].Price = input("What is the new price of the product?\n")
                    elif Command == 5:
                        break  # Exit the loop and quit the function
                else:
                    print("Please enter a number between 1 and 5.")

            except ValueError:
                print("Invalid input. Please enter a valid number between 1 and 5.")

    def handleMultipleProducts(self):
        while True:
            try:
                self._ProductToModify = int(input("What is the number of the product you want to modify?\n"))
                if 0 < self._ProductToModify <= len(self._Products):
                    break  
                else:
                    print(f"Please enter a number between 1 and {len(self._Products)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        Command = 0
        while True:
            try:
                Command = int(input("What would you like to do?\n1. Change the product's Name\n2. Change the product's quantity\n3. Change the product's price\n4. All of the above\n5. Quit\n"))
                
                if 1 <= Command <= 5:
                    if Command == 1:
                        self._Products[self._ProductToModify-1].Name = input("What is the new name of the product?\n")
                    elif Command == 2:
                        self._Products[self._ProductToModify-1].Quantity = int(input("What is the new quantity of the product?\n"))
                    elif Command == 3:
                        self._Products[self._ProductToModify-1].Price = int(input("What is the new price of the product?\n"))
                    elif Command == 4:
                        self._Products[self._ProductToModify-1].Name = input("What is the new name of the product?\n")
                        self._Products[self._ProductToModify-1].Quantity = int(input("What is the new quantity of the product?\n"))
                        self._Products[self._ProductToModify-1].Price = int(input("What is the new price of the product?\n"))
                    elif Command == 5:
                        break
                else:
                    print("Please enter a number between 1 and 5.")

            except ValueError:
                print("Invalid input. Please enter a valid number between 1 and 5.")

    def addProduct(self):
        NewProductName=input("What is the name of the product\n")
        NewProductQuantity=int(input("What is the quantity of the product\n"))
        NewProductPrice=int(input("What is the price of the product\n"))
        NewProduct=Product(NewProductName,NewProductQuantity,NewProductPrice)
        if self._Products==[]:
            self._Products=[NewProduct]
        else:
           self._Products.append(NewProduct)
        return self._Products
    def __str__(self):
        ObjectInformation=""
        for index,productInformation in enumerate(self._Products):
            ObjectInformation+=f"\nProduct Number {index}:\n{productInformation}"
        return ObjectInformation
    @property
    def Total(self):
        return self._Total