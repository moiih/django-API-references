from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length=50)  ## 'paradigm' = a typical example or pattern of something; a pattern or model.

    def __str__(self):
        return self.name

    # def __str__(self):
    #     return self.paradigm

    class Meta:
        db_table = 'my_api_languages'


