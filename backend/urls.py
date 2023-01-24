from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("api/viaggi-fatti", views.ViaggiFattiViewSet, basename="viaggi-fatti")
router.register("api/viaggi-da-fare", views.ViaggiDaFareViewSet, basename="viaggi-da-fare")

urlpatterns = router.urls