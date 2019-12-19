from django.contrib.postgres.forms import RangeField, IntegerRangeField, DateRangeField


class BaseInclusiveRangeFormField(RangeField):

    def compress(self, values):
        values = super().compress(values)
        values._bounds = "[]"
        return values


class InclusiveIntegerRangeFormField(BaseInclusiveRangeFormField, IntegerRangeField):
    pass


class InclusiveDateRangeFormField(BaseInclusiveRangeFormField, DateRangeField):
    pass
