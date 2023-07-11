from django import forms



class FormularioRegistroCliente(forms.Form):
        username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        rut = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        
      
        telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        region = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class':'form-control'}))

        comuna = forms.ChoiceField(
        choices=[],
        widget=forms.Select( attrs={'class':'form-control'}))




       
class FormularioProductor(forms.Form):
        username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        rut = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
      
      
        telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
       


class LoginUsuario(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese su username','class':'form-control'}),max_length=50,required=True,label='Nombre de usuario')
    clave = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña','class':'form-control'}), max_length=20,label='Password',required=True,error_messages={'required':'La contraseña es obligatoria'})







class FormularioRegistroProductoStaff(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    precio = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    stock = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    archivo = forms.FileField(label='Selecciona un archivo')




class FormularioRegistroProductoProductor(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    precio = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    stock = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    archivo = forms.FileField(label='Selecciona un archivo')








class FormularioEstado(forms.Form):

        
        
        estado = forms.ChoiceField(
        choices=[],
        widget=forms.Select( attrs={'class':'form-control'}))



class FormularioAgregarProductoCarrito(forms.Form):
       producto_id = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Ingrese el precio','class':'form-control'}))
       cantidad_id = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Ingrese el precio','class':'form-control','style':'width:50%;'}))







class FormularioPedidoStaff(forms.Form):
        direccion=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese la direccion del pedido','class':'form-control'}))
        fecha_entrega = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class':'form-control'}))
        cliente = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Ingrese el email para identificar el cliente','class':'form-control'}))
        
        region = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class':'form-control'}))

        comuna = forms.ChoiceField(
        choices=[],
        widget=forms.Select( attrs={'class':'form-control'}))

        cliente = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class':'form-control'}))



class FormularioPedidoCliente(forms.Form):
        fecha_entrega = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class':'form-control'}))
        
        direccion=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese la direccion del pedido','class':'form-control'}))
               
        region = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class':'form-control'}))

        comuna = forms.ChoiceField(
        choices=[],
        widget=forms.Select( attrs={'class':'form-control'}))



class FormularioPedidoProveedor(forms.Form):
        fecha_entrega = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class':'form-control'}))
        
        direccion=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese la direccion del pedido','class':'form-control'}))
               
        region = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class':'form-control'}))

        comuna = forms.ChoiceField(
        choices=[],
        widget=forms.Select( attrs={'class':'form-control'}))



