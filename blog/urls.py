from django.urls import path
from .views import post_list, post_detail, post_delete, post_edit

urlpatterns = [
    path('', post_list, name="post_list"),
    path('post/detail/<int:post_pk>', post_detail, name="post_detail"),
    path('post/delete/<int:post_pk>', post_delete, name="post_delete"),
    path('post/edit/<int:post_pk>', post_edit, name='post_edit'),

]
