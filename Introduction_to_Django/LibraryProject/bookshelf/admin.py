from django.contrib import admin
from .models import Book

# Register the Book model with the admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show in the list view
    search_fields = ('title', 'author')  # Add search functionality
    list_filter = ('publication_year',)  # Add filter by publication year
