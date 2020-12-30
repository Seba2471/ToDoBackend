from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import TaskViewSet,TaskListViewSet

router = DefaultRouter()
router.register('task', TaskViewSet, basename='task')
router.register('tasklist', TaskListViewSet, basename='tasklist')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('viewset/', include(router.urls)),
]
