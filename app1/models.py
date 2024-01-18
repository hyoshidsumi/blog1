from django.db import models

CATEGORY = (('todo', 'Todo'), ('blog', 'Blog'), ('else', 'Else'))


class blogModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=40, choices=CATEGORY)
    blogImage = models.ImageField(upload_to='', null=True, blank=True)
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    cdate = models.DateTimeField(null=True, blank=True)
    udate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class a1Model(models.Model):
    title = models.CharField(max_length=100)
    a1image = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.title
