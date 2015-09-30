from django.conf.urls import patterns, url

from views.views import MarksView,studentView


urlpatterns = patterns(
    '',
    # REST

    url(r'^marks-view/(?P<registration_no>\d+)/$', MarksView.as_view()),
    url(r'^marks-view/?$', MarksView.as_view()),
    #url(r'^students/(?P<name>\w*)?$', studentView.as_view()),
    #url(r'^guide/(?P<guide_id>[0-9]+)/step/(?P<step_id>[0-9]+)?$', GuideStepRest.as_view()),
)