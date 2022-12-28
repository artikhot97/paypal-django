from django.conf.urls import url
from .views import ( CaptureOrderAPIView, CreateOrderAPIView, GetOrderDetailAPIView, AuthorizePaymentOrderAPIView,
                     UpdateOrderAPIView, ConfirmPaymentOrderAPIView, WebProfilesAPIView,)

urlpatterns = [
    # url('', views.home, name='home'),
    # url('paypal-return', views.paypal_return, name='paypal_return'),
    # url('paypal-cancel', views.paypal_cancel, name='paypal_cancel'),
    # Order API url
    url('createOrder',CreateOrderAPIView.as_view(), name='ordercreate'),
    url('getOrderDetail/(?P<order_id>.+)/', GetOrderDetailAPIView.as_view(), name='getorder'),
    url('confirmOrder/(?P<order_id>.+)/', ConfirmPaymentOrderAPIView.as_view(), name='confirm-order'),
    url('captureOrder/(?P<order_id>.+)/', CaptureOrderAPIView.as_view(), name='captureorder'),
    url('updateOrder/(?P<order_id>.+)/', UpdateOrderAPIView.as_view(), name='update-order'),
    url('authorizePaymentOrder/(?P<order_id>.+)/', AuthorizePaymentOrderAPIView.as_view(), name='authorize-payment'),

    # Payment Experience
    url('webProfiles', WebProfilesAPIView.as_view(), name='web-profile'),
]