#  Сервис "Конвертер валют" в стиле REST-API.

## Пример использования:

### Получение результата происходит путем добавления параметров в GET запрос.

Пример конвертирования 100 рублей в доллар.

http://localhost:8080/api/rates/?from=RUB&to=USD&value=100

Ответ:

{
	"result": 1.0363
}

## Проверка ввода:

- Неверный параметр переданный в from:

  - {
	"error": "Wrong param in GET request"
    }

- Неверный параметр переданный в to:

  - {
	"error": "Wrong param in GET request"
    }

- Неверный параметр переданный в value:

  - {
	"error": "Wrong param in GET request"
    }

- Переданы одинаковые параметры to и from:

  - {
	"error": "Error. You cant convert current currency on same currency"
    }
