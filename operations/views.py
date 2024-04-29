import logging
from datetime import datetime, timezone
from django.db.models import F, Avg, ExpressionWrapper
from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.db.models.fields import DurationField
from cerberus import Validator

from operations.models import (
    Vendor,
    PurchaseOrder,
    HistoricalPerformance,
)
from vm_service.utils import custom_exceptions as ce
from operations.serializers import (
    orm_result_list_to_dict,
    orm_result_row_to_dict,
)
from operations import schemas

logger = logging.getLogger("operations")
c_validator = Validator()


class VendorAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, vendor_id=None):
        try:
            if vendor_id is not None:
                vendor = Vendor.objects.get(
                    pk=vendor_id, deleted_on__isnull=True
                )
                if "performance" in request.path:
                    performance_metric = (
                        HistoricalPerformance.objects.get(
                            vendor=vendor, deleted_on__isnull=True
                        )
                    )

                    data = orm_result_row_to_dict(
                        performance_metric,
                        [
                            "vendor_id",
                            "on_time_delivery_rate",
                            "quality_rating_avg",
                            "average_response_time",
                            "fulfillment_rate",
                        ],
                    )
                    return Response(
                        {
                            "message": "Performance metric data found",
                            "data": data,
                        },
                        status=status.HTTP_200_OK,
                    )
                data = orm_result_row_to_dict(
                    vendor,
                    [
                        "id",
                        "name",
                        "contact_details",
                        "address",
                        "vendor_code",
                        "on_time_delivery_rate",
                        "quality_rating_avg",
                        "average_response_time",
                        "fulfillment_rate",
                    ],
                )
                return Response(
                    {"message": "Vendor data found", "data": data},
                    status=status.HTTP_200_OK,
                )
            else:
                vendors = Vendor.objects.filter(
                    deleted_on__isnull=True
                ).all()
                data = orm_result_list_to_dict(
                    vendors,
                    [
                        "id",
                        "name",
                        "contact_details",
                        "address",
                        "vendor_code",
                        "on_time_delivery_rate",
                        "quality_rating_avg",
                        "average_response_time",
                        "fulfillment_rate",
                    ],
                )
                return Response(
                    {"message": "Vendor data found", "data": data},
                    status=status.HTTP_200_OK,
                )
        except HistoricalPerformance.DoesNotExist:
            logger.error(
                "VENDOR API VIEW - GET: Performance metric does not exist"
            )
            raise ce.NotFound("Performance metric does not exist")
        except Vendor.DoesNotExist:
            logger.error("VENDOR API VIEW - GET: Vendor does not exist")
            raise ce.NotFound("Vendor does not exist")
        except Exception as e:
            logger.error(f"VENDOR API VIEW - GET: {e}")
            raise ce.InternalServerError

    def post(self, request):
        try:
            data = request.data

            is_valid = c_validator.validate(data, schemas.VENDOR_POST)
            if not is_valid:
                raise ce.ValidationFailed(
                    {
                        "message": "Validations Failed.",
                        "data": c_validator.errors,
                    }
                )

            existing_record = Vendor.objects.filter(
                vendor_code=data["vendor_code"], deleted_on__isnull=True
            ).first()
            if existing_record:
                return Response(
                    {
                        "message": "This vendor is already present in our system."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                vendor = Vendor.objects.create(
                    name=data["name"],
                    contact_details=data["contact_details"],
                    address=data["address"],
                    vendor_code=data["vendor_code"],
                    on_time_delivery_rate=data["on_time_delivery_rate"],
                    quality_rating_avg=data["quality_rating_avg"],
                    average_response_time=data["average_response_time"],
                    fulfillment_rate=data["fulfillment_rate"],
                )
                return Response(
                    {
                        "message": "Vendor created successfully",
                        "data": orm_result_row_to_dict(
                            vendor,
                            [
                                "id",
                                "name",
                                "contact_details",
                                "address",
                                "vendor_code",
                                "on_time_delivery_rate",
                                "quality_rating_avg",
                                "average_response_time",
                                "fulfillment_rate",
                            ],
                        ),
                    },
                    status=status.HTTP_201_CREATED,
                )
        except ce.ValidationFailed as vf:
            logger.error(f"VENDOR API VIEW - POST: {vf}")
            raise
        except Exception as e:
            logger.error(f"VENDOR API VIEW - POST: {e}")
            raise ce.InternalServerError

    def put(self, request, vendor_id):
        try:
            data = request.data
            if not data:
                raise ce.ValidationFailed(
                    {"message": "Empty payload not allowed."}
                )
            is_valid = c_validator.validate(data, schemas.VENDOR_PUT)

            if not is_valid:
                raise ce.ValidationFailed(
                    {
                        "message": "Validations Failed.",
                        "data": c_validator.errors,
                    }
                )

            vendor = Vendor.objects.get(
                pk=vendor_id, deleted_on__isnull=True
            )

            # Check if the proposed PO number already exists for another record
            if "vendor_code" in data:
                existing_record = (
                    Vendor.objects.filter(
                        vendor_code=data["vendor_code"],
                        deleted_on__isnull=True,
                    )
                    .exclude(pk=vendor_id)
                    .exists()
                )
                if existing_record:
                    return Response(
                        {
                            "message": "Another vendor with the same Vendor code already exists.",
                            "data": None,
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            vendor.name = data.get("name", vendor.name)
            vendor.contact_details = data.get(
                "contact_details", vendor.contact_details
            )
            vendor.address = data.get("address", vendor.address)
            vendor.vendor_code = data.get(
                "vendor_code", vendor.vendor_code
            )
            vendor.on_time_delivery_rate = data.get(
                "on_time_delivery_rate", vendor.on_time_delivery_rate
            )
            vendor.quality_rating_avg = data.get(
                "quality_rating_avg", vendor.quality_rating_avg
            )
            vendor.average_response_time = data.get(
                "average_response_time", vendor.average_response_time
            )
            vendor.fulfillment_rate = data.get(
                "fulfillment_rate", vendor.fulfillment_rate
            )
            vendor.save()
            return Response(
                {
                    "message": "Vendor updated successfully",
                    "data": orm_result_row_to_dict(
                        vendor,
                        [
                            "id",
                            "name",
                            "contact_details",
                            "address",
                            "vendor_code",
                            "on_time_delivery_rate",
                            "quality_rating_avg",
                            "average_response_time",
                            "fulfillment_rate",
                        ],
                    ),
                },
                status=status.HTTP_200_OK,
            )
        except ce.ValidationFailed as vf:
            logger.error(f"VENDOR API VIEW - PUT: {vf}")
            raise
        except Vendor.DoesNotExist:
            logger.error("VENDOR API VIEW - PUT: Vendor does not exist")
            raise ce.NotFound("Vendor does not exist")
        except Exception as e:
            logger.error(f"VENDOR API VIEW - PUT: {e}")
            raise ce.InternalServerError

    def delete(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(
                pk=vendor_id, deleted_on__isnull=True
            )
            curr_time = datetime.now()
            vendor.deleted_on = curr_time
            vendor.save()
            PurchaseOrder.objects.filter(
                vendor_id=vendor_id, deleted_on__isnull=True
            ).update(deleted_on=curr_time)
            HistoricalPerformance.objects.filter(
                vendor_id=vendor_id, deleted_on__isnull=True
            ).update(deleted_on=curr_time)
            return Response(
                {
                    "message": "Vendor deleted successfully",
                    "data": None,
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        except Vendor.DoesNotExist:
            logger.error(
                "VENDOR API VIEW - DELETE: Vendor does not exist"
            )
            raise ce.NotFound("Vendor does not exist")
        except Exception as e:
            logger.error(f"VENDOR API VIEW - DELETE: {e}")
            raise ce.InternalServerError("An error occurred")


class PurchaseOrderAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, po_id=None):
        try:
            if po_id is not None:
                purchase_order = PurchaseOrder.objects.get(
                    pk=po_id, deleted_on__isnull=True
                )
                data = orm_result_row_to_dict(
                    purchase_order,
                    [
                        "id",
                        "po_number",
                        "vendor_id",
                        "order_date",
                        "expected_delivery_date",
                        "actual_delivery_date",
                        "items",
                        "quantity",
                        "status",
                        "quality_rating",
                        "issue_date",
                        "acknowledgment_date",
                    ],
                )
                return Response(
                    {"message": "Purchase order found", "data": data},
                    status=status.HTTP_200_OK,
                )
            else:
                purchase_orders = PurchaseOrder.objects.filter(
                    deleted_on__isnull=True
                ).all()
                data = orm_result_list_to_dict(
                    purchase_orders,
                    [
                        "id",
                        "po_number",
                        "vendor_id",
                        "order_date",
                        "expected_delivery_date",
                        "actual_delivery_date",
                        "items",
                        "quantity",
                        "status",
                        "quality_rating",
                        "issue_date",
                        "acknowledgment_date",
                    ],
                )
                return Response(
                    {
                        "message": "Purchase orders found",
                        "data": data or None,
                    },
                    status=status.HTTP_200_OK,
                )
        except PurchaseOrder.DoesNotExist:
            logger.error(
                "PURCHASE ORDER API VIEW - GET: Purchase order does not exist"
            )
            raise ce.NotFound("Purchase order does not exist")
        except Exception as e:
            logger.error(f"PURCHASE ORDER API VIEW - GET: {e}")
            raise ce.InternalServerError

    def post(self, request, po_id=None):
        try:
            data = request.data
            is_valid = c_validator.validate(
                data, schemas.PURCHASE_ORDER_POST
            )

            if not is_valid:
                raise ce.ValidationFailed(
                    {
                        "message": "Validations Failed.",
                        "data": c_validator.errors,
                    }
                )

            if po_id:
                purchase_order = PurchaseOrder.objects.get(
                    pk=po_id, deleted_on__isnull=True
                )
                purchase_order.acknowledgment_date = data.get(
                    "acknowledgment_date",
                    purchase_order.acknowledgment_date,
                )
                purchase_order.save()

                return Response(
                    {
                        "message": "Purchase order acknowledged successfully",
                        "data": None,
                    },
                    status=status.HTTP_200_OK,
                )

            existing_record = PurchaseOrder.objects.filter(
                po_number=data["po_number"], deleted_on__isnull=True
            ).first()
            if existing_record:
                return Response(
                    {
                        "message": "This PO Number already exists in our system.",
                        "data": None,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                vendor = Vendor.objects.get(
                    pk=data["vendor"], deleted_on__isnull=True
                )

                actual_delivery_date = (
                    datetime.now()
                    if data["status"] == "completed"
                    else None
                )

                po = PurchaseOrder.objects.create(
                    po_number=data["po_number"],
                    vendor=vendor,
                    order_date=data["order_date"],
                    expected_delivery_date=data[
                        "expected_delivery_date"
                    ],
                    actual_delivery_date=actual_delivery_date,
                    items=data["items"],
                    quantity=data["quantity"],
                    status=data["status"],
                    quality_rating=data.get("quality_rating"),
                    issue_date=data["issue_date"],
                    acknowledgment_date=data.get("acknowledgment_date"),
                )
                return Response(
                    {
                        "message": "Purchase order created successfully",
                        "data": orm_result_row_to_dict(
                            po,
                            [
                                "id",
                                "po_number",
                                "vendor_id",
                                "order_date",
                                "expected_delivery_date",
                                "actual_delivery_date",
                                "items",
                                "quantity",
                                "status",
                                "quality_rating",
                                "issue_date",
                                "acknowledgment_date",
                            ],
                        ),
                    },
                    status=status.HTTP_201_CREATED,
                )
        except ce.ValidationFailed as vf:
            logger.error(f"PURCHASE ORDER API VIEW - POST: {vf}")
            raise
        except Vendor.DoesNotExist:
            logger.error(
                "PURCHASE ORDER API VIEW - POST: Vendor does not exist"
            )
            raise ce.NotFound("Vendor does not exist")
        except PurchaseOrder.DoesNotExist:
            logger.error(
                "PURCHASE ORDER API VIEW - POST: Purchase order does not exist"
            )
            raise ce.NotFound("Purchase order does not exist")
        except Exception as e:
            logger.error(f"PURCHASE ORDER API VIEW - POST: {e}")
            raise ce.InternalServerError

    def put(self, request, po_id):
        try:
            data = request.data
            if not data:
                raise ce.ValidationFailed(
                    {"message": "Empty payload not allowed."}
                )
            is_valid = c_validator.validate(
                data, schemas.PURCHASE_ORDER_PUT
            )

            if not is_valid:
                raise ce.ValidationFailed(
                    {
                        "message": "Validations Failed.",
                        "data": c_validator.errors,
                    }
                )

            po = PurchaseOrder.objects.get(
                pk=po_id, deleted_on__isnull=True
            )

            vendor = Vendor.objects.get(
                pk=data["vendor"], deleted_on__isnull=True
            )

            # Check if the proposed PO number already exists for another record
            if "po_number" in data:
                existing_record = (
                    PurchaseOrder.objects.filter(
                        po_number=data["po_number"],
                        deleted_on__isnull=True,
                    )
                    .exclude(pk=po_id)
                    .exists()
                )
                if existing_record:
                    return Response(
                        {
                            "message": "Another purchase order with the same PO number already exists.",
                            "data": None,
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            po.po_number = data.get("po_number", po.po_number)
            po.vendor_id = data.get("vendor", po.vendor_id)
            po.order_date = data.get("order_date", po.order_date)
            po.expected_delivery_date = data.get(
                "expected_delivery_date", po.expected_delivery_date
            )
            po.items = data.get("items", po.items)
            po.quantity = data.get("quantity", po.quantity)
            po.status = data.get("status", po.status)
            actual_delivery_date = (
                datetime.now() if po.status == "completed" else None
            )
            po.actual_delivery_date = actual_delivery_date
            po.quality_rating = data.get(
                "quality_rating", po.quality_rating
            )
            po.issue_date = data.get("issue_date", po.issue_date)
            po.acknowledgment_date = data.get(
                "acknowledgment_date", po.acknowledgment_date
            )
            po.save()
            return Response(
                {
                    "message": "Purchase order updated successfully",
                    "data": orm_result_row_to_dict(
                        po,
                        [
                            "id",
                            "po_number",
                            "vendor_id",
                            "order_date",
                            "expected_delivery_date",
                            "actual_delivery_date",
                            "items",
                            "quantity",
                            "status",
                            "quality_rating",
                            "issue_date",
                            "acknowledgment_date",
                        ],
                    ),
                },
                status=status.HTTP_200_OK,
            )
        except ce.ValidationFailed as vf:
            logger.error(f"PURCHASE ORDER API VIEW - PUT: {vf}")
            raise
        except Vendor.DoesNotExist:
            logger.error(
                "PURCHASE ORDER API VIEW - POST: Vendor does not exist"
            )
            raise ce.NotFound("Vendor does not exist")
        except PurchaseOrder.DoesNotExist:
            logger.error(
                "PURCHASE ORDER API VIEW - PUT: Purchase order does not exist"
            )
            raise ce.NotFound("Purchase order does not exist")
        except Exception as e:
            logger.error(f"PURCHASE ORDER API VIEW - PUT: {e}")
            raise ce.InternalServerError

    def delete(self, request, po_id):
        try:
            po = PurchaseOrder.objects.get(
                pk=po_id, deleted_on__isnull=True
            )
            po.deleted_on = datetime.now()
            po.save()
            return Response(
                {
                    "message": "Purchase order deleted successfully",
                    "data": None,
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        except PurchaseOrder.DoesNotExist:
            logger.error(
                "PURCHASE ORDER API VIEW - DELETE: Purchase order does not exist"
            )
            raise ce.NotFound("Purchase order does not exist")
        except Exception as e:
            logger.error(f"PURCHASE ORDER API VIEW - DELETE: {e}")
            raise ce.InternalServerError


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    try:
        vendor = instance.vendor

        completed_purchases = vendor.purchaseorder_set.filter(
            status="completed", deleted_on__isnull=True
        )
        if (
            instance.status == "completed"
            or instance.deleted_on is not None
        ):
            # Recalculate on-time delivery rate
            # Logic: Count the number of completed POs delivered on or before expected_delivery_date
            # and divide by the total number of completed POs for that vendor.

            total_completed_purchases = completed_purchases.count()
            on_time_deliveries = completed_purchases.filter(
                actual_delivery_date__lte=F("expected_delivery_date")
            ).count()
            if total_completed_purchases > 0:
                vendor.on_time_delivery_rate = (
                    on_time_deliveries / total_completed_purchases
                ) * 100
            else:
                vendor.on_time_delivery_rate = 0

        if instance.quality_rating or instance.deleted_on is not None:
            # Recalculate quality rating average
            # Logic: Calculate the average of all quality_rating values for completed POs of the vendor.
            quality_ratings = completed_purchases.exclude(
                quality_rating__isnull=True
            ).aggregate(avg_quality_rating=Avg("quality_rating"))[
                "avg_quality_rating"
            ]
            vendor.quality_rating_avg = (
                quality_ratings if quality_ratings is not None else 0
            )

        if (
            instance.acknowledgment_date
            or instance.deleted_on is not None
        ):
            # Recalculate average response time
            # Logic: Compute the time difference between issue_date and acknowledgment_date for each PO,
            # and then find the average of these times for all POs of the vendor.
            response_times = (
                completed_purchases.exclude(
                    acknowledgment_date__isnull=True
                )
                .annotate(
                    response_time=ExpressionWrapper(
                        F("acknowledgment_date") - F("issue_date"),
                        output_field=DurationField(),
                    )
                )
                .aggregate(avg_response_time=Avg("response_time"))[
                    "avg_response_time"
                ]
            )
            vendor.average_response_time = (
                response_times.total_seconds()
                if response_times is not None
                else 0
            )

        if instance.status or instance.deleted_on is not None:
            # Recalculate fulfillment rate
            # Logic: Divide the number of successfully fulfilled POs (status 'completed' without issues)
            # by the total number of POs issued to the vendor.
            fulfilled_purchases = completed_purchases.exclude(
                status="canceled"
            )
            total_purchases = vendor.purchaseorder_set.filter(
                deleted_on__isnull=True
            ).count()
            if total_purchases > 0:
                vendor.fulfillment_rate = (
                    fulfilled_purchases.count() / total_purchases
                ) * 100
            else:
                vendor.fulfillment_rate = 0

        vendor.save()

        existing_record = HistoricalPerformance.objects.filter(
            vendor=vendor, deleted_on__isnull=True
        ).first()

        if existing_record:
            # Update existing record
            existing_record.date = datetime.now()
            existing_record.on_time_delivery_rate = (
                vendor.on_time_delivery_rate
            )
            existing_record.quality_rating_avg = (
                vendor.quality_rating_avg
            )
            existing_record.average_response_time = (
                vendor.average_response_time
            )
            existing_record.fulfillment_rate = vendor.fulfillment_rate
            existing_record.save()
        else:
            # Create a new HistoricalPerformance object
            historical_performance = HistoricalPerformance(
                vendor=vendor,
                date=datetime.now(),
                on_time_delivery_rate=vendor.on_time_delivery_rate,
                quality_rating_avg=vendor.quality_rating_avg,
                average_response_time=vendor.average_response_time,
                fulfillment_rate=vendor.fulfillment_rate,
            )

            historical_performance.save()
    except Vendor.DoesNotExist:
        logger.error("UPDATE VENDOR PERFORMANCE: Vendor does not exist")
        raise ce.NotFound("Vendor does not exist")
    except Exception as e:
        logger.error(f"UPDATE VENDOR PERFORMANCE : {e}")
        raise ce.InternalServerError
