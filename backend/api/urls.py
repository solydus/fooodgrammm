from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views
from users import urls as users_urls

app_name = 'api'

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet, basename='recipes')
router.register(
    r'recipes/(?P<recipe_id>\d+)/FavoriteAdmin',
    views.FavoriteViewSet, basename='favorite')
router.register(
    'users/subscriptions',
    views.SubscriptionsViewSet, basename='subscriptions')
router.register('tags', views.TagViewSet, basename='tags')
router.register('ingredients', views.IngredientViewSet, basename='ingredients')
router.register(
    r'recipes/(?P<recipe_id>\d+)/shopping_cart',
    views.ShoppingCartViewSet, basename='shopping_cart')

urlpatterns = [
    path(
        'recipes/download_shopping_cart/',
        views.DownloadShoppingCart.as_view()),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    path('users/', include(users_urls))]