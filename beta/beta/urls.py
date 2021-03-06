from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from rest_framework_nested import routers as nested_routers
from yata import views

handler500 = 'yata.views.error_500'

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'timesheets', views.TimesheetViewSet, base_name='timesheet')

nested_router = nested_routers.NestedSimpleRouter(router, r'timesheets', lookup='timesheet')
nested_router.register(r'hours', views.HourViewSet, base_name='hour')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(nested_router.urls)),
    url(r'^api/me/$', views.me_view),
    url(r'^api/token/', views.token_view),
    url(r'^', include('rest_framework_swagger.urls')),
]
