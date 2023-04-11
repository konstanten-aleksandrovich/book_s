from django.db import models
from django.urls import reverse
# Create your models here.
class Ganre(models.Model):
    name=models.CharField(max_length=200,help_text='Введите жанр книги',verbose_name='Жанр книги')
    def __str__(self):
        return self.name
class Language(models.Model):
    lang=models.CharField(max_length=20,help_text='Введите язык книги',verbose_name='Язык книги')
    def __str__(self):
        return self.lang
class Author(models.Model):
    first_name=models.CharField(max_length=100,help_text='Введите имя авторя',verbose_name='Имя автора')
    last_name=models.CharField(max_length=100,help_text='Ведите фамилию автора',verbose_name='Фамилия автора')
    date_of_birth=models.DateField(help_text='Ведите дату рождения',verbose_name='Дата рождения',null=True,blank=True)
    date_of_death=models.DateField(help_text='Ведите дату смерти',verbose_name='Дата смерти',null=True,blank=True)
    def __str__(self):
        return self.last_name
class Books(models.Model):
    title=models.CharField(max_length=200,help_text='Введите название книги',verbose_name='Название книги')
    genre=models.ForeignKey('Ganre',on_delete=models.CASCADE,help_text='Выберите жанр',verbose_name='Жанр книги',null=True)
    language=models.ForeignKey('Language',on_delete=models.CASCADE,help_text='Выберите язык',verbose_name='Язык книги',null=True)
    author=models.ManyToManyField('Author',help_text='Выберите автора',verbose_name='Автор книги')
    summary=models.TextField(max_length=1000,help_text='Ведите краткое описание книги',verbose_name='Анотация книги')
    isbn=models.CharField(max_length=13,help_text='Должно содиржать 13 символов',verbose_name='ISBN книги')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return  reverse('book-detail',args=[str(self.id)])
class Status(models.Model):
    name=models.CharField(max_length=20,help_text='Ведите статус экземпляра книги',verbose_name='Статус экземпляра книги')
    def __str__(self):
        return self.name
class Bookinstance(models.Model):
    book=models.ForeignKey('Books',on_delete=models.CASCADE,null=True)
    inv_nom=models.CharField(max_length=20,help_text='Введите инвентарный номер книги',verbose_name='Инвентарный номер книги',null=True)
    imprint=models.CharField(max_length=200,help_text='Введите издательство и год выпуска',verbose_name='Издательство',null=True)
    status=models.ForeignKey('Status',on_delete=models.CASCADE,null=True,help_text='Измините статус экземпляра книги', verbose_name='Статус экземпляра')
    due_back=models.DateField(null=True,blank=True,help_text='Введите дату конца срока статуса',verbose_name='Дата окончания статуса')
    def __str__(self):
        return f'{self.inv_nom}{self.book}{self.status}'