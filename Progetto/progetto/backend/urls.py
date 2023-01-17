from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("api/viaggi", views.ViaggiViewSet, basename="viaggi")

urlpatterns = router.urls