from DTO.company import Company
class CompanyHandler:
    def __init__(self,CompanyEX) -> None:
        self._Company:Company=CompanyEX
    def handleCompanyModification(self):
        while True:
            try:
                Command = int(input("What would you like to do?\n1. Change the Company Name\n2. Change the Company Address\n3. Change the Company Matricule\n4. Change the Company Phone Number\n5. All of the above\n6. Quit\n"))
                
                if 1 <= Command <= 6:
                    if Command == 1:
                        self._Company.Name = input("What is the new name of the company?\n")
                    elif Command == 2:
                        self._Company.Address = input("What is the new address of the company?\n")
                    elif Command == 3:
                        self._Company.MF = input("What is the new Matricule of the company?\n")
                    elif Command == 4:
                        self._Company.Phone = input("What is the new phone number of the company?\n")
                    elif Command == 5:
                        self._Company.Name = input("What is the new name of the company?\n")
                        self._Company.Address = input("What is the new address of the company?\n")
                        self._Company.MF = input("What is the new matricule of the company?\n")
                        self._Company.Phone = input("What is the new phone number of the company?\n")
                    elif Command == 6:
                        break  # Exit the loop and quit the function
                else:
                    print("Please enter a number between 1 and 6.")
            
            except ValueError:
                print("Invalid input. Please enter a valid number between 1 and 6.")
    def Company(self):
        return self._Company