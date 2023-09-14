from django.http import JsonResponse
from django.views.decorators.http import require_GET
from APILayer.fixer_api import currency_convert


@require_GET
def get_currency_rate(request):
    """
    Обработчик GET запроса. Получение в запросе валют и значения.
    :param request:
    :return: JsonResponse result with convert rate or error
    """
    current_currency = request.GET.get('from')
    to_currency = request.GET.get('to')
    amount = request.GET.get('value', 1)

    if current_currency == to_currency:
        # При конвертировании одинаковых валют возврат предупреждения.
        return JsonResponse({'error': 'Error. You cant convert current currency on same currency'})

    # Вызов функции APILayer.fixer_apy currency_convert
    value = currency_convert(current_currency=current_currency, to_currency=to_currency, amount=amount)

    if not value:
        return JsonResponse({'error': 'Wrong param in GET request'})

    return JsonResponse({'result': value})
