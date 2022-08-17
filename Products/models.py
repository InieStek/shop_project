from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.

class Producent(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=60)
    descryption = models.TextField(blank=True)

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producers"

class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"


class Products(models.Model):
    category = models.ForeignKey(Category, null=True, blank = True, on_delete=models.CASCADE)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    descryption = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    slug = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product-image', default='', blank=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"

    def __unicode__(self):
        return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)

    def total_price(self):
        return self.quantity * self.unit_price

    total_price = property(total_price)

    # product
    def get_product(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)

    def set_product(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk

    product = property(get_product, set_product)






