from django.urls import path
# from main.views import CategoryListView
from .views import PostList, PostCreate, PostDetail, ConfirmUser
# , PostDetail, PostDelete, find, PostSearch, PostCreate, PostUpdate

urlpatterns = [

   path('', (PostList.as_view()), name='post_list'),
   path('main/create/', PostCreate.as_view(), name='post_create'),
   path('main/<int:pk>/new/', PostDetail.as_view(), name='post_detail'),
   path('main/posts/', ConfirmUser.as_view(), name='confirm_user'),
   path('main/<int:pk>/comment/', PostCreate.as_view(), name='post_comment'),

   

]

