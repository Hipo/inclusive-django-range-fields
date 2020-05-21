from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from inclusive_django_range_fields import InclusiveNumericRange, InclusiveDateRange


def _validate_data_shape(data):
    if not data.get("lower"):
        raise ValidationError("lower is required")
    elif not data.get("upper"):
        raise ValidationError("upper is required")


class InclusiveIntegerRangeField(serializers.Field):

    def to_representation(self, value):
        return {
            "lower": value.lower,
            "upper": value.upper,
        }

    def to_internal_value(self, data):
        _validate_data_shape(data=data)

        lower = serializers.IntegerField().to_internal_value(data["lower"])
        upper = serializers.IntegerField().to_internal_value(data["upper"])

        return InclusiveNumericRange(lower=lower, upper=upper)


class InclusiveDateRangeField(serializers.Field):

    def to_representation(self, value):
        return {
            "lower": value.lower,
            "upper": value.upper,
        }

    def to_internal_value(self, data):
        _validate_data_shape(data=data)

        lower = serializers.DateField().to_internal_value(data["lower"])
        upper = serializers.DateField().to_internal_value(data["upper"])

        return InclusiveDateRange(lower=lower, upper=upper)
