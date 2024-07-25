from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.account_management, name='account_management'),
    path('cooldown/', views.tools, name='tools'),
]