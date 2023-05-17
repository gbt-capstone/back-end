from django.db import models

# Create your models here.
class Toilet(models.Model):
    id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50, verbose_name='이름')
    address=models.CharField(max_length=150, verbose_name='주소')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'capstone_toilet'
        verbose_name = '화장실'
        verbose_name_plural = '화장실'