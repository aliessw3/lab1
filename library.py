class Library:
    libraries_quantity=0
    def __init__(self):
        Library.libraries_quantity+=1
        self.books={}
    def add_book(self, title):
        self.books[title]= True
    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
    def find_book(self, title):
        return self.books.get(title, False)
    def show_all_available_books(self):
        return [title for title in self.books if self.books[title]]

lib1 = Library()
lib1.add_book("1")
lib1.add_book("2")
lib1.books["1"] = False
print(lib1.find_book("1"))
print(lib1.find_book("2"))
print(lib1.show_all_available_books())
print(Library.libraries_quantity)