from django.conf.urls import url

from . import views

app_name = 'polls'
base_app_id_regex = r'^(?P<pk>[0-9]+)'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(base_app_id_regex + r'/$', views.DetailView.as_view(), name='detail'),
    url(base_app_id_regex + r'/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
