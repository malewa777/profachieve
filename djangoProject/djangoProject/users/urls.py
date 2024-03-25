from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='blog-home'),
	path('create/', views.create, name='create'),
	path('test/', views.achieve, name='test'),
	path('test/<int:pk>', views.ArticlesUpdateView.as_view(), name='articles-update'),
	path('test/<int:pk>', views.ArticlesView.as_view(), name='articles-detail')
]