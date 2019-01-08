from django.db import models

class Product(models.Model):
    department = models.IntegerField(default=0, null=True)
    department_id = models.IntegerField(default=0, null=True)
    aisle = models.IntegerField(default=0, null=True)
    aisle_id = models.IntegerField(default=0, null=True)
    product = models.IntegerField(default=0, null=True)
    product_id = models.IntegerField(default=0, null=True)
    product_count = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.department
        return self.aisle
        return self.product

    class Meta:
        ordering = ['department']

class Vip_reorder(models.Model):
    department=models.CharField(max_length=200,null=True)
    reordered=models.FloatField(max_length=200,null=True)

class Vip_aisle(models.Model):
    aisle=models.CharField(max_length=200,null=True)
    ratio=models.FloatField(max_length=200,null=True)

class Order_dow(models.Model):
    Sat = models.IntegerField(default=0, null=True)
    Sun = models.IntegerField(default=0, null=True)
    Mon = models.IntegerField(default=0, null=True)
    Tues = models.IntegerField(default=0, null=True)
    Wed = models.IntegerField(default=0, null=True)
    Thrs = models.IntegerField(default=0, null=True)
    Fri = models.IntegerField(default=0, null=True)

class Product_middle(models.Model):
    aisle_id=models.IntegerField(null=False, primary_key=True)
    aisle=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.aisle

class Product_small(models.Model):
    product_id=models.FloatField(max_length=200,null=False, primary_key=True, default=999999)
    product_name=models.CharField(max_length=200,null=True)
    aisle_id=models.ForeignKey(Product_middle, on_delete=models.CASCADE)
