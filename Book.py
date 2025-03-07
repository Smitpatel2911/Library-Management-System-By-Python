class Book:
    """Contains the All Information about Book In Library"""
    def __init__(self, book_id, book_title, book_author):
        self.__bookId = book_id
        self.book_title = book_title
        self.book_author = book_author
        self.available = True
    
    def __str__(self):
        """Return the atring cantaining """
        return f"Book[ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available}]"
