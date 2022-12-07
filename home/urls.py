from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Prayag's Admin"
admin.site.index_title = "Welcome to Prayagwebscale"
admin.site.site_title = "Prayag's-Webscale"

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("bill", views.bill, name='bill'),
    path("contact", views.contact, name='contact'),

]
