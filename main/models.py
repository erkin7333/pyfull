from django.db import models

class Post(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.RESTRICT)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()
    added_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'
        index_together  = (
            ('user', 'added_at'),
            ('added_at',)
        )

