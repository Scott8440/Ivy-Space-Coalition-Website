from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<slug:post_slug>/', views.detail, name='detail'),
    path('category/<slug:category_slug>/', views.category, name='category'),
]

