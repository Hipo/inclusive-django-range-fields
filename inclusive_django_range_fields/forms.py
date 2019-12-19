from django.contrib.postgres.forms import IntegerRangeField


class InclusiveIntegerRangeFormField(IntegerRangeField):

    def compress(self, values):
        values = super().compress(values)
        values._bounds = "[]"
        return values
