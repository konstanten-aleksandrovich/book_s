from django.contrib import admin
from .models import *
class Booksinstanceinline(admin.TabularInline):
    model = Bookinstance
# Register your models here.
#admin.site.register(Books)
@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre','author')
    inlines = [Booksinstanceinline]
admin.site.register(Ganre)
#admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name',('date_of_birth', 'date_of_death')]
admin.site.register(Author,AuthorAdmin)
admin.site.register(Language)
admin.site.register(Status)
#admin.site.register(Bookinstance)
@admin.register(Bookinstance)
class BookinstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','borrower','due_back','id')
    list_filter = ('book','status')
    fieldsets = (
        ('Экземпляр книги',{'fields' : ( 'book', 'imprint', 'inv_nom')}),
        ('Статус и окончание его действия', {'fields': ('status', 'due_back','borrower')}))

