"""atlanticrun_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    prefix_default_language=False,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(r'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns