# Generated by Django 4.2 on 2023-04-11 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите имя авторя', max_length=100, verbose_name='Имя автора')),
                ('last_name', models.CharField(help_text='Ведите фамилию автора', max_length=100, verbose_name='Фамилия автора')),
                ('date_of_birth', models.DateField(blank=True, help_text='Ведите дату рождения', null=True, verbose_name='Дата рождения')),
                ('date_of_death', models.DateField(blank=True, help_text='Ведите дату смерти', null=True, verbose_name='Дата смерти')),
            ],
        ),
        migrations.CreateModel(
            name='Ganre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите жанр книги', max_length=200, verbose_name='Жанр книги')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(help_text='Введите язык книги', max_length=20, verbose_name='Язык книги')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ведите статус экземпляра книги', max_length=20, verbose_name='Статус экземпляра книги')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название книги', max_length=200, verbose_name='Название книги')),
                ('summary', models.TextField(help_text='Ведите краткое описание книги', max_length=1000, verbose_name='Анотация книги')),
                ('isbn', models.CharField(help_text='Должно содиржать 13 символов', max_length=13, verbose_name='ISBN книги')),
                ('author', models.ManyToManyField(help_text='Выберите автора', to='catalog.author', verbose_name='Автор книги')),
                ('genre', models.ForeignKey(help_text='Выберите жанр', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.ganre', verbose_name='Жанр книги')),
                ('language', models.ForeignKey(help_text='Выберите язык', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.language', verbose_name='Язык книги')),
            ],
        ),
        migrations.CreateModel(
            name='Bookinstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_nom', models.CharField(help_text='Введите инвентарный номер книги', max_length=20, null=True, verbose_name='Инвентарный номер книги')),
                ('imprint', models.CharField(help_text='Введите издательство и год выпуска', max_length=200, null=True, verbose_name='Издательство')),
                ('due_back', models.DateField(blank=True, help_text='Введите дату конца срока статуса', null=True, verbose_name='Дата окончания статуса')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.books')),
                ('status', models.ForeignKey(help_text='Измините статус экземпляра книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.status', verbose_name='Статус экземпляра')),
            ],
        ),
    ]
