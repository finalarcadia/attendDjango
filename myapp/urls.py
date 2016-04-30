from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'classes', views.ClassViewSet)
router.register(r'universities', views.UniversityViewSet)
router.register(r'userdetails', views.UserDetailViewSet)
router.register(r'roster', views.ClassRosterViewSet)
router.register(r'requests', views.ClassRequestViewSet)
router.register(r'attendance', views.AttendanceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/(?P<usr>[a-z0-9]+)/(?P<pw>[a-z0-9]+)/$', views.AuthView.as_view()),
    url(r'^usersfromuniversity/(?P<pk>[0-9]+)/$', views.UserUniversityView.as_view()),
    url(r'^usersfromclass/(?P<pk>[0-9]+)/$', views.UserClassListView.as_view()),
    url(r'^classesfromuser/(?P<pk>[0-9]+)/$', views.ClassUserListView.as_view()),
    url(r'^requestsfromuser/(?P<pk>[0-9]+)/$', views.RequestUserListView.as_view()),
    url(r'^requestsfromuniversity/(?P<pk>[0-9]+)/$', views.RequestUniversityListView.as_view()),
    url(r'^record/(?P<pk>[0-9]+)/(?P<classpk>[0-9]+)/$', views.RecordView.as_view())
]