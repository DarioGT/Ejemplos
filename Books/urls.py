from django.conf.urls.defaults import *
from django.views.generic.base import *
from django.views.generic import list_detail
from Books import views

from Books.models import Publisher, Book
publisher_info = {
    'queryset': Publisher.objects.all(),
    'template_name': 'publisher_list_page.html',
    'extra_context': {'book_list': Book.objects.all()}
}

book_info = {
    'queryset': Book.objects.order_by('-publication_date'),
}

urlpatterns = patterns('',
    (r'^search-form/$', 'Books.views.search_form'),
    (r'^search/$', 'Books.views.search'),
    (r'^about/$', TemplateView.as_view(template_name='about.html')),
    (r'^publishers/$', list_detail.object_list, publisher_info), 
    (r'^books/$', list_detail.object_list, book_info),
)

