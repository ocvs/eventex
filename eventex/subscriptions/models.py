from django.db import models
import uuid

from eventex.subscriptions.validators import validate_cpf


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    email = models.EmailField('e-mail', blank=True)
    phone = models.CharField('telefone', blank=True, max_length=20)
    masked_id = models.UUIDField('masked_id', default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    paid = models.BooleanField('pago', default=False)

    class Meta:
        verbose_name_plural = "Inscrições"
        verbose_name = 'inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
