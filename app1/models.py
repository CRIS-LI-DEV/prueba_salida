from django.db import models
from django.contrib.auth.models import User





#TABLAS AUXILIARES
class EstadoPedido(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.nombre}"

class Comuna(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

class Region(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

class FormaDePago(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

class Rubro(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"









#ENTIDADES QUE DESCIENDE DE USER

class UsuarioStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=200,null=True)
    direccion = models.CharField(max_length=200,null=True)
    rut= models.CharField(max_length=200,null=True)
  
    comuna= models.ForeignKey(Comuna, on_delete=models.CASCADE,null=True)
    region= models.ForeignKey(Region, on_delete=models.CASCADE,null=True)
  

    class Meta:
        permissions = [
            ("permiso_staff", "puede acceder a las intefaces del staff")]

    def __str__(self):
        return f"{self.user.username}|{self.user.last_name}|{self.comuna}"



class Cliente(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identificador = models.CharField(max_length=200,null=True)
    telefono = models.CharField(max_length=200,null=True)
   
    rut= models.CharField(max_length=200,null=True)
    
    direccion = models.CharField(max_length=200,null=True)
    comuna= models.ForeignKey(Comuna, on_delete=models.CASCADE,null=True)
    region= models.ForeignKey(Region, on_delete=models.CASCADE,null=True)
    
  

    class Meta:
        permissions = [
            ("permiso_cliente", "puede acceder a las intefaces del cliente")]

    def __str__(self):
        return f"{self.user.username}|{self.user.last_name}|{self.comuna}"




class Productor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=200,null=True)
   
    direccion = models.CharField(max_length=200,null=True)
    rut= models.CharField(max_length=100)

    razon_social = models.CharField(max_length=200,null=True)
    rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE,null=True)
    
    comuna= models.ForeignKey(Comuna, on_delete=models.CASCADE,null=True)
    region= models.ForeignKey(Region, on_delete=models.CASCADE,null=True)


    nombre_contacto = models.CharField(max_length=200,null=True)

    class Meta:
        permissions = [
            ("permiso_proveedor", "puede acceder a las intefaces del proveedor")]

    def __str__(self):
        return f"{self.user.username}|{self.user.last_name}|{self.comuna}"

#ENTIDAD PRODUCTO

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion= models.CharField(max_length=255,null=True)
    
    precio = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)
    
    imagen_b = models.BinaryField(null=True)
    imagen_f = models.ImageField(upload_to='images/',null=True)
    productor= models.ForeignKey(Productor, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.nombre}|{self.precio}|{self.descripcion}"


#ENTIDADES DE COMPRA



class Carrito(models.Model):
    
    cantidad_total =   models.IntegerField( null=True)
    precio_total = models.IntegerField( null=True)
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,null=True)
    empleado = models.ForeignKey(UsuarioStaff, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.cantidad_total}|{self.precio_total}|"

class DetalleProductoSocilicitado(models.Model):
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    
    valor_producto = models.IntegerField()
    cantidad = models.IntegerField()

    
    def __str__(self):
        return f"{self.producto.nombre}|{self.carrito}|{self.cantidad}"




class Pedido(models.Model):
    
    carrito = models.ForeignKey(Carrito , on_delete=models.CASCADE)
   

    fecha = models.DateField(null=True)
    estado = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE,null=True)
   
    calle_entrega = models.CharField(max_length=200,null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE,null=True)
    region= models.ForeignKey(Region, on_delete=models.CASCADE,null=True)

    
    def __str__(self):
        return f"{self.fecha}|{self.estado}|{self.calle_entrega}|{self.comuna}"

class ImagenesAuxiliares(models.Model):
    nombre = models.CharField(max_length=200) 
    imagen_b = models.BinaryField(null=True)
    imagen_f = models.ImageField(upload_to='images/',null=True)
   



