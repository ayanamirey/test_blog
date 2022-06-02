from django.urls import path
from .views import post_delete, Postlist, PostCreateView, \
    post_edit, MyProjectLoginView, RegisterUserView, MyProjectLogoutView, PostDetailView

urlpatterns = [
    path('', Postlist.as_view(), name="post_list"),
    path('post/create/', PostCreateView.as_view(), name="post_create"),
    path('post/detail/<int:post_pk>', PostDetailView.as_view(), name="post_detail"),
    path('post/delete/<int:post_pk>', post_delete, name="post_delete"),
    path('post/edit/<int:post_pk>', post_edit, name='post_edit'),
    path('login/', MyProjectLoginView.as_view(), name='login_page'),
    path('register/', RegisterUserView.as_view(), name='register_page'),
    path('logout/', MyProjectLogoutView.as_view(), name='logout_page'),

]
