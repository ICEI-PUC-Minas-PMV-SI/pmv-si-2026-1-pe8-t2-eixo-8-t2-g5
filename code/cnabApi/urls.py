from django.urls import path, include
# from .views import DocumentationViewSet, DonoViewSet, NameViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
# router.register('doc', DocumentationViewSet, basename='document')


urlpatterns = [
    path('', include(router.urls)),
    # path('doc/', DocumentationViewSet.as_view(), name='index'),
    # path('donos/<int:pk>/', DonoViewSet.as_view(), name='donos'),
    # path('names/<str:name>/', NameViewSet.as_view(), name='names'),
    ]
