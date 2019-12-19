from datetime import timedelta

from django.contrib.postgres.fields import RangeField, IntegerRangeField, BigIntegerRangeField, DateRangeField

from inclusive_django_range_fields.forms import InclusiveIntegerRangeFormField, InclusiveDateRangeFormField


class BaseInclusiveRangeField(RangeField):
    form_field = None
    precision = None

    def from_db_value(self, value, expression, connection):
        if value is not None:
            if not value.upper_inf and not value.upper_inc and value._bounds != "[]":
                value._upper -= self.precision
                value._bounds = "[]"

        return value


class InclusiveIntegerRangeField(BaseInclusiveRangeField, IntegerRangeField):
    form_field = InclusiveIntegerRangeFormField
    precision = 1


class InclusiveBigIntegerRangeField(BaseInclusiveRangeField, BigIntegerRangeField):
    form_field = InclusiveIntegerRangeFormField
    precision = 1


class InclusiveDateRangeField(BaseInclusiveRangeField, DateRangeField):
    form_field = InclusiveDateRangeFormField
    precision = timedelta(days=1)
