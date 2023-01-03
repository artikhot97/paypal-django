from django.conf.urls import url
from .views import (PlanListAPIView,
                     CreatePlanAPIView,UpdatePlanAPIView,PlanDetailAPIView,ActivePlanAPIView,DeactivatePlanAPIView,
                     UpdatePriceAPIView,CreateSubscriptionAPIView, UpdateSubscriptionAPIView,SubscriptionDetailAPIView,
                     ActivateSubscriptionAPIView,CancelsSubscriptionAPIView,AuthorizePaymentSubscriptionAPIView,
                     SuspendSubscriptionAPIView, SubscriptionTransactionsAPIView, ProductsListAPIView,
                     CreateProductAPIView,UpdateProductAPIView , ProductDetailAPIView,CreateWebhookAPIView,UpdateSubscriptionWebhookAPIView,
                    ListSubscriptionWebhookAPIView,)

urlpatterns = [
    #Product
    url('productsList', ProductsListAPIView.as_view(), name='product-list'),
    url('createProduct', CreateProductAPIView.as_view(), name='create-product'),
    url('updateProduct/(?P<product_id>.+)/', UpdateProductAPIView.as_view(), name='update-product'),
    url('productDetail/(?P<product_id>.+)/', ProductDetailAPIView.as_view(), name='product-detail'),

    #Suscritions
    url('listPlan', PlanListAPIView.as_view(), name='plan-list'),
    url('createPlan', CreatePlanAPIView.as_view(), name='create-plan'),
    url('updatePlan/(?P<plan_id>.+)/', UpdatePlanAPIView.as_view(), name='update-plan'),
    url('planDetail/(?P<plan_id>.+)/', PlanDetailAPIView.as_view(), name='plan-detail'),
    url('activePlan/(?P<plan_id>.+)/', ActivePlanAPIView.as_view(), name='active-plan'),
    url('deactivatePlan/(?P<plan_id>.+)/', DeactivatePlanAPIView.as_view(), name='deactive-plan'),
    url('updatePrice/(?P<plan_id>.+)/', UpdatePriceAPIView.as_view(), name='update-price'),
    url('createSubscription', CreateSubscriptionAPIView.as_view(), name='create-subscription'),
    url('updateSubscription/(?P<subscription_id>.+)/', UpdateSubscriptionAPIView.as_view(), name='update-subscription'),
    url('subscriptionDetail/(?P<subscription_id>.+)/', SubscriptionDetailAPIView.as_view(), name='subscription-detail'),
    url('activateSubscription/(?P<subscription_id>.+)/', ActivateSubscriptionAPIView.as_view(), name='activate-subscription'),
    url('cancelsSubscription/(?P<subscription_id>.+)/', CancelsSubscriptionAPIView.as_view(), name='cancels-subscription'),
    url('authorizePaymentSubscription/(?P<subscription_id>.+)/', AuthorizePaymentSubscriptionAPIView.as_view(), name='authorize-payment-subscription'),
    url('suspendSubscription/(?P<subscription_id>.+)/', SuspendSubscriptionAPIView.as_view(), name='suspend-subscription-subscription'),
    url('listOfSubscriptionTransactions/(?P<subscription_id>.+)/', SubscriptionTransactionsAPIView.as_view(), name='suspend-subscription-subscription'),
  
    # Webhook
    url('createWebhook', CreateWebhookAPIView.as_view(), name='create-webhook'),
    url('updateSubscriptionWebhook', UpdateSubscriptionWebhookAPIView.as_view(), name='update-webhook'),
    url('listSubscriptionWebhook', ListSubscriptionWebhookAPIView.as_view(), name='list-webhook'),
]
