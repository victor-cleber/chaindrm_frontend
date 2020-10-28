from django.db import models

class DigitalContent(models.Model):    
    file_name=models.CharField(db_column='file_name', max_length=100, blank=False)
    hash_id=models.CharField(db_column='hash_id', max_length=100, blank=False)
    date_created=models.DateTimeField(auto_now_add=True,blank=False)