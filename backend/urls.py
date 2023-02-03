from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

#VIAGGI FATTI
router.register("api/viaggi-fatti/titolo", views.RicercaTitoloVF, basename="ricerca-titolovf")
router.register("api/viaggi-fatti/data", views.RicercaDataVF, basename="ricerca-datavf")
router.register("api/viaggi-fatti/luogo", views.RicercaLuogoVF, basename="ricerca-luogovf")
router.register("api/viaggi-fatti", views.ViaggiFattiViewSet, basename="viaggi-fatti")
#VIAGGI DA FARE
router.register("api/viaggi-da-fare/titolo", views.RicercaTitoloVdF, basename="ricerca-titolovdf")
router.register("api/viaggi-da-fare/data", views.RicercaDataVdF, basename="ricerca-datavdf")
router.register("api/viaggi-da-fare/luogo", views.RicercaLuogoVdF, basename="ricerca-luogovdf")
router.register("api/viaggi-da-fare", views.ViaggiDaFareViewSet, basename="viaggi-da-fare")

urlpatterns = router.urls