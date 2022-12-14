from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, Subscribe
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(PostList.as_view()), name='posts'),
    path('<int:pk>', cache_page(60*5)(PostDetail.as_view()), name='post_detail'),
    path('create/', PostCreate.as_view(), name='create_news'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='product_delete'),
    path('subscribe/', Subscribe.as_view(), name='subscribe'),

]
