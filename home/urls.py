from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("",views.index),
    path("category/<str:string>",views.category,name="category"),
    path("signout",views.signout,name="signout"),
    path("signin",views.signin,name="signin"),
    path("signup",views.signup,name="signup"),
    path("about",views.about,name="about"),
    path("feedback",views.feedback,name="feedback"),
    path("help",views.help,name="help"),
    path("submitfeedback",views.submitfeedback,name="submitfeedback"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
