from django.db import models
# from django.contrib.auth import get_user_model


# User=get_user_model()

class ToDo(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(blank=False)
    date = models.DateField(blank=False)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="mainapp")

    class Meta:
        verbose_name = "todo"
        verbose_name_plural = "todos"
        ordering = ["-date"]

    def __str__(self):
        return self.title
