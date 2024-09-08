from DTO.client import Client
class ClientHandler:
    def __init__(self,ClientEx=None) -> None:
        self._Client:Client=ClientEx
    def handleClientModification(self):
        while True:
            try:
                Command = int(input("\nWhat would you like to do?\n1. Change the Client Name\n2. Change the Client Address\n3. Change the Client Phone\n4. Change All of the above\n5. Quit\n"))
                
                if 1 <= Command <= 5:
                    if Command == 1:
                        self._Client.Name = input("\nWhat is the name of the Client? ")
                    elif Command == 2:
                        self._Client.Address = input("\nWhat is the address of the Client? ")
                    elif Command == 3:
                        self._Client.Phone = int(input("\nWhat is the phone number of the Client? "))
                    elif Command == 4:
                        self._Client.Name = input("\nWhat is the name of the Client? ")
                        self._Client.Address = input("\nWhat is the address of the Client? ")
                        self._Client.Phone = int(input("\nWhat is the phone number of the Client? "))
                    elif Command == 5:
                        print("Exiting client modification.")
                        break  # Exit the loop and quit the function
                else:
                    print("Please enter a number between 1 and 5.")
            
            except ValueError:
                print("Invalid input. Please enter a valid number between 1 and 5.")

    def Client(self):
        return self._Client 