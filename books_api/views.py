from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import requests

def get_book_data():
    url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
    book_request = requests.get(url)
    return json.loads(book_request.text)

# Create your views here.
@api_view(['GET'])
def all_books(request):
    if request.method == 'GET':
        data = get_book_data()
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response(data , status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def book_info(request, pk):
    return Response(serielizer.errors, status=status.HTTP_400_BAD_REQUEST)
    pass


@api_view(['GET'])
def book_published_date(request, year):
    if request.method == 'GET':
        print(year)
        raw_data = get_book_data()
        for obj in raw_data:
            print(obj)
    return Response(serielizer.errors, status=status.HTTP_400_BAD_REQUEST)
    pass


@api_view(['GET'])
def books_sorted_by_year():
    return Response(serielizer.errors, status=status.HTTP_400_BAD_REQUEST)
    pass