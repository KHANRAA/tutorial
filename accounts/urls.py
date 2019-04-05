from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    url(r'^$',views.home),
    url(r'^login/$',LoginView.as_view(template_name='accounts/login.html'),name="login"),
    url(r'^logout/$', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    url(r'^register/$',views.register,name='register'),
    url(r'^profile/$', views.view_profile,name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile')

]