class Author:
    all = []
    def __init__(self,name):
        if not isinstance(name, str):
            raise Exception("name must be type 'string'")
        else: 
            self.name = name
            self.__class__.all.append(self)

    def contracts(self):
        print(self.name)
        print([contract.author for contract in Contract.all])
        return [contract for contract in Contract.all if contract.author == self]


    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties): 
        if not isinstance(book, Book) or not isinstance(date, str) or not isinstance(royalties, int):
            raise Exception("Invalid contract parameters")
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        return sum(contract.royalties for contract in Contract.all if contract.author == self)

class Book:
    all = []
    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("title must be type 'string'")
        self.title = title
        self.__class__.all.append(self)

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author) or not isinstance(book, Book) or not isinstance(date, str) or not isinstance(royalties, int):
            raise Exception("Invalid contract parameters")
        else:  
            self.author = author
            self.book = book
            self.date = date
            self.royalties = royalties
            self.__class__.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
