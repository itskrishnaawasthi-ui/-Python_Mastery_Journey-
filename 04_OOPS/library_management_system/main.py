# Import the Library class from the library module
from library import Library
lib=Library()

# Start an infinite loop to keep the program running until the user chooses to exit
while True:
  # Display the menu options to the user
  print("\n-----Library Menu-------\n")
  print("1.Add Book")
  print("2.Show Books")
  print("3.Issue Book")
  print("4.Return Book")
  print("5.Show Detail of book")
  print("6.Exit")
  
  # Use a try-except block to handle non-integer inputs gracefully
  try:
    choice = int(input("Enter your choice: "))
  except ValueError:
    print("\n------ Please enter a valid number -------\n")
    continue

  # Logic for Option 1: Adding a new book in the library
  if choice==1:
    book_id=input("enter the id of book:")
    title=input("enter book title:")
    author=input("enter the author name:")
    lib.add_book(book_id,title,author)
  # Logic for Option 2: Displaying all books in the library
  elif choice==2:
    lib.show_books()
  # Logic for Option 3: Issuing a book in the library
  elif choice==3:
    title = input("Enter the title of the book you want to issue: ")
    author = input("Enter the author of the book you want to issue: ")
    lib.issue_book(title,author)
  # Logic for Option 4: Returning a book in the library
  elif choice==4:
    title = input("Enter the title of the book you want to return: ")
    author = input("Enter the author of the book you want to return: ")
    lib.return_book(title, author)
  # Logic for Option 5: Showing details of a book
  elif choice==5:
    title=input("Enter the title of the book you want to get detail of:")
    lib.get_detail(title)
  # Logic for Option 6: Breaking the loop to close the application
  elif choice==6:
    print("\n------Thank you------\n")
    break
  # Invalid choice handling
  else:
    print("\n------Invalid choice-------\n")
    
