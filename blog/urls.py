from django.urls import path
from .views import post_delete, post_edit, Postlist, PostCreateView, post_detail

urlpatterns = [
    path('', Postlist.as_view(), name="post_list"),
    # path('', post_list, name="post_list"),
    path('post/create/', PostCreateView.as_view(), name="post_create"),
    path('post/detail/<int:post_pk>', post_detail, name="post_detail"),
    path('post/delete/<int:post_pk>', post_delete, name="post_delete"),
    path('post/edit/<int:post_pk>', post_edit, name='post_edit'),

]
