from django.urls import path
from .views import BlogList, BlogDetail, AddBlog, EditBlog, DeleteBlog

urlpatterns = [
    path('', BlogList.as_view(), name='bloglist'),
    path('detail/<int:pk>', BlogDetail.as_view(), name='blog_detail'),
    path('add_blog/', AddBlog.as_view(), name='add_blog'),
    path('edit_blog/<int:pk>', EditBlog.as_view(), name='edit_blog'),
    path('delete_blog/<int:pk>', DeleteBlog.as_view(), name='delete_blog')
]