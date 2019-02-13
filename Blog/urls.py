from django.urls import path
from . import views

urlpatterns = [
   path('', views.blog, name='blog'),
   path('new-post', views.new_post, name='new-post'),
   path('<int:id_post>', views.post_page, name='post-page'),
]