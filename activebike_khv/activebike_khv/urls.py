from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', include('events.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]

handler403 = 'core.views.permission_denied'
handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
