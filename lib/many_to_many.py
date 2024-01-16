class Author:
    all = []
    def __init__(self,name):

            self.name = name
            self.__class__.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("name must be type 'string'")
        else: 
            self._name = value

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]


    def books(self):
        # return [contract.book for contract in Contract.all if contract.author == self]
        return [contract.book for contract in self.contracts()]

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

        self.title = title
        self.__class__.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("title must be type 'string'")
        else:
            self._title = value

    def contracts(self):
        return [contract for contract in Contract. all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]

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
