from django.urls import path
from .views import all_books, book_info, book_published_date, books_sorted_by_year

urlpatterns = [
    path('', all_books),
    path('/<int:pk>/', book_info),
    path('/<str:published_date>', book_published_date),
    path('/<str:sort>', books_sorted_by_year),

    ]