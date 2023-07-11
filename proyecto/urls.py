
from django.contrib import admin
from django.urls import path
from app1.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home,name="HOME"),
    path('', home,name="HOME"),
    
     path('login_view/', loginUsuario,name="LOGIN"),

    path('p_staff/', perfil_staff,name="P_STAFF"),

     path('p_prod/', perfil_productor,name="P_PROD"),

     path('p_cliente/', perfil_cliente,name="CLIENTE"),
     
     path('ag_pro_staff/', funcion_para_guardar_staff,name="CLIENTE"),
path('ag_pro_cliente/', funcion_para_guardar_cliente,name="CLIENTE"),
  path('finalizar_pedido_staff/',FinalizarPedidoStaff.as_view(),name='FINALIZAR_PEDIDO'),
    path('finalizar_pedido_cliente/',FinalizarPedidoCliente.as_view(),name='FINALIZAR_PEDIDO'),

    # path('logout/', login_usuario,name="LOGIN"),
    
    # path('reg_prod_staff/', registro_producto_staff,name="REG_PROD_STAFF"),
    # path('reg_prod_prod/', registro_producto_pro,name="REG_PROD_PROD"),
    
   
    # path('reg_cliente/', login_usuario,name="REG_CLIENTE"),

     path('hacer_pedido_staff/', HacerPedidoStaff.as_view(),name="H_P_STAFF"),
    path('hacer_pedido_cliente/', HacerPedidoCliente.as_view(),name="H_P_CLIENTE"),
     path('hacer_pedido_staff/', HacerPedidoStaff.as_view(),name="H_P_STAFF"),
    path('hacer_pedido_prod/', HacerPedidoProd.as_view(),name="H_P_CLIENTE"),
    # path('hacer_pedi_productor/', login_usuario,name="H_P_STAFF"),
     path('limpiar_carrito_staff/', limpiar_carrito_staff,name="LIMPIAR_CARRITO_STAFF"),
    path('limpiar_carrito_cliente/', limpiar_carrito_cliente,name="LIMPIAR_CARRITO_CLIENTE"),
     path('registro_producto/', registro_producto,name='registro_producto'),
        path('registro_cliente/', registro_cliente,name='registro_producto'),
           path('finalizar_pedido_staff/',FinalizarPedidoStaff.as_view(),name='FINALIZAR_PEDIDO'),
    path('finalizar_pedido_cliente/',FinalizarPedidoCliente.as_view(),name='FINALIZAR_PEDIDO'),
     path('finalizar_pedido_prod/',FinalizarPedidoProd.as_view(),name='FINALIZAR_PEDIDO'),
    path('pedido/<int:id>', visualizar_pedidos, name='PEDIDO'),
    path('pedido_e/<int:id>', visualizar_pedidos_e, name='PEDIDO_CON_ESTADO'),
    path('modificar_estado/<int:id_pedido>', modificar_estado_pedido,name="LIMPIAR_CARRITO"),
    path('logout_view/', logout_view,name='logout_view'),
    path('catalogo/', catalogo,name='logout_view'),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)