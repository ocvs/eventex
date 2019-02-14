from django.db import models
import uuid


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
    #masked_id = models.UUIDField('masked_id', default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = "Inscrições"
        verbose_name = 'inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
