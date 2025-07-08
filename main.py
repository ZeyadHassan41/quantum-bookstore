from book import PaperBook, EBook, ShowcaseBook
from store import Bookstore


def run_test():
    store = Bookstore()

    paper = PaperBook("ISBN001", "Python Basics", 2020, 100, "John Doe", 10)
    ebook = EBook("ISBN002", "Calculus", 1980, 50, "michael spivak", "PDF")
    demo = ShowcaseBook("ISBN003", "ضربة البجاية", 2023, 0, "نجاتي ")

    store.add_book(paper)
    store.add_book(ebook)
    store.add_book(demo)

    store.remove_books(years_of_validity=5, current_year=2025)
    try:
        store.buy_book("ISBN001", 2, "user@example.com", "123 Street")
    except ValueError as e:
        print(e)

    try:
        store.buy_book("ISBN002", 1, "user@example.com", "")
    except ValueError as e:
        print(e)

    try:
        store.buy_book("ISBN003", 1, "user@example.com", "")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    run_test()
