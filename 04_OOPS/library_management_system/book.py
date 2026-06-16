# Define a class named Book to act as a template for book objects
class Book:
    # Define the constructor method that runs when a new Book is created
    def __init__(self,book_id,title,author):
        
        self.book_id=book_id
        
        self.title=title
        
        self.author=author
        
        self.available=True

    # Define a method to print the details of the book instance
    def display(self):
         status="Available" if self.available else "Issued"
         # Print the book information using an f-string for formatting
         print(f"ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\nStatus: {status}")