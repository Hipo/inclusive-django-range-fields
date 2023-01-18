from django.contrib.postgres.forms import BaseRangeField, IntegerRangeField, DateRangeField


class BaseInclusiveRangeFormField(BaseRangeField):

    def compress(self, values):
        values = super().compress(values)
        if value is not None:
            values._bounds = "[]"
        return values


class InclusiveIntegerRangeFormField(BaseInclusiveRangeFormField, IntegerRangeField):
    pass


class InclusiveDateRangeFormField(BaseInclusiveRangeFormField, DateRangeField):
    pass
