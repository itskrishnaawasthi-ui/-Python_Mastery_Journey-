import csv
import os
from book import Book

class Library:
    def __init__(self):
        self.books = []
        self.filename = "books.csv"
        self.load_books()

    def load_books(self):
        """
        Loads book data from the persistent CSV storage into the runtime list.
        Performs a check for file existence to avoid FileNotFoundError during startup.
        """
        if not os.path.exists(self.filename):
            return
        
        # DictReader maps the header row to dictionary keys for more readable object instantiation
        with open(self.filename, mode='r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                book = Book(row['id'], row['title'], row['author'])
                # Explicitly cast the 'available' string back to a boolean type for logical operations
                book.available = row['available'] == 'True'
                self.books.append(book)

    def add_book(self, book_id, title, author):
        """
        Normalizes input data and appends a new record to both the in-memory list and CSV file.
        Uses title casing to ensure string comparison consistency across the application.
        """
        title = title.title()
        author = author.title()
        
        book = Book(book_id, title, author)
        self.books.append(book)
        
        # Append mode logic: Check if file exists to determine if the CSV header needs to be initialized
        file_exists = os.path.isfile(self.filename)
        with open(self.filename, mode='a', newline='') as f:
            fieldnames = ["id", "title", "author", "available"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader()
            
            writer.writerow({"id": book.book_id, "title": book.title, "author": book.author, "available": book.available})
            
        print("\n------ Book added successfully ------\n")

    def show_books(self):
        """
        Renders the current collection of books in a tabular format using f-string alignment.
        Handles empty library states and manages text truncation for UI consistency.
        """
        if not self.books:
            print("\n----- No Books in library -----\n")
        else:
            print("\n" + "="*80)
            # Field width modifiers (e.g., :<30) ensure left-alignment within a fixed character space
            print(f"{'ID':<10} | {'Title':<30} | {'Author':<20} | {'Status':<10}")
            print("-" * 80)
            for book in self.books:
                status = "Available" if book.available else "Issued"
                # Slicing strings at 30 characters prevents overflow if data exceeds column width
                print(f"{str(book.book_id):<10} | {book.title[:30]:<30} | {book.author[:20]:<20} | {status:<10}")
            print("=" * 80 + "\n")

    def save_books(self):
        """
        Synchronizes the in-memory state with the CSV file. Overwrites the file to reflect status changes.
        """
        with open(self.filename, mode='w', newline='') as f:
            fieldnames = ["id", "title", "author", "available"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            for book in self.books:
                writer.writerow({
                    "id": book.book_id, 
                    "title": book.title, 
                    "author": book.author, 
                    "available": str(book.available)
                })

    def issue_book(self, title, author):
        """
        Handles the book issuance logic. Searches for a matching Title/Author pair 
        and updates the availability flag if the book is present.
        """
        title = title.title()
        author = author.title()
        
        for book in self.books:
            # Case-insensitive comparison used for robust matching
            if book.title.lower() == title.lower() and book.author.lower() == author.lower():
                if book.available:
                    book.available = False
                    self.save_books() # Persist the updated 'False' availability status
                    print(f"\n------ Book '{book.title}',{book.author} issued successfully! ------\n")
                    return # Terminate search after successful issuance
                else:
                    print(f"\n------ Book '{book.title}' ,{book.author} is currently NOT available (already issued) ------\n")
                    return
        
        print(f"\n------ Book '{title}' not found in the library ------\n")

    def return_book(self, title, author):
        """
        Updates the book status back to available. Syncs with CSV for data persistence.
        """
        title = title.title()
        author = author.title()
        
        for book in self.books:
            if book.title.lower() == title.lower() and book.author.lower() == author.lower():
                if not book.available:
                    book.available = True
                    self.save_books() # Persist the updated 'True' availability status
                    print(f"\n------ Book '{book.title}' by {book.author} returned successfully! ------\n")
                    return
                else:
                    print(f"\n------ Book '{book.title}' by {book.author} is already marked as available ------\n")
                    return
        
        print(f"\n------ Book '{title}' by '{author}' not found in the library ------\n")

    def get_detail(self,title):
        """
        Search algorithm to find and display detailed information for a specific title.
        Handles cases where multiple editions or entries might exist for the same title.
        """
        if not self.books:
            print("\n----- No Books in library -----\n")
            return

        found = False
        title_lower = title.lower()
        for book in self.books:
            if book.title.lower() == title_lower:
                if not found:
                    print("\n" + "="*80)
                    print(f"{'ID':<10} | {'Title':<30} | {'Author':<20} | {'Status':<10}")
                    print("-" * 80)
                    found = True
                status = "Available" if book.available else "Issued"
                print(f"{str(book.book_id):<10} | {book.title[:30]:<30} | {book.author[:20]:<20} | {status:<10}")

        if found:
            print("=" * 80 + "\n")
        else:
            print(f"\n------ Book '{title}' not found in the library ------\n")
                    
