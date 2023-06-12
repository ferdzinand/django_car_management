from django.db import models
from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import connection

#Default Values
# Color Fields
Red="rd"
Yellow="yw"
Blue="bl"
Green="grn"
Colors=[("Red",Red), ("Yellow",Yellow), ("Blue",Blue), ("Green",Green)]
    
#Brand Fields
Ferrari="fr"
Honda="hn"
Boujie="bo"
Suzuki="sz"
Toyota="ty"
Brands=[("Ferrari",Ferrari),("Honda",Honda),("Boujie",Boujie),("Suzuki",Suzuki),("Toyota",Toyota)]

class Car(models.Model):
    #DB Fields
    origin = models.CharField(max_length=50)
    brand = models.CharField(max_length=50,choices=Brands,default=None)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=50,choices=Colors,default=None)
    position=models.FloatField(max_length=50,default=0)
    

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color})" 
    
    class Meta:
        ordering = ['position','id']

# @receiver(post_save, sender=Car)
# def create_id2_trigger(sender, instance, created, **kwargs):
#         if created:
#             with connection.cursor() as cursor:
#                 cursor.execute(
#                     '''
#                     CREATE TRIGGER IF NOT EXISTS trigger_update_postion
#                     AFTER INSERT ON car_app_car
#                     BEGIN
#                         UPDATE car_app_car
#                         SET position = (SELECT COALESCE(MAX(position), 0) + 1 FROM car_app_car)
#                         WHERE id = NEW.id;
#                     END;
#                     '''
#                 )
