from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('add-post/', views.add_post, name='add_post'),
    path('delete-post/<int:post_id>', views.delete_post, name='delete_post'),
    path('edit-post/<int:post_id>', views.edit_post, name='edit_post'),
    path('add-reply/<int:comment_id>', views.add_reply, name='add_reply'),
]
 