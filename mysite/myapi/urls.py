from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url
from django.contrib import admin


router = routers.DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^create/', views.create_post, name='createpost'),
    url(r'^(?P<id>\d+)/$', views.detail_post_view, name='detail'),
    url(r'^(?P<postid>\d+)/preference/(?P<userpreference>\d+)/$', views.post_preference, name='postpreference'),
]
