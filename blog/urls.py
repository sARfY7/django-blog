from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('drafts/<int:id>/publish', views.post_draft_publish, name='post_draft_publish'),
    path('post/<int:id>', views.post_detail, name="post_detail"),
    path('post/new', views.post_new, name="post_new"),
    path('post/<int:id>/edit', views.post_edit, name="post_edit"),
    path('post/<int:id>/delete', views.post_delete, name="post_delete"),
    path('tag/<tag_name>/post', views.tag_post_list, name="tag_post_list")
]
