from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from django.urls import reverse

from db.models import PromoCode


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    fields = ('code', 'discount_percentage', 'valid_from', 'valid_to', 'is_active')
    readonly_fields = ('code',)
    list_display = ('code', 'discount_percentage', 'valid_from', 'valid_to', 'is_active')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('generate_code/', self.admin_site.admin_view(self.generate_code), name='generate_code'),
        ]
        return custom_urls + urls

    def generate_code(self, request):
        # Генерация нового кода
        new_code = PromoCode()
        new_code.save()  # Сохраняем новый объект, чтобы сгенерировать код

        # Перенаправляем обратно на страницу редактирования нового промокода
        return HttpResponseRedirect(reverse('admin:appname_promocode_change', args=[new_code.id]))

    def response_change(self, request, obj):
        if "_generate_code" in request.POST:
            obj.save()  # Сохраняем объект, чтобы сгенерировать новый код
            self.message_user(request, "Промокод успешно сгенерирован!")
            return HttpResponseRedirect(request.path_info)
        return super().response_change(request, obj)
