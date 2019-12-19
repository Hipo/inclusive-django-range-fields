from rest_framework import serializers

from inclusive_django_range_fields import InclusiveNumericRange, InclusiveDateRange


class InclusiveIntegerRangeField(serializers.Field):

    def to_representation(self, value):
        return {
            "lower": value.lower,
            "upper": value.upper,
        }

    def to_internal_value(self, data):
        return InclusiveNumericRange(lower=data["lower"], upper=data["upper"])


class InclusiveDateRangeField(serializers.Field):

    def to_representation(self, value):
        return {
            "lower": value.lower,
            "upper": value.upper,
        }

    def to_internal_value(self, data):
        return InclusiveDateRange(lower=data["lower"], upper=data["upper"])
