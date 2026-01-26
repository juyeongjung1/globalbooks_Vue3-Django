from django.db import models

class Employee(models.Model):
    # idはDjangoが自動生成するため省略可
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    salary = models.IntegerField()
    location_name = models.CharField(max_length=255, null=True, blank=True)
    image_path = models.CharField(max_length=255, null=True, blank=True) # 画像用に追加
    
    def __str__(self):
        return self.name