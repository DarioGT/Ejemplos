from Books.models import Publisher, Author, Book 
from django.contrib import admin

class Book_Admin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publisher', 'publication_date')
#    list_filter = ('publisher',)
    ordering = ('-publication_date',)
    search_fields = ('title',)

# ...
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book, Book_Admin)
