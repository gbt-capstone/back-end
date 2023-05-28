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
    for_disabled=models.CharField(max_length=10, verbose_name='장애인 전용', null = True, default='N')
    separate=models.CharField(max_length=10, verbose_name='남녀분리', null=True, default='Y')
    toilet_count=models.IntegerField(verbose_name='좌변기 갯수', null=True)
    washstand=models.CharField(max_length=10, verbose_name='세면대', null = True, default='Y')
    hand_sanitizer=models.CharField(max_length=10, verbose_name='손 세정제', null=True)
    toilet_paper=models.CharField(max_length=10, verbose_name='휴지', null=True,default='Y')
    for_children=models.CharField(max_length=10, verbose_name='아동 전용', null=True)
    diaper_change=models.CharField(max_length=10, verbose_name='기저귀 교환대', null=True)
    women_safe=models.CharField(max_length=10, verbose_name='여성 안심 화장실', null=True)
    cleanliness=models.FloatField(verbose_name='청결도', default=0)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'capstone_toilet'
        verbose_name = '화장실'
        verbose_name_plural = '화장실'