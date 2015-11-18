from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers
from comicxpress_backend.api import views
from rest_framework.urlpatterns import format_suffix_patterns

#REST API routes
router = routers.DefaultRouter()
#router.register(r'forumposts', views.ForumpostViewSet) #use this for viewset approach
router.register(r'users', views.userViewSet)

#REST API
urlpatterns = [
    url(r'^', include(router.urls)),

    #class-based view approach
 #   url(r'^$', views.api_root), #needed if you use all class-based views and want them to show up in the landing page for the browsable api
 #   url(r'^orders/$', views.catalogList.as_view(), name='catalog-list'),
    url(r'^monthlyorders/$', views.monthlyorderList.as_view(), name='monthlyorder-list'),
    url(r'^catalogs/$', views.catalogList.as_view(), name='catalog-list'),
    url(r'^previewselections/$', views.previewselectionsList.as_view(), name='previewselections-list'),
]
