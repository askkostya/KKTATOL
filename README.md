Скрипт для мониторинга ККТ Атол

Скрипт для Zabbix получает от ККТ следующие данные

Если ККТ подключена локально необходимо передать один параметр

1 - Получить заводской номер ККТ

2 - РН ККТ

3 - Серийный номер ФН4- Сколько осталось дней до окончания ФН

4 - Осталось дней до окончания ФН

5 - Возраст в днях первого не отправленного документа в ФН

6 - Модель ККТ

7 - Версия прошивки


Для подключения к ККТ по сети необходимо передать три параметра

1 - Данные которые хотим получить (описание выше)

2 - IP адрес

3 - IP порт 


Обновление
Добавлена возможность подключения к кассе по TCP IP (если касса подключена не локально)
Для подключения к кассе по TCP IP необходимо передать 3 параметра

1 - какие данные получаем

2 - IP адрес

3 - Порт (по умолчанию 5555)


Работа скрипта проверялась на версии ДТО 10.0.8.0 и прошивке 5.7.10
При локальном подключении необходимо чтобы кассове ПО временно захватывало устройство
Для ПО Фронтол необходимо установить флаг _Временно захватывать устройство_
