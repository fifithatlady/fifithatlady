"""
URL configuration for Fifi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from accounts.api import UserViewSet
from babies.api import BabyViewSet
from forum import api as forum_api
from marketplace.api import CategoryViewSet, ItemViewSet
from milestones.api import MilestoneViewSet, LoggedMilestoneViewSet, ActivityViewSet, NutritionGuideViewSet, ProgressViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'babies', BabyViewSet)
router.register(r'forum/categories', forum_api.CategoryViewSet)
router.register(r'forum/threads', forum_api.ThreadViewSet)
router.register(r'forum/posts', forum_api.PostViewSet)
router.register(r'forum/comments', forum_api.CommentViewSet)
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'items', ItemViewSet, basename='item')
router.register(r'milestones', MilestoneViewSet)
router.register(r'logged_milestones', LoggedMilestoneViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'nutrition_guides', NutritionGuideViewSet)
router.register(r'progresses', ProgressViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('accounts/', include('accounts.urls')),
    path('babies/', include('babies.urls')),
    path('milestones/', include('milestones.urls')),# Keep your existing URLs
    path('forum/', include('forum.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('chatbot/', include('chatbot.urls')),
    # ...other urls
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
