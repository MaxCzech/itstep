from django.urls import include, path, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    # path('users/', include('django.contrib.auth.urls')),
    # path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),

    path('footer/', include('footer.urls')),

    # re_path(r'^account/', include('account.urls')),

    path('', include('shop.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Subscriptions shop"
admin.site.index_title = "E-shop administration"
