from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone  # اضافه کردن این خط برای استفاده از timezone
from .models import SubscriptionPlan, Content, UserSubscription


def home(request):
    return render(request, 'subscriptions/home.html')


def subscription_plans(request):
    plans = SubscriptionPlan.objects.all()
    return render(request, 'subscriptions/plans.html', {'plans': plans})

@login_required
def content_list(request):
    user_subscription = UserSubscription.objects.filter(user=request.user).first()
    if not user_subscription:
        return redirect('subscription_plans')

    if user_subscription.end_date < timezone.now():
        return redirect('subscription_plans')

    content = Content.objects.filter(is_premium=False)
    if user_subscription:
        content = Content.objects.all()

    return render(request, 'subscriptions/content_list.html', {'content': content})
