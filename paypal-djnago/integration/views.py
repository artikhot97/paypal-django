import requests
import uuid
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.contrib import messages
from .utils import paypal_token, ResponseInfo, return_response
from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView)

def home(request):
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '13.00',
        'item_name': 'Product 1',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url':f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal_return")}',
        'cancel_return': f'http://{host}{reverse("paypal_cancel")}'
    }

    form= PayPalPaymentsForm(initial=paypal_dict)
    context = {'form': form}
    print(context)
    return render(request, 'home.html', context)

def paypal_return(request):
    messages.sucess(request, "You have successfully completed payment.")
    return redirect('home')

def paypal_cancel(request):
    messages.error(request, "You order has been cancelled.")
    return redirect('home')

token = paypal_token()
headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+token
        }
URL = 'https://api-m.sandbox.paypal.com/v2/'

class CreateOrderAPIView(CreateAPIView):
    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(CreateOrderAPIView, self).__init__(**kwargs)
    def post(self, request):
        json_data = request.data
        response = requests.post(URL+'checkout/orders', headers=headers, json=json_data)
        # linkForPayment = response.json()['links'][1]['href']
        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)

class UpdateOrderAPIView(UpdateAPIView):
    """
    capture order aims to check whether the user has authorized payments.
    """
    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(UpdateOrderAPIView, self).__init__(**kwargs)
    def post(self, request, *args, **kwargs):
        capture_url = URL+ 'checkout/orders/'+ self.kwargs["order_id"]
        response = requests.patch(capture_url, headers=headers, json=request.data)

        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)
class GetOrderDetailAPIView(RetrieveAPIView):
    """
    Show Order details from id
    """
    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(GetOrderDetailAPIView, self).__init__(**kwargs)
    def get(self, request, *args, **kwargs):
        order_url = URL+'checkout/orders/'+ self.kwargs["order_id"]
        try:
            response = requests.get(order_url, headers=headers)
            self.response_format = return_response(
                response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
            return Response(self.response_format)

        except Exception as e:
            return Response(self.response_format)

class ConfirmPaymentOrderAPIView(ListAPIView):
    """
    Payer confirms their intent to pay for the the Order with the given payment source.
    """
    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(ConfirmPaymentOrderAPIView, self).__init__(**kwargs)
    def post(self, request, *args, **kwargs):
        confirm_url = URL+ 'checkout/orders/'+ self.kwargs["order_id"] +'/confirm-payment-source'
        response = requests.post(confirm_url, headers=headers, json=request.data)

        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)

class AuthorizePaymentOrderAPIView(CreateAPIView):
    """
    capture order aims to check whether the user has authorized payments.
    """
    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(AuthorizePaymentOrderAPIView, self).__init__(**kwargs)
    def get(self, request, *args, **kwargs):
        capture_url = URL+ 'checkout/orders/'+ self.kwargs["order_id"] +'/authorize'
        response = requests.post(capture_url, headers=headers)

        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)

class CaptureOrderAPIView(CreateAPIView):
    """
    capture order aims to check whether the user has authorized payments.
    """
    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(CaptureOrderAPIView, self).__init__(**kwargs)
    def get(self, request, *args, **kwargs):
        capture_url = URL+ 'checkout/orders/'+ self.kwargs["order_id"] +'/capture'
        response = requests.post(capture_url, headers=headers)

        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)


class WebProfilesAPIView(CreateAPIView):
    """
    Creates a web experience profile. In the JSON request body, specify the profile name and details.
    """
    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(WebProfilesAPIView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):

        web_profile = URL + 'customer/partner-referrals'
        response = requests.post(web_profile, headers=headers, json=request.data)

        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)
