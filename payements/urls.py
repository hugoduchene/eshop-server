from django.urls import path

from .views import ChargeViews, WebHooksViews

urlpatterns = [
    path('charge', ChargeViews.as_view(), name="chargePayements"),
    path('webhooks', WebHooksViews.as_view(), name="webhooks"),
]
