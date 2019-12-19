from rest_framework import serializers

from inclusive_django_range_fields import ranges


class InclusiveIntegerRangeField(serializers.Field):

    def to_representation(self, value):
        return {
            "lower": value.lower,
            "upper": value.upper,
        }

    def to_internal_value(self, data):
        return ranges.InclusiveNumericRange(lower=data["lower"], upper=data["upper"])


class InclusiveDateRangeField(serializers.Field):

    def to_representation(self, value):
        return {
            "lower": value.lower,
            "upper": value.upper,
        }

    def to_internal_value(self, data):
        return ranges.InclusiveDateRange(lower=data["lower"], upper=data["upper"])
