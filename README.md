# Inclusive Django Range Fields

![Inclusive](https://media.giphy.com/media/xUOwGdD7RGT4CTnUaY/giphy.gif "Inclusive")

## How to use?

### Django

```python
# models.py

from django.db import models
from inclusive_django_range_fields import InclusiveIntegerRangeField

class AdCampaign(models.Model):
    age_target = models.InclusiveIntegerRangeField()
```

### Django Rest Framework

```python
# serializers.py

from rest_framework import serializers
from inclusive_django_range_fields.django_rest_framework.fields import InclusiveIntegerRangeField

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

- `inclusive_django_range_fields.ranges.InclusiveNumericRange`
- `inclusive_django_range_fields.ranges.InclusiveDateRange`


### Django Rest Framework Serializers

- `inclusive_django_range_fields.django_rest_framwork.fields.InclusiveIntegerRangeField`
- `inclusive_django_range_fields.django_rest_framwork.fields.InclusiveDateRangeField`


### Form Fields

- `inclusive_django_range_fields.forms.InclusiveIntegerRangeFormField`
- `inclusive_django_range_fields.forms.InclusiveDateRangeFormField`
