from rest_framework import generics,status
from .models import Book, BookDetails, BorrowedBooks
from .serializers import BookSerializer, BookDetailsSerializer,BorrowedBooksSerializer
from django.db import IntegrityError
from rest_framework.response import Response
from django.http import Http404


class AddBookView(generics.CreateAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response({'error': 'Integrity Error: ISBN must be unique.'}, status=status.HTTP_400_BAD_REQUEST)
        


class ListBooksView(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class GetBookByIdView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Http404:
            return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)

class AddBookDetailsView(generics.CreateAPIView):
    queryset = BookDetails.objects.all()
    serializer_class = BookDetailsSerializer


class BookDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookDetails.objects.all()
    serializer_class = BookDetailsSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Http404:
            return Response({'error': 'Book Details not found.'}, status=status.HTTP_404_NOT_FOUND)



class BorrwingBooksView(generics.CreateAPIView):
    queryset=BorrowedBooks.objects.all()
    serializer_class= BorrowedBooksSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')  
        book_id = request.data.get('book_id')  

        # Check if the user has already borrowed the same book
        existing_borrowed_book = BorrowedBooks.objects.filter(user_id=user_id, book_id=book_id, return_date__isnull=True).first()
        if existing_borrowed_book:
            return Response({'error': 'User cannot borrow the same book multiple times.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response({'error': 'Integrity Error: Unable to create borrowed book.'}, status=status.HTTP_400_BAD_REQUEST)

class ListBorrwedBooksView(generics.ListAPIView):
    queryset=BorrowedBooks.objects.all()
    serializer_class= BorrowedBooksSerializer

class BorrowedBooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=BorrowedBooks.objects.all()
    serializer_class= BorrowedBooksSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Http404:
            return Response({'error': 'Book Details not found.'}, status=status.HTTP_404_NOT_FOUND)

