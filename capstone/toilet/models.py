from django.db import models

# Create your models here.
class Toilet(models.Model):
    id = models.IntegerField(primary_key=True)
    area=models.CharField(max_length=50, verbose_name='지역', null = True)
    name=models.CharField(max_length=50, verbose_name='명칭', null = True)
    address=models.CharField(max_length=150, verbose_name='소재지', null = True)
    using=models.CharField(max_length=50, verbose_name='주용도', null = True)
    way=models.CharField(max_length=100, verbose_name='처리방식', null = True)
    bellYN=models.CharField(max_length=10, verbose_name='비상벨 여부', null=True, default='여')  
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'capstone_toilet'
        verbose_name = '화장실'
        verbose_name_plural = '화장실'