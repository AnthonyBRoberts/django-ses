from django.conf.urls import patterns, url

urlpatterns = patterns('django_ses.views',
    url(r'^$', 'dashboard', name='django_ses_stats'),
)
