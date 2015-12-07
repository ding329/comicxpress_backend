from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers
#from comicxpress_backend.api import views
from api import views


from rest_framework.urlpatterns import format_suffix_patterns
from axes.decorators import watch_login

#REST API routes
router = routers.DefaultRouter()
router.register(r'users', views.userViewSet)

#REST API
urlpatterns = [
    url(r'^', include(router.urls)),

url(r'^session/', watch_login(views.Session.as_view())),

    #class-based view approach
 #   url(r'^$', views.api_root), #needed if you use all class-based views and want them to show up in the landing page for the browsable api
 #   url(r'^orders/$', views.catalogList.as_view(), name='catalog-list'),
    url(r'^monthlyorders/$', views.monthlyorderList.as_view(), name='monthlyorder-list'),
    url(r'^monthlyorders/(?P<pk>[0-9]+)/$', views.monthlyorderDetail.as_view(), name ='monthlyorder-detail' ),
    url(r'^catalogs/$', views.catalogList.as_view(), name='catalog-list'),
#    url(r'^catalogs/(?P<pk>[0-9]+)/$', views.catalogDetail.as_view(), name='catalog-detail'),
    url(r'^previewselections/$', views.previewselectionsList.as_view(), name='previewselections-list'),
    url(r'^registration/$', views.Registration.as_view()),
]
