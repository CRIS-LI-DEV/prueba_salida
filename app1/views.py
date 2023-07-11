from django.shortcuts import render,redirect
from app1.forms import *
from app1.models import *
from django.views import View
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from app1.forms import *
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
import string
import random
from django.core.mail import send_mail
import uuid
from app1.models import *
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth.decorators import permission_required

def home(request):
    template = 'home.html'
    return render(request,template)





# def loginUsuario(request):
#     if request.method=='POST':

#         redirect('/')
#     else:
#         form = LoginUsuario()
#         return render(request, 'login.html', {'form': form})






def loginUsuario(request):
    if request.method == 'POST':

        form = LoginUsuario(request.POST)

        print(form['clave'].value())

        if form.is_valid():
            username = form.cleaned_data['usuario']
            password = form.cleaned_data['clave']

            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:

                login(request, user)

                staff = UsuarioStaff.objects.filter(
                    user_id=user.id).count()
                productor = Productor.objects.filter(
                    user_id=user.id).count()
                cliente = Cliente.objects.filter(
                    user_id=user.id).count()

                if staff==1 and productor == 0 and cliente == 0:
                    return redirect('/p_staff/')
                if staff == 0 and productor == 0 and cliente == 1:
                    return redirect('/p_cliente/')
                if staff == 0 and productor == 1 and cliente == 0:
                    return redirect('/p_prod/')

               
            else:
                pass
            return redirect('/')
    else:
        form = LoginUsuario()
        return render(request, 'login.html', {'form': form})





permission_required('permiso_staff')
def perfil_staff(request):
    print("llegue")
    pedidos = Pedido.objects.all()
    
    template='staff.html'
    #return HttpResponse("FUNCIONA")
    return render(request,template,{'lista':pedidos})

permission_required('permiso_cliente')
def perfil_cliente(request):
    template='perfil_cliente.html'
    pedidos = Pedido.objects.filter(id=request.user.id)
    return render(request,template,{'lista':pedidos})




def perfil_productor(request):
    template='perfil_productor.html'
    pedidos = Pedido.objects.filter(id=request.user.id)
    return render(request,template,{'lista':pedidos})






def registro_producto_staff(request):

    if request.method == 'POST':
        
        form = FormularioRegistroProductoStaff(request.POST)
        
        imagen = request.FILES['archivo']
        producto = Producto(nombre =form['nombre'].value(),  precio =form['precio'].value(), descripcion = form['descripcion'].value() )
        producto.imagen_b = imagen.read()
        producto.imagen_f = imagen
        producto.save()
        return redirect('/tomar_pedido_staff/')

    else:

        form = FormularioRegistroProductoStaff()
      
        return render(request, 'registrar_producto_staff.html', {'form': form})




def registro_producto_pro(request):

    if request.method == 'POST':
        
        form = FormularioRegistroProductoProductor(request.POST, request.FILES)
        
        imagen = request.FILES['archivo']
        producto = Producto(nombre =form['nombre'].value(),  precio =form['precio'].value(), descripcion = form['descripcion'].value() )
        producto.imagen_b = imagen.read()
        producto.imagen_f = imagen
        producto.save()
        return redirect('/tomar_pedido_staff/')

    else:

        form = FormularioRegistroProductoProductor()
      
        return render(request, 'registrar_producto_staff.html', {'form': form})














def registrar_cliente(request):

    if request.method == 'POST':
        
        form = FormularioRegistroCliente(request.POST, request.FILES)
        
        imagen = request.FILES['archivo']
        producto = Producto(nombre =form['nombre'].value(),  precio =form['precio'].value(), descripcion = form['descripcion'].value() )
        producto.imagen_b = imagen.read()
        producto.imagen_f = imagen
        producto.save()
        return redirect('/tomar_pedido_staff/')

    else:

        form = FormularioRegistroCliente()
      
        return render(request, 'registrar_producto_staff.html', {'form': form})




class HacerPedidoCliente(View):
   
    id_carrito = None
    def get(self,request):
   
        carrito = Carrito(precio_total=0,cantidad_total=0)
        carrito.save()
        self.id_carrito = carrito.id
       
        lista = Producto.objects.all()
        carrito = request.session.get("carrito")     
        template="hacer_pedido_cliente.html"
       
        return render(request,template,context={'lista':lista, 'carrito': carrito})
        #return HttpResponse(lista)
    def post(self,request):
        pass






class HacerPedidoStaff(View):
   
    id_carrito = None
    def get(self,request):
   
        carrito = Carrito(precio_total=0,cantidad_total=0)
        carrito.save()
        self.id_carrito = carrito.id
       
        lista = Producto.objects.all()
        carrito = request.session.get("carrito")     
        template="hacer_pedido_staff.html"
       
        return render(request,template,context={'lista':lista, 'carrito': carrito})
        #return HttpResponse(lista)
    def post(self,request):
        pass


class HacerPedidoProd(View):
   
    id_carrito = None
    def get(self,request):
   
        carrito = Carrito(precio_total=0,cantidad_total=0)
        carrito.save()
        self.id_carrito = carrito.id
       
        lista = Producto.objects.all()
        carrito = request.session.get("carrito")     
        template="hacer_pedido_productor.html"
       
        return render(request,template,context={'lista':lista, 'carrito': carrito})
        #return HttpResponse(lista)
    def post(self,request):
        pass



def funcion_para_guardar_cliente(request):
    if request.method=="POST":
        formulario = FormularioAgregarProductoCarrito(request.POST)

        if request.session.get('carrito') == None:
        
            request.session['carrito']=[]
        
        carrito = request.session.get('carrito')
        producto = Producto.objects.get(id=formulario['producto_id'].value())
        carrito.append({"producto":formulario['producto_id'].value(),"cantidad":formulario['cantidad_id'].value(),'nombre':producto.nombre})
        
        request.session['carrito'] = carrito
        return redirect('/hacer_pedido_cliente/')


permission_required('permiso_staff')
def funcion_para_guardar_staff(request):
    if request.method=="POST":
        formulario = FormularioAgregarProductoCarrito(request.POST)

        if request.session.get('carrito') == None:
        
            request.session['carrito']=[]
        
        carrito = request.session.get('carrito')
        
        producto = Producto.objects.get(id=formulario['producto_id'].value())

        carrito.append({"producto":formulario['producto_id'].value(),"cantidad":formulario['cantidad_id'].value(),'nombre':producto.nombre})
        
        request.session['carrito'] = carrito
        return redirect('/hacer_pedido_staff/')



class FinalizarPedidoCliente(View):
    # permission_required('permiso_cliente')
    def get(self,request):

        opciones_region = Region.objects.all().values_list('nombre', flat=True)
        opciones_comuna = Comuna.objects.all().values_list('nombre', flat=True)
        opciones_username = Cliente.objects.all()
        OPCIONES_REGION = tuple([(opcion, opcion) for opcion in opciones_region])
        OPCIONES_COMUNA = tuple([(opcion, opcion) for opcion in opciones_comuna] )
        OPCIONES_USERNAME = tuple([(opcion.user.username, opcion.user.username) for opcion in opciones_username] )

        carrito = request.session.get('carrito')
        formulario = FormularioPedidoCliente()
        formulario.fields['comuna'].choices = OPCIONES_COMUNA
        formulario.fields['region'].choices = OPCIONES_REGION
        template = 'finalizar_pedido_cliente.html'
        context = {'formulario':formulario,'carrito':carrito}
        return render(request,template,context)
        
    # permission_required('permiso_cliente')
    def post(self,request):
        formulario = FormularioPedidoCliente(request.POST)
       
        
          
        usuario_cliente =  User.objects.get(id=request.user.id)

        cliente = Cliente.objects.get(user_id= usuario_cliente.id)
        
            
        carrito= Carrito(
                cantidad_total= 0,
                precio_total=0,
                cliente = cliente
      
                 )
        carrito.save()
        carrito_session = request.session.get('carrito')
        suma_precio=0
        for x in carrito_session:
                producto = Producto.objects.get(id=x['producto'])
                cantidad = x['cantidad']
                detalle = DetalleProductoSocilicitado(
                    producto =producto,
                    cantidad= cantidad,
                    valor_producto = producto.precio,
                    carrito = carrito
                 )
        detalle.save()
        suma_precio = suma_precio + (int(producto.precio) * int(cantidad))
        suma_cantidad= DetalleProductoSocilicitado.objects.filter(carrito_id = carrito.id).aggregate(total=Sum('cantidad'))
        carrito.cantidad_total = suma_cantidad['total']
        carrito.precio_total = suma_precio
        carrito.save()
        estado = EstadoPedido.objects.get(id=1)
        comuna = Comuna.objects.get(nombre=formulario['comuna'].value())
        region = Region.objects.get(nombre=formulario['region'].value())
        pedido = Pedido( 
                    fecha = formulario['fecha_entrega'].value(),
                    estado=estado,
                    calle_entrega=formulario['direccion'].value(),
                    comuna=comuna,
                    region=region,
                    carrito = carrito         
                    
                )        

        pedido.save()
        return redirect('/p_cliente')

# permission_required('permiso_empleado')
def limpiar_carrito_staff(request):
    request.session['carrito']=[]
    return redirect('/hacer_pedido_staff/')

# permission_required('permiso_cliente')
def limpiar_carrito_cliente(request):
    request.session['carrito']=[]
    return redirect('/hacer_pedido_cliente/')


# # permission_required('permiso_empleado')
# def modificar_estado_pedido(request,id_pedido):
    
#     formulario = FormularioEstado(request.POST)

#     if formulario.is_valid():
#         nombre_estado = formulario.cleaned_data['estado']
#         estado = EstadoPedido.objects.get(nombre=nombre_estado)
#         pedido=Pedido.objects.get(id=id_pedido)
#         pedido.estado = estado
#         pedido.save()
        
#         email = pedido.carrito.cliente.user.email
#         print(email)
#         destinatarios=[email]
#         asunto = 'ESTADO DE TU PEDIDO'
#         cuerpo = 'TU PEDIDO ESTA ' + nombre_estado
               
#         send_mail(
#             asunto,
#             cuerpo,
#             'talento@fabricadecodigo.dev',
#             destinatarios,
#             fail_silently=False,
#         )
#         direccion='/pedido_e/'+ str(id_pedido)
#         return redirect(direccion)



class FinalizarPedidoStaff(View):
    permission_required('permiso_empleado')
    def get(self,request):
        opciones_region = Region.objects.all().values_list('nombre', flat=True)
        opciones_comuna = Comuna.objects.all().values_list('nombre', flat=True)
        opciones_username = Cliente.objects.all()
        OPCIONES_REGION = tuple([(opcion, opcion) for opcion in opciones_region])
        OPCIONES_COMUNA = tuple([(opcion, opcion) for opcion in opciones_comuna] )
        OPCIONES_USERNAME = tuple([(opcion.user.username, opcion.user.username) for opcion in opciones_username] )
        print("STAFF")
        carrito = request.session.get('carrito')
        print("STAFF2")
        formulario = FormularioPedidoStaff()
        formulario.fields['comuna'].choices = OPCIONES_COMUNA
        formulario.fields['region'].choices = OPCIONES_REGION
        formulario.fields['cliente'].choices = OPCIONES_USERNAME
        template = 'finalizar_pedido_staff.html'
        context = {'formulario':formulario,'carrito':carrito}
        
        return render(request,template,context)
        
        
    # permission_required('permiso_empleado')  
    
    def post(self,request):
        formulario = FormularioPedidoStaff(request.POST)
         
       
        
          
        
        x = User.objects.get(username=formulario['cliente'].value())
        cliente = Cliente.objects.get(user_id= x.id)
        # x_user = User.objects.get(username=formulario['cliente'].value())
        staff = UsuarioStaff.objects.get(user_id=request.user.id) 
            
        carrito= Carrito(  
              cantidad_total= 0,
                precio_total=0,
                cliente = cliente,
                empleado = staff
      
                 )
        carrito.save()
        carrito_session = request.session.get('carrito')
        suma_precio=0
        for x in carrito_session:
                producto = Producto.objects.get(id=x['producto'])
                cantidad = x['cantidad']
                detalle = DetalleProductoSocilicitado(
                    producto =producto,
                    cantidad= cantidad,
                    valor_producto = producto.precio,
                    carrito = carrito
                 )
        detalle.save()
        suma_precio = suma_precio + (int(producto.precio) * int(cantidad))
        suma_cantidad= DetalleProductoSocilicitado.objects.filter(carrito_id = carrito.id).aggregate(total=Sum('cantidad'))
        carrito.cantidad_total = suma_cantidad['total']
        carrito.precio_total = suma_precio
        carrito.save()
        estado = EstadoPedido.objects.get(id=1)
        comuna = Comuna.objects.get(nombre=formulario['comuna'].value())
        region = Region.objects.get(nombre=formulario['region'].value())
        pedido = Pedido( 
                    fecha = formulario['fecha_entrega'].value(),
                    estado=estado,
                    calle_entrega=formulario['direccion'].value(),
                    comuna=comuna,
                    region=region,
                    carrito = carrito         
                    
                )        

        pedido.save()
        return redirect('/p_staff')
           













class FinalizarPedidoProd(View):
  
    def get(self,request):
        opciones_region = Region.objects.all().values_list('nombre', flat=True)
        opciones_comuna = Comuna.objects.all().values_list('nombre', flat=True)
        opciones_username = Cliente.objects.all()
        OPCIONES_REGION = tuple([(opcion, opcion) for opcion in opciones_region])
        OPCIONES_COMUNA = tuple([(opcion, opcion) for opcion in opciones_comuna] )
        OPCIONES_USERNAME = tuple([(opcion.user.username, opcion.user.username) for opcion in opciones_username] )
        print("STAFF")
        carrito = request.session.get('carrito')
        print("STAFF2")
        formulario = FormularioPedidoStaff()
        formulario.fields['comuna'].choices = OPCIONES_COMUNA
        formulario.fields['region'].choices = OPCIONES_REGION
        formulario.fields['cliente'].choices = OPCIONES_USERNAME
        template = 'finalizar_pedido_staff.html'
        context = {'formulario':formulario,'carrito':carrito}
        
        return render(request,template,context)
        
        
    
    
    def post(self,request):
        formulario = FormularioPedidoStaff(request.POST)
         
       
        
          
        
        x = User.objects.get(username=formulario['cliente'].value())
        cliente = Cliente.objects.get(user_id= x.id)
        # x_user = User.objects.get(username=formulario['cliente'].value())
        # staff = Productor.objects.get(user_id=request.user.id) 
            
        carrito= Carrito(  
              cantidad_total= 0,
                precio_total=0,
                cliente = cliente,
              
      
                 )
        carrito.save()
        carrito_session = request.session.get('carrito')
        suma_precio=0
        for x in carrito_session:
                producto = Producto.objects.get(id=x['producto'])
                cantidad = x['cantidad']
                detalle = DetalleProductoSocilicitado(
                    producto =producto,
                    cantidad= cantidad,
                    valor_producto = producto.precio,
                    carrito = carrito
                 )
        detalle.save()
        suma_precio = suma_precio + (int(producto.precio) * int(cantidad))
        suma_cantidad= DetalleProductoSocilicitado.objects.filter(carrito_id = carrito.id).aggregate(total=Sum('cantidad'))
        carrito.cantidad_total = suma_cantidad['total']
        carrito.precio_total = suma_precio
        carrito.save()
        estado = EstadoPedido.objects.get(id=1)
        comuna = Comuna.objects.get(nombre=formulario['comuna'].value())
        region = Region.objects.get(nombre=formulario['region'].value())
        pedido = Pedido( 
                    fecha = formulario['fecha_entrega'].value(),
                    estado=estado,
                    calle_entrega=formulario['direccion'].value(),
                    comuna=comuna,
                    region=region,
                    carrito = carrito         
                    
                )        

        pedido.save()
        return redirect('/p_prod')




def visualizar_pedidos(request,id):
    template="pedido.html"
    pedido = Pedido.objects.get(id=id)
    carrito = Carrito.objects.get(id=pedido.carrito_id)
    detalles = DetalleProductoSocilicitado.objects.filter(carrito_id = carrito.id)
    suma_precio=0
    for x in detalles:
        suma_precio = suma_precio + (x.producto.precio * x.cantidad)
        

    suma_cantidad= DetalleProductoSocilicitado.objects.filter(carrito_id = carrito.id).aggregate(total=Sum('cantidad'))
   
  
    context={'pedido':pedido,
              'carrito':carrito,
              'detalles':detalles,
                'suma_precio':suma_precio,
                'suma_cantidad':suma_cantidad['total'] 
             }
    return render(request,template,context)

permission_required('permiso_staff')
    
def visualizar_pedidos_e(request,id):
   
    opciones_estado = EstadoPedido.objects.all().values_list('nombre', flat=True)
    
    OPCIONES_ESTADO = tuple([(opcion, opcion) for opcion in opciones_estado])
    
    template="pedido_estado.html"
    pedido = Pedido.objects.get(id=id)
    carrito = Carrito.objects.get(id=pedido.carrito_id)
    detalles = DetalleProductoSocilicitado.objects.filter(carrito_id = carrito.id)
    suma_precio=0
    for x in detalles:
        suma_precio = suma_precio + (x.producto.precio * x.cantidad)
        

    suma_cantidad= DetalleProductoSocilicitado.objects.filter(carrito_id = carrito.id).aggregate(total=Sum('cantidad'))
   
    formulario_estado = FormularioEstado()
    formulario_estado.fields['estado'].choices = OPCIONES_ESTADO
    context={'pedido':pedido,
             'carrito':carrito,
             'detalles':detalles,
             'suma_precio':suma_precio,
             'suma_cantidad':suma_cantidad['total'] ,
             'formulario':formulario_estado    
             }
    return render(request,template,context)






def logout_view(request):

    print('logout')
    logout(request)
    return redirect('/')






permission_required('permiso_staff')

def registro_producto(request):

    if request.method == 'POST':
        
        form = FormularioRegistroProductoStaff(request.POST, request.FILES)
        
        imagen = request.FILES['archivo']
        producto = Producto(nombre =form['nombre'].value(),  precio =form['precio'].value(), descripcion = form['descripcion'].value() )
        producto.imagen_b = imagen.read()
        producto.imagen_f = imagen
        producto.save()
        return redirect('/hacer_pedido_staff/')

    else:

        form = FormularioRegistroProductoStaff()
      
        return render(request, 'registro_producto.html', {'form': form})




def registro_cliente(request):
    if request.method == 'POST':
        print("LLEGUE")
        formulario = FormularioRegistroCliente(request.POST)
               
        print("llegue")
        username = formulario['username'].value()
        nombre = formulario['nombre'].value()
        apellido = formulario['apellido'].value()
        email = formulario['email'].value()
        clave = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
       
        direccion = formulario['direccion'].value()
        telefono = formulario['telefono'].value()
        c_nombre = formulario['comuna'].value()
        r_nombre = formulario['region'].value()
        comuna = Comuna.objects.get(nombre = c_nombre)
        region = Region.objects.get(nombre = r_nombre)

  
            
        usuario = User(
                username=username,
                first_name=nombre,
                last_name=apellido,
                email=email)
        usuario.password = make_password(clave)
        usuario.save()
        
        cliente = Cliente()
        cliente.telefono = telefono
        cliente.comuna
        cliente.region
        cliente.identificador = 'u' + str(clave)
        cliente.user = usuario   
        cliente.direccion =direccion
        cliente.save()  
        grupo = Group.objects.get(name='clientes')
        usuario.groups.add(grupo)
        destinatarios=[email]
        asunto="clave"
        cuerpo = "TU CLAVE ES " + str(clave)
        send_mail(
            asunto,
            cuerpo,
            'talento@fabricadecodigo.dev',
            destinatarios,
            fail_silently=False,
        ) 
        return redirect("/login_view/")

    else:
        opciones_region = Region.objects.all().values_list('nombre', flat=True)
        opciones_comuna = Comuna.objects.all().values_list('nombre', flat=True)
        opciones_username = Cliente.objects.all()
        OPCIONES_REGION = tuple([(opcion, opcion) for opcion in opciones_region])
        OPCIONES_COMUNA = tuple([(opcion, opcion) for opcion in opciones_comuna] )
        OPCIONES_USERNAME = tuple([(opcion.user.username, opcion.user.username) for opcion in opciones_username] )
        formulario = FormularioRegistroCliente()
        formulario.fields['comuna'].choices = OPCIONES_COMUNA
        formulario.fields['region'].choices = OPCIONES_REGION
        return render(request, 'registro_cliente.html', context={'formulario': formulario})

permission_required('permiso_staff')
def modificar_estado_pedido(request,id_pedido):
    
    formulario = FormularioEstado(request.POST)

    nombre_estado = formulario['estado'].value()
    estado = EstadoPedido.objects.get(nombre=nombre_estado)
    pedido=Pedido.objects.get(id=id_pedido)
    pedido.estado = estado
    pedido.save()
        
    email = pedido.carrito.cliente.user.email
    print(email)
    destinatarios=[email]
    asunto = 'ESTADO DE TU PEDIDO'
    cuerpo = 'TU PEDIDO ESTA ' + nombre_estado
               
    send_mail(
            asunto,
            cuerpo,
            'talento@fabricadecodigo.dev',
            destinatarios,
            fail_silently=False,
        )
    direccion='/pedido_e/'+ str(id_pedido)
    return redirect(direccion)


def catalogo(request):
    productos= Producto.objects.all()
    return render(request, 'catalogo.html',{'productos':productos})