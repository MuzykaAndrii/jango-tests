from django.urls import path

from .views import index, by_theme, BbCreateView


urlpatterns = [
    path('', index, name='index'),
    path('<int:theme_id>', by_theme, name='by_theme'),
    path('add/', BbCreateView.as_view(), name='add'),
]