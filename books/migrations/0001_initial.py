from django.db import migrations, models

def create_initial_books(apps, schema_editor):
    Book = apps.get_model('books', 'Book')
    Book.objects.create(title="Django for Beginners", author="William S. Vincent", published_year=2018)
    Book.objects.create(title="Two Scoops of Django", author="Daniel Roy Greenfeld", published_year=2020)
    Book.objects.create(title="Python Crash Course", author="Eric Matthes", published_year=2019)
    Book.objects.create(title="Automate the Boring Stuff with Python", author="Al Sweigart", published_year=2015)
    Book.objects.create(title="Fluent Python", author="Luciano Ramalho", published_year=2015)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # No self-dependency here!
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('published_year', models.IntegerField()),
            ],
        ),
        migrations.RunPython(create_initial_books),
    ]