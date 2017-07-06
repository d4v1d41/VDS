from django.conf.urls import url

from . import views
app_name= 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^menu/(?P<info_id>[0-9]+)/$', views.infol, name='infol'),
    url(r'^(?P<post_id>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<comment_id>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<comment_id>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]