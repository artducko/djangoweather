from django.urls import path
# the "." means from current directory. in this case it's the "lookup" directory
from . import views

urlpatterns = [
    # '' is the homepage
    path('', views.home, name="home"),
    # always include the ".html" - not sure about this because it worked without it but was used in video
    # turns out you don't its preference
    path('about.html', views.about, name="about"),

]