from django.urls import path

from content.views import category_list

app_name = 'content'
urlpatterns = [
    path('categories/', category_list, name='category-list'),

]