from django.db import models
from datetime import datetime

# Create your models here.


#n1 MODELO CATEGORIAS
class Categoria(models.Model):
    id =  models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la categoria',max_length=150,unique=True,blank=False,null=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


#n2 MODELO DE PRODUCTOS
class  Producto(models.Model):
    id = models.AutoField(primary_key=True)
    id_categoria =  models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField('Nombre del producto',max_length=150,unique=True,blank=False,null=False)
    imagen = models.ImageField(upload_to =  'product/%y/%m/%d',null=True,blank=True)
    pvp =  models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
    
#n3 MODELO DE CLIENTES
class  Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombre del producto',max_length=150,unique=True,blank=False,null=False)
    apellidos = models.CharField('Nombre del producto',max_length=150,unique=True,blank=False,null=False)
    dni = models.CharField('Numero de identidad',max_length=10, unique=True,blank=False,null=False)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', default = datetime.now, null=False,blank=False)
    direccion  = models.CharField('Direccion', max_length=150, blank=False, null=False)
    sexo_choices =  (
        ('Honbre','Hombre'),
        ('Mujer','Mujer'),
    )
    sexo =  models.CharField('Sexo',max_length = 50, choices=sexo_choices)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombres']
    
    def __str__(self):
        return self.nombres

#n4 MODELO VENTAS
class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente =  models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fecha_venta = models.DateField('Fecha de venta',default=datetime.now, null = False,blank = False)
    iva = models.DecimalField('Impuesto al valor agregado', default=0.00, max_digits=9, decimal_places=2, null=False,blank=False)
    total = models.DecimalField('Total venta', default=0.00, max_digits=9, decimal_places=2, null=False,blank=False)
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']
    
    def __str__(self):
        return self.id_cliente.nombres
    
#n5 DETALLE DE VENTAS
class Detalle_Venta(models.Model):
    id = models.AutoField(primary_key=True)
    id_venta =  models.ForeignKey(Venta, on_delete = models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    precio = models.DecimalField('Precio del producto', default=0.00, max_digits=9, decimal_places=2, null=False,blank=False)
    cantidad = models.IntegerField('Cantidad del producto', default=0)
    subtotal = models.DecimalField('Subtotal detalle', default=0.00, max_digits=9, decimal_places=2, null=False,blank=False)
    
    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalle Ventas'
        ordering = ['id']
    
    def __str__(self):
        return self.id_producto.nombre
    
    