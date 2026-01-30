#Create a Library Management System where different library items calculate borrowing
#charges differently.
'''Library item (parent class)
Book and magazie (child class)
LibraryApp(main class)

Book IS-A libraryitem
Magazine IS-A libraryitem
LibraryApp HAS-A libraryitem

Output format
Item Type: Book
Borrow Days: 5
Borrowing Charge: 50
Or 
Item Type: Magazine
Borrow Days: 3
Borrowing Charge: 30'''

class LibraryItem:
    def __init__(self,borrow_days):
        self._borrow_days=borrow_days

    def calculate_charge(self):
        pass

    def GetItemType(self):
        return "Library Item"


class Book(LibraryItem):
    def calculate_charge(self):
        return self._borrow_days*10 #borrow charge for book=10rs per day
    def GetItemType(self):
        return "Book"

class Magazine(LibraryItem):
    def calculate_charge(self):
        return self._borrow_days*10 #borrow charge for magazine=10rs per day
    def GetItemType(self):
        return "Magazine"

class LibraryApp:
    def __init__(self,item):
        self.item=item

    def Show(self):
        print("Item type:",self.item.GetItemType())
        print("Borrow dyas:",self.item._borrow_days)
        print("Borrowing Charge:",self.item.calculate_charge())

book=Book(5)
app1=LibraryApp(book)
app1.Show()
print()

magz=Magazine(3)
app2=LibraryApp(magz)
app2.Show()









        

