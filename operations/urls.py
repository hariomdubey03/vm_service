from django.urls import path
from .views import (
    VendorAPIView,
    PurchaseOrderAPIView,
)

urlpatterns = [
    # Vendor API Endpoints
    path("vendors/", VendorAPIView.as_view(), name="vendor-list"),
    path(
        "vendors/<str:vendor_id>/",
        VendorAPIView.as_view(),
        name="vendor-detail",
    ),
    path(
        "vendors/<int:vendor_id>/performance/",
        VendorAPIView.as_view(),
        name="vendor-performance",
    ),
    path(
        "vendors/<int:vendor_id>/",
        VendorAPIView.as_view(),
        name="vendor-update",
    ),
    path(
        "vendors/<int:vendor_id>/",
        VendorAPIView.as_view(),
        name="vendor-delete",
    ),
    # Purchase Order API Endpoints
    path(
        "purchase_orders/",
        PurchaseOrderAPIView.as_view(),
        name="purchase-order-list",
    ),
    path(
        "purchase_orders/<int:po_id>/",
        PurchaseOrderAPIView.as_view(),
        name="purchase-order-detail",
    ),
    path(
        "purchase_orders/<int:po_id>/",
        PurchaseOrderAPIView.as_view(),
        name="purchase-order-update",
    ),
    path(
        "purchase_orders/<int:po_id>/",
        PurchaseOrderAPIView.as_view(),
        name="purchase-order-delete",
    ),
    path(
        "purchase_orders/<int:po_id>/acknowledge/",
        PurchaseOrderAPIView.as_view(),
        name="acknowledge-purchase-order",
    ),
]
