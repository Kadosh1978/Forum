from django.urls import path
# from main.views import CategoryListView
from .views import PostList
# , PostDetail, PostDelete, find, PostSearch, PostCreate, PostUpdate

urlpatterns = [

   path('', (PostList.as_view()), name='posts'),

]