"""Courses URLs"""
# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from dkecole.courses import views as courses_views

router=DefaultRouter()
router.register(r'classes',courses_views.CourseViewSet,basename='classes')
urlpatterns = [path('',include(router.urls))]

