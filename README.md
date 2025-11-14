# annihilation_gun_backend
Бэкэнд и API на Django REST Framework для OCR парсера инвойсов.

# Set-up:
1. Установите зависимости:


        pip install -r requirements.txt

3. Запустите сервер локально:


       python ./manage.py runserver

Порт по умолчанию 8000.

# Usage:

Для загрузки файлов используйте POST запрос на URL <hostname>/api/pdf/upload/ формата form-data в теле запроса с ключем original_file:
Пример запроса на Python:

    import requests

    API_URL = "http://localhost:8000/api/pdf/upload/"  
    PDF_PATH = "path\\to\\file.pdf"

В ответе на запрос в поле document_id будет представлен UUID вашего запроса. Используя GET запросы на URL /api/pdf/result/<document_id> и /api/pdf/status/<document_id> вы можете получить спаршенный JSON и статус реквеста соответственно.

Админская панель доступна по URL /admin/. Дефолтные креды: admin/admin. Для создания суперюзера используйте:

    python ./manage.py createsuperuser
