from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    @property
    def producs_count (self):
        return self.product_set.count()


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    @property
    def rating (self):
        stars_list = [review.stars for review in self.reviews.all()]
        return sum(stars_list) / len(stars_list)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(max_length=500)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    CHOISES = ((i, "*" * i)for i in range(1,6))
    stars = models.IntegerField(choices=CHOISES, default=5)


