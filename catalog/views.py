from django.contrib.messages.storage import session
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    num_books=Books.objects.all().count()
    num_Instanse=Bookinstance.objects.all().count()
    num_instances_available = Bookinstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()
    num_visits=request.session.get('num_visits',0)
    request.session['num_visits']=num_visits+1

    return render(request, 'index.html',
                  context={'num_books': num_books,
                           'num_Instanse': num_Instanse,
                           'num_instances_available': num_instances_available,
                           'num_authors': num_authors,
                           'num_visits':num_visits})
class BookListView(generic.ListView):
    model = Books
    paginate_by = 3
class BookDitailView(generic.DetailView):
    model = Books
class AuthorsListView(generic.ListView):
    model = Author
    paginate_by = 4
class AuthorDitailView(generic.DetailView):
    model = Author

class LoanedВooksByUserListView(LoginRequiredMixin,generic.ListView):
    '''Универсальный класс представления списка книг,
    находящихся в заказе у текущего пользователя.'''

    model = Bookinstance
    template_name ='catalog/bookinstance_list_borrowed user.html'
    paginate_by = 10
    def get_queryset(self):
        return Bookinstance.objects.filter(borrower=self.request.user).filter(status__pk='2').order_by('due_back')



