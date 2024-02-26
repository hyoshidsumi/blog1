from django.db import models


# Create your models here.
class m2(models.Model):
    title = models.CharField(max_length=400)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'app2'