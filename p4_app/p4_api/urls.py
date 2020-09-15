from django.conf.urls import url
from rest_framework import routers
from p4_app.p4_api.views import CategoryViewSet, CategoryGames, SingleCategoryGame, GameViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('games', GameViewSet, basename='games')

custom_urlpatterns = [
   url(r'categories/(?P<category_pk>\d+)/games$', CategoryGames.as_view(), name='category_games'),
   url(r'categories/(?P<category_pk>\d+)/games/(?P<pk>\d+)$', SingleCategoryGame.as_view(),
       name='single_category_game'),
   ]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns