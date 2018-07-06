from api.views import PlayerGoalScoreViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'goals', PlayerGoalScoreViewSet)

urlpatterns = router.urls
