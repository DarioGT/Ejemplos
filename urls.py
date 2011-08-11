# This also imports the include function
from django.conf.urls.defaults import *

#from views import current_datetime, hours_ahead

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#    (r'^polls/', include('polls.urls')),
    (r'^books/', include('Books.urls')),
    (r'^contact/', 'contact.views.contact'),

#   (r'^varias/', include('varias/urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)


