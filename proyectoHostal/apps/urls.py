from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

#Para importar el login_required y aplicarlo en el Crud
from django.contrib.auth.decorators import login_required

#Para importar las funciones que estan en views.py
from .views import pagina_principal

#Para la apis
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import ProductViewSet, ProductViewSetDetail

urlpatterns = [
    url(r'^$', pagina_principal, name='pagina_principal'),
]