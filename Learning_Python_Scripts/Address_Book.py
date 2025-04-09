class AddressBook():
    def __init__(self, entry):
        self.addressbook = entry

    def print_address_book(self, list):
        for i in range(len(list)):
            print(list[i])

def main():
    addressbook = {"Jamieson, Lindsay": 8645551212,
                    "Cantrell, Gary" : 3215551234,
                    "Valcourt, Scott" : 2075559876}
    
    print(addressbook)
    addressbook["Viles, Weston"] = 2075555151
    print(addressbook)

    del addressbook["Jamieson, Lindsay"]
    print(addressbook)

    print("\n")

    addressbook["Jamieson, Lindsay"] = 6645551212
    AB = AddressBook(list(addressbook.items()))
    AB.print_address_book(AB.addressbook)


if __name__ == "__main__":
    main()    
