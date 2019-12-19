# Inclusive Django Range Fields

![I love all inclusive](https://media.giphy.com/media/5YiNunQI0Wg9Mpc6Ts/giphy.gif "I love all inclusive")

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
