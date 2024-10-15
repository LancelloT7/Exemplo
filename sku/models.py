from django.db import models
from django.utils.translation import gettext_lazy as _

class Sku(models.Model):
    sku = models.CharField(max_length=100, unique=True, verbose_name=_("SKU"))  # SKU único no banco de dados
    modelo_revenda = models.CharField(max_length=100, verbose_name=_("Modelo Revenda"))

    def __str__(self):
        return f"{self.sku} - {self.modelo_revenda}"

class ModeloSufixo(models.Model):
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE, related_name='sufixos')
    sufixo = models.CharField(max_length=100, verbose_name=_("Sufixo"))

    def __str__(self):
        return f"{self.sku.sku} - {self.sufixo}"

class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} - {self.cargo}"

class Produto(models.Model):
    data_entrada = models.DateField(auto_now_add=True)
    responsavel_entrada = models.ForeignKey(Funcionario, on_delete=models.PROTECT, related_name='produtos_responsaveis')
    ptn = models.CharField(max_length=100, unique=True)
    serie = models.CharField(max_length=100)
    
    # Relaciona o produto a um SKU
    sku = models.ForeignKey(Sku, on_delete=models.PROTECT, related_name='produtos_sku')
    modelo_revenda = models.CharField(max_length=100, verbose_name=_("Modelo Revenda"), blank=True)
    modelo_sufixo = models.ForeignKey(ModeloSufixo, on_delete=models.PROTECT, related_name='produtos_modelo_sufixo', null=True, blank=True)

    def save(self, *args, **kwargs):
        # Preencher automaticamente o modelo_revenda se o SKU já existir
        if self.sku:
            self.modelo_revenda = self.sku.modelo_revenda
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ptn} - {self.serie} - {self.responsavel_entrada.nome} - {self.sku}"
