1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`.

Here there is two app accounts and librarymgt

accounts app consist models and views related to user like user creation, user view and finding user
librarymgt app consist models and views related to books like adding book, view all books, bowwowing books, book details and returnig of book.

for the api view i have used the generic view as it is use to use and modify accordingly.

and here are api endpoints
For creating a user
endpoint: http://127.0.0.1:8000/user/register/
method POST
json
'''
{
    "name": "name",
    "email": "email@gmail.com",
    "membership_date": date
}
'''
For Viewing all users
endpoint: http://127.0.0.1:8000/user/viewusers/
method GET

For searching user by user id
endpoint: http://127.0.0.1:8000/user/finduser/1
method GET

For Viewing all books
endpoint: http://127.0.0.1:8000/books/allbooks/
method GET

For Adding new book
endpoint: http://127.0.0.1:8000/books/addbook/
method POST
json
{
    "title": "title",
    "isbn": "isbn number",
    "published_date": date,
    "genre": "genre"
}

For searching book by book id
endpoint: http://127.0.0.1:8000/books/findbook/1
method GET

For Adding book details
endpoint: http://127.0.0.1:8000/books/addbookdetails/
method POST
json
{
    "number_of_pages": pagenumber,
    "publisher": "publisher name",
    "language": "language",
    "book_id": book_id
}

For viewing and updating book details using id
endpoint: http://127.0.0.1:8000/books/viewbookdetails/1/
method GET,PUT

For borrowing book
endpoint: http://127.0.0.1:8000/books/borrowingbook/
method POST
json
{
    "borrow_date": borrowed date,
    "return_date": null,
    "user_id": userid,
    "book_id": bookid
}

For viewing borrowed books
endpoint: http://127.0.0.1:8000/books/borrowedbooks/
method GET

For returnig book using id
endpoint: http://127.0.0.1:8000/books/returningbook/1/
method GET,PUT
{
    "borrow_date": borrowed_date,
    "return_date": returndate,
    "user_id": userid,
    "book_id": bookid
}
