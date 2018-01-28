"""ownphotos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from api import views

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

router = routers.DefaultRouter()

router.register(r'api/albums/auto/list', views.AlbumAutoListViewSet)
router.register(r'api/albums/date/list', views.AlbumDateListViewSet)
router.register(r'api/albums/person/list', views.AlbumPersonListViewSet)

router.register(r'api/albums/auto', views.AlbumAutoViewSet)
router.register(r'api/albums/person', views.AlbumPersonViewSet)
router.register(r'api/albums/date', views.AlbumDateViewSet)
router.register(r'api/persons', views.PersonViewSet)
router.register(r'api/photos', views.PhotoViewSet)
router.register(r'api/faces/inferred',views.FaceInferredViewSet)
router.register(r'api/faces/labeled',views.FaceLabeledViewSet)
router.register(r'api/faces', views.FaceViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api/facetolabel', views.FaceToLabelView.as_view()),
    url(r'^api/trainfaces', views.TrainFaceView.as_view()),
    url(r'^api/clusterfaces', views.ClusterFaceView.as_view()),
    url(r'^api/socialgraph', views.SocialGraphView.as_view()),
    url(r'^api/scanphotos', views.ScanPhotosView.as_view()),
    url(r'^api/fetch-external-people', views.FetchExternalPeopleView.as_view()),
    url(r'^api/autoalbumgen', views.AutoAlbumGenerateView.as_view()),

    url(r'^api/stats', views.StatsView.as_view()),
    url(r'^api/locclust', views.LocationClustersView.as_view()),
    url(r'^api/photocountrycounts', views.PhotoCountryCountsView.as_view()),
    url(r'^api/photomonthcounts', views.PhotoMonthCountsView.as_view()),
    url(r'^api/wordcloud', views.SearchTermWordCloudView.as_view()),

    url(r'^api/watcher/photo', views.IsPhotosBeingAddedView.as_view()),
    url(r'^api/watcher/autoalbum', views.IsAutoAlbumsBeingProcessed.as_view()),
    url(r'^api/token-auth/', obtain_jwt_token),
    url(r'^api/token-refresh/', refresh_jwt_token),
    url(r'^api/token-verify/', verify_jwt_token),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
