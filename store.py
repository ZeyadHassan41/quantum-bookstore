class Bookstore:

    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.isbn] = book
        print(f"Book '{book.title}' added to inventory.")

    def remove_books(self, years_of_validity, current_year):
        removed = {}
        for isbn in list(self.books):
            book = self.books[isbn]
            if current_year - book.year > years_of_validity:
                removed[isbn] = self.books.pop(isbn)
                print(f"Removed expired book '{removed[isbn].title}'")
        return removed

    def buy_book(self, isbn, quantity, email, address):
        if isbn not in self.books:
            raise ValueError("Book not found.")

        book = self.books[isbn]
        if not book.is_sellable():
            raise ValueError("Not for sale.")

        amount_paid = book.buy(quantity, email, address)
        print(f"Purchase successful. Paid: {amount_paid}")
        return amount_paid
