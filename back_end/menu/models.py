from django.db import models


class MenuItem(models.Model):
    """Item on a menu"""

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return "{}: €{}".format(self.name, str(self.price))

    class Meta:
        ordering = ("name",)
        unique_together = ("name", "price")
