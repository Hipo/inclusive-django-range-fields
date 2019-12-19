from django.contrib.postgres.fields import IntegerRangeField

from inclusive_django_range_fields.forms import InclusiveIntegerRangeFormField


class InclusiveIntegerRangeField(IntegerRangeField):
    form_field = InclusiveIntegerRangeFormField

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        else:
            if not value.upper_inf and not value.upper_inc and value._bounds != "[]":
                value._upper -= 1
                value._bounds = "[]"

        return value

