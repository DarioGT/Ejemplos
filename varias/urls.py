from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^/varias/time/$', current_datetime),
    (r'^/time/$', current_datetime),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),

)
