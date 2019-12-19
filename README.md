# Inclusive Django Range Fields

![Inclusive](https://media.giphy.com/media/xUOwGdD7RGT4CTnUaY/giphy.giff "Inclusive")

## How to use?

```python
from django.db import models
from inclusive_django_range_fields import InclusiveIntegerRangeField

class AdCampaign(models.Model):
    age_target = models.InclusiveIntegerRangeField()
```

## Reference

### Model Fields

- `inclusive_django_range_fields.InclusiveIntegerRangeField`
- `inclusive_django_range_fields.InclusiveBigIntegerRangeField`
- `inclusive_django_range_fields.InclusiveDateRangeField`

### Form Fields

- `inclusive_django_range_fields.forms.InclusiveIntegerRangeFormField`
- `inclusive_django_range_fields.forms.InclusiveDateRangeFormField`
