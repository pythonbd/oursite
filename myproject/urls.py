
from django.contrib import admin
from django.conf.urls import url, include
admin.site.site_title = "Pythonbd Admin"
admin.site.site_header = "Pythonbd Administrator"

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('pythonbd.urls')),
    url(r'^pythonbd/', include('pythonbd.urls'))
]
