from django.urls import path
from .views import PostsList, PostDetail, PostCreate,\
   PostEdit, PostDelete


urlpatterns = [
   path('', PostsList.as_view(), name='posts_list',),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]