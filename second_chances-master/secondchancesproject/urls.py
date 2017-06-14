"""secondchancesproject URL Configuration

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
from secondchances import views
from rest_framework import routers
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
# router.register(r'user_profile/(?P<user_id>[0-9]+)', views.User_ProfileViewSet)
router.register(r'user_profile', views.User_ProfileViewSet)
router.register(r'user', views.UserViewSet)
# router.register(r'job/(?P<user_id>[0-9]+)', views.JobViewSet)

router.register(r'jobmatch/(?P<user_id>[0-9]+)', views.JobMatchViewSet, 'jobmatch')
router.register(r'jobmatch', views.JobMatchViewSet, 'jobmatch')
router.register(r'job', views.JobViewSet, 'job')
router.register(r'ownedjob/(?P<user_id>[0-9]+)', views.OwnedJobViewSet, 'ownedjob')
router.register(r'location', views.LocationViewSet)
router.register(r'userlocation/user/(?P<user_id>[0-9]+)', views.User_LocationViewSet)
router.register(r'userlocation', views.User_LocationBaseViewSet)
router.register(r'skills', views.SkillsViewSet)
router.register(r'providedskill/user/(?P<user_id>[0-9]+)', views.Provided_SkillViewSet)
router.register(r'providedskill', views.Provided_SkillBaseViewSet)
router.register(r'requiredskill/job/(?P<job_id>[0-9]+)', views.Required_SkillViewSet)
router.register(r'requiredskill', views.Required_SkillBaseViewSet)
router.register(r'userneeds/user/(?P<user_id>[0-9]+)', views.User_NeedsViewSet)
router.register(r'userneeds', views.User_NeedsBaseViewSet)
router.register(r'providedneeds/(?P<service_id>[0-9]+)', views.Provided_NeedsViewSet)
router.register(r'providedneeds', views.Provided_NeedsViewSet)
router.register(r'needs', views.NeedsViewSet)
router.register(r'service/(?P<user_id>[0-9]+)', views.ServiceViewSet)
router.register(r'service', views.ServiceViewSet)
router.register(r'connection', views.ConnectionViewSet)
router.register(r'conversation', views.ConversationViewSet)
router.register(r'message', views.MessageViewSet)


urlpatterns = [
    url(r'^secondchances/$', views.login),
    url(r'^$', views.index, name='index'),
    url(r'api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^secondchances/profile/(?P<user_id>[0-9]+)', views.profile, name='profile'),
    # url(r'^secondchances/postings', views.postings),
    # url(r'^secondchances/postings/(?P<user_id>[0-9]+)/search', views.posting_search),
    # url(r'^secondchances/postings/(?P<posting_id>[0-9]+)', views.posting_detail),
    url(r'^secondchances/messages/(?P<user_id>[0-9]+)', views.messages, name='messages'),
    url(r'^secondchances/conversation/(?P<sender_id>[0-9]+)/(?P<recipient_id>[0-9]+)', views.conversation, name='conversation'),
    # url(r'^secondchances/messages/(?P<conversation_id>[0-9]+)', views.message_detail),
    url(r'^secondchances/myskills/(?P<user_id>[0-9]+)', views.myskills),
    url(r'^admin/', admin.site.urls),
]
