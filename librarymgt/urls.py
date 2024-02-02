from django.urls import path
from .views import *

urlpatterns = [
    path('allbooks/', ListBooksView.as_view(),name='allbooks'),
    path('addbook/', AddBookView.as_view(),name='addbook'),
    path('findbook/<int:pk>/', GetBookByIdView.as_view(),name='findbooks'),
    path('addbookdetails/', AddBookDetailsView.as_view(),name='addbookdetails'),
    path('viewbookdetails/<int:pk>/', BookDetailsView.as_view(),name='viewbookdetails'),
    path('borrowingbook/', BorrwingBooksView.as_view(),name='borrowingbook'),
    path('borrowedbooks/', ListBorrwedBooksView.as_view(),name='borrowedbooks'),
    path('returningbook/<int:pk>/', BorrowedBooksDetailView.as_view(),name='returningbook'),
]
