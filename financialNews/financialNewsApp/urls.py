from django.urls import path, include
from rest_framework.routers import DefaultRouter
from financialNewsApp import views

router = DefaultRouter()
router.register(r'news', views.NewsList)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]