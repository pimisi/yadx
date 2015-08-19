from django.conf.urls import patterns, url
from apps.responsive_web import views

urlpatterns = patterns(
    '',
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^/blogs$', views.HomePageView.as_view(), name='home'),
)
