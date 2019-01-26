from django.db import models
from registration.models import User
from menu.models import Snacks, StreetFood, Beverages, Breads, Vegetable, Rice, Desserts


# Create your models here.

class OrderItem(models.Model):
    product_snacks = models.OneToOneField(Snacks, on_delete=models.SET_NULL(), null=True)
    product_streetfood = models.OneToOneField(StreetFood, on_delete=models.SET_NULL(), null=True)
    product_beverages = models.OneToOneField(Beverages, on_delete=models.SET_NULL(), null=True)
    product_breads = models.OneToOneField(Breads, on_delete=models.SET_NULL(), null=True)
    product_vegetable = models.OneToOneField(Vegetable, on_delete=models.SET_NULL(), null=True)
    product_rice = models.OneToOneField(Rice, on_delete=models.SET_NULL(), null=True)
    product_dessert = models.OneToOneField(Desserts, on_delete=models.SET_NULL(), null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return '{}{}{}{}{}{}{}' .format(self.product_snacks.snacks, self.product_streetfood.streetfood, self.product_beverages.beverages, self.product_breads.breads, self.product_vegetable.vegetable, self.product_rice.rice, self.product_dessert.desserts)


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL(), null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(null=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum(item.product_snacks.snacks_amt for item in self.items.all()) + sum(item.product_streetfood.streetfood_amt for item in self.items.all()) + sum(item.product_beverages.beverages_amt for item in self.items.all()) + sum(item.product_breads.breads_amt for item in self.items.all()) + sum(item.product_vegetable.vegetable_amt for item in self.items.all()) + sum(item.product_rice.rice_amt for item in self.items.all()) + sum(item.product_dessert.desserts_amt for item in self.items.all())

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)



