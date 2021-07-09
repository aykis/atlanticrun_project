from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('', include(('index.urls', 'index'), namespace='index')),
    path('l_envol', include(('envol.urls', 'envol'), namespace='envol')),
    path('nous_decouvrir', include(('decouvrir.urls', 'decouvrir'), namespace='decouvrir')),
    path('a_quoi_sert_le_don', include(('don.urls', 'don'), namespace='don')),
    path('contact', include(('contact.urls', 'contact'), namespace='contact')),
    path('inscription', include(('inscription.urls', 'inscription'), namespace='inscription')),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    prefix_default_language=False,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(r'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns