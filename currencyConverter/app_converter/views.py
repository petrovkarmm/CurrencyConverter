from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import CurrencyRate


@require_GET
def get_currency_rate(request):
    """
    Обработчик GET запроса. Получение в запросе валют и значения.
    :param request:
    :return: JsonResponse result with convert rate or 404 if error
    """
    from_currency = request.GET.get('from')
    to_currency = request.GET.get('to')
    value = float(request.GET.get('value', 1))

    if from_currency == to_currency:
        # При конвертировании одинаковых валют был exception, лучше провести проверку.
        return JsonResponse({'result': value})

    try:
        rate = CurrencyRate.objects.get(from_currency=from_currency, to_currency=to_currency).rate
        # Получение онли rate. Дальше просто математика и возврат.
        result = value * rate
        return JsonResponse({'result': result})
    except CurrencyRate.DoesNotExist:
        return JsonResponse({'error': 'Currency rate not found'}, status=404)
