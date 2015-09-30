from django.conf.urls import include, url
from django.contrib import admin
from student_database import urls
urlpatterns = [
    # Examples:
    # url(r'^$', 'restapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^student_database/',include('student_database.urls'))

]
