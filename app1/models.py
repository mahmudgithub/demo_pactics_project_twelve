from django.db import models

class post(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField() #ForeignKey('auth.user',on_delete=models.CASCADE,)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    about = models.TextField()
    value = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    

    class Meta:
        verbose_name_plural = "Post"

    def __str__(self):
        return self.name