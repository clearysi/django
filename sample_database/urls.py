from django.conf.urls import *
from django.contrib import admin
import settings
from django.conf.urls.static import static
from ajax_select import urls as ajax_select_urls
from table.views import *

admin.autodiscover()

urlpatterns = [
    url(r'^$', include('table.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^home/','table.views.home'),
    url(r'^first_check/','table.views.first_check'),
    url(r'^second_check/','table.views.second_check'),
    url(r'^ajax_select/',include(ajax_select_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/','table.views.login_user'),
    url(r'^input/','table.views.input'),
    url(r'^list/','table.views.list'),
    url(r'^logout/','table.views.logout_view'),
    url(r'^results/','table.views.index_sample'),
    url(r'^modify/','table.views.modify_sample'),
    url(r'^contact/','table.views.contact'),
    url(r'^request_list/','table.views.request_list'),
    url(r'^display/','table.views.display'),
#    url(r'^product_list/', 'table.views.product_list'),
    url(r'^selectable/', include('selectable.urls')),
    url(r'session_security/', include('session_security.urls')),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('', url(r'^files/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT, 'show_indexes':True}),)

