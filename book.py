from book_sending import Mail, Shipping

class Book:
    def __init__(self, isbn, title, year, price, author):
        self.isbn = isbn
        self.title = title
        self.year = year
        self.price = price
        self.author = author

    def is_sellable(self):
        return False

    def buy(self, quantity, email, address):
        raise NotImplementedError("not availble to sell now.")
    
class PaperBook(Book):
    def __init__(self, isbn, title, year, price, author, stock):
        super().__init__(isbn, title, year, price, author)
        self.stock = stock

    def is_sellable(self):
        return True

    def buy(self, quantity, email, address):
        if quantity > self.stock:
            raise ValueError("Not enough stock for paper book.")
        self.stock -= quantity
        Shipping.send(address)
        return self.price * quantity


class EBook(Book):
    def __init__(self, isbn, title, year, price, author, filetype):
        super().__init__(isbn, title, year, price, author)
        self.filetype = filetype

    def is_sellable(self):
        return True

    def buy(self, quantity, email, address):
        if quantity > 1:
            raise ValueError("Cannot buy more than 1 copy of an ebook.")
        Mail.send(email, self.filetype)
        return self.price * quantity
    
class ShowcaseBook(Book):
    def is_sellable(self):
        return False

    def buy(self, quantity, email, address):
        raise ValueError(" not for sale.")