from django.db import models


# Create your models here.
class Usuario(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    username = models.CharField(max_length=50, verbose_name='Username')
    email = models.EmailField()
    password = models.CharField(max_length=50, verbose_name='Password')
    api_keys = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return f"{self.username} | ID: {self.id} , {self.email}"



class Dream(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    fecha = models.DateTimeField(auto_now_add=True)
    titulo = models.TextField(max_length=200)
    is_public = models.BooleanField(default=False)
    userId = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # BigAutoField -> ?
    title = models.TextField(max_length=400)

    def get_prompts(self):
        pass



class AiAnswer(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    dreamId = models.ForeignKey(Dream, on_delete=models.CASCADE)
    prompt = models.TextField(max_length=600)
    ans = models.JSONField(default=dict, blank=True, null=True)
    params = models.JSONField(default=dict, blank=True, null=True)