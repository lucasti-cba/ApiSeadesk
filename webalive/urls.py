from django.contrib import admin
from django.urls import include, path
from webalive import settings
from django.conf.urls.static import static
from landing.api import *
from landing.views import *
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
import landing.urls as landingUrls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic.base import RedirectView
import admin.urls as adminUrls
from rest_framework.urlpatterns import format_suffix_patterns

# api_router = routers.DefaultRouter()
# api_router.register(r"loja", LojaDetail)
# api_router.register(r"endereco", EnderecoDetail)


api_router = routers.DefaultRouter()
api_router.register(r"seadesk_imagem", EnvioImagemDetail)
api_router.register(r"seadesk_relatorio", EnvioRelatorioDetail)
api_router.register(r"find_caixa", FindCaixaViewSet)
api_router.register(r"envio_logs", LogsDetail)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(landingUrls)),   
    path("api/", include(api_router.urls)),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/auth/', include('djoser.urls.authtoken')),
  
   
]


