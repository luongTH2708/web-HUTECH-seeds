from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

class Nav(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name_nav = models.CharField(max_length=100, default='')
    code = models.TextField()
    color = models.CharField(max_length=100, default='')
    parent= models.ForeignKey("self", null=True,related_name='sub_product', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


