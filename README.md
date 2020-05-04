# Inclusive Django Range Fields

![Inclusive](https://media.giphy.com/media/xUOwGdD7RGT4CTnUaY/giphy.gif "Inclusive")

The default bound of Django range fields is `[)`. This package follows default bounds as `[]`.

## How to use?

```sh
pip install inclusive-django-range-fields
```

### Django

```python
# models.py

from django.db import models
from inclusive_django_range_fields import InclusiveIntegerRangeField

class AdCampaign(models.Model):
    age_target = InclusiveIntegerRangeField()
```

```
>> AdCampaign.objects.first().age_target
NumericRange(18, 30, '[]')
```
### Django Rest Framework

```python
# serializers.py

from rest_framework import serializers
from inclusive_django_range_fields.drf import InclusiveIntegerRangeField

class AdCampaignSerializer(serializers.ModelSerializer):
    age_target = InclusiveIntegerRangeField()

    class Meta:
        model = AdCampaign
        fields = (
            "id",
            "age_target",
        )
```

```json
{
  "id": 1993,
  "age_target": {
    "lower": 18,
    "upper": 30
  }
}
```

## Reference

### Model Fields

- `inclusive_django_range_fields.InclusiveIntegerRangeField`
- `inclusive_django_range_fields.InclusiveBigIntegerRangeField`
- `inclusive_django_range_fields.InclusiveDateRangeField`

### Ranges

- `inclusive_django_range_fields.InclusiveNumericRange`
- `inclusive_django_range_fields.InclusiveDateRange`
- `inclusive_django_range_fields.InclusiveDateTimeTZRange`


### Django Rest Framework Serializers

- `inclusive_django_range_fields.drf.InclusiveIntegerRangeField`
- `inclusive_django_range_fields.drf.InclusiveDateRangeField`


### Form Fields

- `inclusive_django_range_fields.InclusiveIntegerRangeFormField`
- `inclusive_django_range_fields.InclusiveDateRangeFormField`


## PyPI
https://pypi.org/project/inclusive-django-range-fields/
