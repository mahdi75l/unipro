from django.db import models

# Create your models here.


class CategoryGuid(models.Model):
    name = models.CharField("دسته بندی راهنمایی ها", max_length= 50, unique=True)
    about = models.TextField()

    def __str__(self):
        return self.name


class Guid(models.Model):
    categoryguid = models.ForeignKey(CategoryGuid,on_delete=models.CASCADE)
    name = models.CharField("دسته بندی", max_length= 50, unique=True)
    about = models.TextField()
    address = models.FileField(upload_to="FileGuid/",blank=True,null=True)
    ceated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name