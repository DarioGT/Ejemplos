from django.forms import ModelForm, Textarea
from Books.models import Book


class ArticleForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'publisher')
        widgets = {
            'notes': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
