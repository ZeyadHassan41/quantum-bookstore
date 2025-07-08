class Shipping:
    @staticmethod
    def send(address):
        print(f"Quantum book store: Paper book shipped to {address}")


class Mail:
    @staticmethod
    def send(email, filetype):
        print(f"Quantum book store: EBook ({filetype}) sent to {email}")
