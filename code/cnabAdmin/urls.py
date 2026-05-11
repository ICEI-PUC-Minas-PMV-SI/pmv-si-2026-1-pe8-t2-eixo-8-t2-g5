import debug_toolbar
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
                  # path('grappelli/', include('grappelli.urls')),
                  path('admin/', admin.site.urls),
                  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('', include('cnab.urls.homeurls')),
                  path('upload/', include('cnab.urls.uploadurls')),
                  path('list/', include('cnab.urls.listcontenturls')),
                  path('type/', include('cnab.urls.typeurls')),
                  path('provider/', include('cnab.urls.providerurls')),
                  path('maker/', include('cnab.urls.makerurls')),
                  path('warehouse/', include('cnab.urls.warehouseurls')),
                  path('sales/', include('cnab.urls.salesurls')),
                  path('transfer/', include('cnab.urls.transfersurls')),
                  path('contact/', include('cnab.urls.contacturls')),
                  path('finish/', include('cnab.urls.finishurls')),
                  path('signup/', include('cnab.urls.sigupurls')),
                  path('product/', include('cnab.urls.producturls')),
                  # path('accounts/', include('allauth.urls')),
                  path('login/', include('cnab.urls.loginurls')),
                  path('logout/', include('cnab.urls.logouturls')),
                  # path('login/', include('django.contrib.auth.urls')),
                  path('api/', include('cnabApi.urls')),
                  path('__debug__/', include(debug_toolbar.urls)),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'SOS dos Farois'
admin.site.site_title = 'SOS dos Farois'
admin.site.index_title = 'Administração'

# FIXME: ajuste de login e logout
