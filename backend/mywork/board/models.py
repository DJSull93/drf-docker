from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    create_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'posts'