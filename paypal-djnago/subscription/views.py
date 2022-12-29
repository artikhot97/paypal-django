import requests
from rest_framework import status
from rest_framework.response import Response
from django.contrib import messages
from integration.utils import paypal_token, ResponseInfo, return_response
from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView)


token = paypal_token()

headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+token,
        }
URL = 'https://api-m.sandbox.paypal.com/v1/'


class ProductsListAPIView(ListAPIView):
    """
    Lists products.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(ProductsListAPIView, self).__init__(**kwargs)
    def get(self, request, *args, **kwargs):
        try:
            product_url = URL + 'catalogs/products'
            response = requests.get(product_url, headers=headers)
            self.response_format = return_response(
                response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
            return Response(self.response_format)
        except Exception as e:
            return Response(self.response_format)

class CreateProductAPIView(ListAPIView):
    """
    Creates a product.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(CreateProductAPIView, self).__init__(**kwargs)
    def post(self, request, *args, **kwargs):
        try:
            product_url = URL + 'catalogs/products'
            response = requests.post(product_url, headers=headers, json=request.data)
            print(response)
            self.response_format = return_response(
                response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
            return Response(self.response_format)
        except Exception as e:
            return Response(self.response_format)


class UpdateProductAPIView(CreateAPIView):
    """
    Updates a product, by ID
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(UpdateProductAPIView, self).__init__(**kwargs)
    def post(self, request, *args, **kwargs):
        try:
            product_url = URL + 'catalogs/products/'+self.kwargs['product_id']
            response = requests.patch(product_url, headers=headers, json=request.data)
            self.response_format = return_response(
                response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
            return Response(self.response_format)
        except Exception as e:
            return Response(self.response_format)

class ProductDetailAPIView(ListAPIView):
    """
    Lists billing plans.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(ProductDetailAPIView, self).__init__(**kwargs)
    def get(self, request, *args, **kwargs):
        try:
            plan_url = URL + 'catalogs/products/'+self.kwargs['product_id']
            response = requests.get(plan_url, headers=headers)
            self.response_format = return_response(
                response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
            return Response(self.response_format)
        except Exception as e:
            return Response(self.response_format)


class PlanListAPIView(ListAPIView):
    """
    Lists billing plans.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(PlanListAPIView, self).__init__(**kwargs)
    def get(self, request, *args, **kwargs):
        try:
            plan_url = URL + 'billing/plans'
            response = requests.get(plan_url, headers=headers)
            list_response = response.json()
            output_dict = [x for x in list_response["plans"] if x['status'] != 'INACTIVE']
            self.response_format = return_response(
                output_dict, None, status.HTTP_200_OK, messages.success(request,'SUCCESS'))
            return Response(self.response_format)
        except Exception as e:
            print(e)
            return Response(self.response_format)


class CreatePlanAPIView(CreateAPIView):
    """
    Creates a plan that defines pricing and billing cycle details for subscriptions.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(CreatePlanAPIView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        plan_url = URL + 'billing/plans'
        response = requests.post(plan_url, headers=headers, json=request.data)

        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)

class UpdatePlanAPIView(CreateAPIView):
    """
    Creates a plan that defines pricing and billing cycle details for subscriptions.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(UpdatePlanAPIView, self).__init__(**kwargs)
    def post(self, request, *args, **kwargs):
        try:
            plan_url = URL + 'billing/plans/'+ self.kwargs["plan_id"]
            response = requests.patch(plan_url, headers=headers, json=request.data)

            self.response_format = return_response(
                response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
            return Response(self.response_format)
        except Exception as e:
            return Response(self.response_format)

class PlanDetailAPIView(ListAPIView):
    """
    Creates a plan that defines pricing and billing cycle details for subscriptions.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(PlanDetailAPIView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):

        plan_url = URL + 'billing/plans/'+self.kwargs["plan_id"]
        response = requests.get(plan_url, headers=headers)

        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)


class ActivePlanAPIView(ListAPIView):
    """
    Creates a plan that defines pricing and billing cycle details for subscriptions.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(ActivePlanAPIView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        try:
            plan_url = URL + 'billing/plans/'+self.kwargs["plan_id"]+'/activate'
            response = requests.post(plan_url, headers=headers)

            self.response_format = return_response(
                response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
            return Response(self.response_format)
        except Exception as e:
            return Response(self.response_format)

class DeactivatePlanAPIView(ListAPIView):
    """
    Creates a plan that defines pricing and billing cycle details for subscriptions.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(DeactivatePlanAPIView, self).__init__(**kwargs)
    def get(self, request, *args, **kwargs):
        try:
            plan_url = URL + 'billing/plans/'+self.kwargs["plan_id"]+'/deactivate'
            response = requests.post(plan_url, headers=headers)

            self.response_format = return_response(
                response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
            return Response(self.response_format)
        except Exception as e:
            return Response(self.response_format)

class UpdatePriceAPIView(CreateAPIView):
    """
    Updates pricing for a plan.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(UpdatePriceAPIView, self).__init__(**kwargs)
    def post(self, request, *args, **kwargs):
        plan_url = URL + 'billing/plans/'+self.kwargs["plan_id"]+'/update-pricing-schemes'
        response = requests.post(plan_url, headers=headers, json=request.data)

        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)

class CreateSubscriptionAPIView(CreateAPIView):
    """
    Creates a subscription.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(CreateSubscriptionAPIView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        subscription_url = URL + 'billing/subscriptions'
        response = requests.post(subscription_url, headers=headers, json=request.data)
        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)

class UpdateSubscriptionAPIView(CreateAPIView):
    """
    Creates a plan that defines pricing and billing cycle details for subscriptions.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(UpdateSubscriptionAPIView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        subscription_url = URL + 'billing/subscriptions/' + self.kwargs["subscription_id"]
        response = requests.patch(subscription_url, headers=headers, json=request.data)

        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)


class SubscriptionDetailAPIView(CreateAPIView):
    """
    Shows details for a subscription, by ID.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(SubscriptionDetailAPIView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        subscription = URL + 'billing/subscriptions/'+self.kwargs["subscription_id"]
        response = requests.get(subscription, headers=headers)

        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)


class ActivateSubscriptionAPIView(CreateAPIView):
    """
    Activates the subscription.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(ActivateSubscriptionAPIView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        subscription = URL + 'billing/subscriptions/'+self.kwargs["subscription_id"]+'/activate'
        response = requests.post(subscription, headers=headers, json=request.data)

        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)


class CancelsSubscriptionAPIView(CreateAPIView):
    """
    Cancels the subscription.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(CancelsSubscriptionAPIView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        subscription = URL + 'billing/subscriptions/'+self.kwargs["subscription_id"]+'/cancel'
        response = requests.post(subscription, headers=headers, json=request.data)

        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)


class AuthorizePaymentSubscriptionAPIView(CreateAPIView):
    """
    Captures an authorized payment from the subscriber on the subscription.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(AuthorizePaymentSubscriptionAPIView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        subscription = URL + 'billing/subscriptions/'+self.kwargs["subscription_id"]+'/capture'
        response = requests.post(subscription, headers=headers, json=request.data)

        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)


class SuspendSubscriptionAPIView(CreateAPIView):
    """
    Suspends the subscription.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(SuspendSubscriptionAPIView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        try:
            subscription = URL + 'billing/subscriptions/'+self.kwargs["subscription_id"]+'/suspend'
            response = requests.post(subscription, headers=headers, json=request.data)

            self.response_format = return_response(
                response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
            return Response(self.response_format)

        except Exception as e:
            return Response(self.response_format)


class SubscriptionTransactionsAPIView(CreateAPIView):
    """
    Suspends the subscription.
    """
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(SubscriptionTransactionsAPIView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        subscription = URL + 'billing/subscriptions/'+self.kwargs["subscription_id"]+'/transactions?start_time=2018-01-21T07:50:20.940Z&end_time=2022-12-28T07:50:20.940Z'
        response = requests.get(subscription, headers=headers)

        self.response_format = return_response(
            response.json(), None, status.HTTP_200_OK, messages.SUCCESS)
        return Response(self.response_format)
