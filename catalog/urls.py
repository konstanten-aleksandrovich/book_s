from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name='index'),
    path('books/',BookListView.as_view(),name='books'),
    path('book-detail/<int:pk>/',BookDitailView.as_view(),name='book-detail'),
    path('authors/',AuthorsListView.as_view(),name='authors'),
    path('author-detail/<int:pk>',AuthorDitailView.as_view(),name='author-detail'),
    path('mybooks/', LoanedВooksByUserListView.as_view(), name='my-borrowed'),
]