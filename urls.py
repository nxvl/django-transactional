from django.conf.urls import patterns, include, url

urlpatterns = patterns('dtrans.utils',
    url(
        r'^(?P<app_name>\w+)/(?P<model_name>\w+)/add/$',
        'add_or_modify',
        name='add'
    ),
    url(
        r'^(?P<app_name>\w+)/(?P<model_name>\w+)/add/(?P<obj_id>\d+)/$',
        'add_or_modify',
        name='modify'
    ),
)
