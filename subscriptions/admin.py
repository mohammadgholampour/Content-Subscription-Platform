from django.contrib import admin
from .models import SubscriptionPlan, Content, UserSubscription, Invoice

admin.site.register(SubscriptionPlan)
admin.site.register(Content)
admin.site.register(UserSubscription)
admin.site.register(Invoice)
