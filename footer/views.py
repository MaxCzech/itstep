from django.shortcuts import render, redirect


def shipping(request):
    return render(request, 'footer/shipping.html')


def gdrp(request):
    return render(request, 'footer/gdrp.html')


def terms(request):
    return render(request, 'footer/terms.html')


def support(request):
    return render(request, 'footer/support.html')


def payment_options(request):
    return render(request, 'footer/payment_options.html')
