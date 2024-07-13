# Финальный проект Yandex Практикум 18 коворта.

## Задание 1 
Нужно проверить, отображается ли созданный заказ в базе данных.<br>
Необходимо поключиться к серверу по ssh и выполгнить sql запрос:<br>

SELECT c.login,<br>
COUNT(o.id) AS "DN" <br>
FROM "Couriers" AS c JOIN "Orders" AS o ON c.id = o."courierId" <br>
WHERE o."inDelivery" = true <br>
GROUP BY c.login;<br>

## 2е задание
При тесте статуса заказов нужно убедиться, что в базе данных они записываются корректно.<br>
Для этого необходимо поключиться к серверу по ssh и выполгнить sql запрос:<br>

SELECT track, <br>
CASE <br>
WHEN finished = true THEN 2 <br>
WHEN cancelled = true THEN -1 <br>
WHEN "inDelivery" = true THEN 1 <br>
ELSE 0<br>
END AS status <br>
FROM "Orders";<br>

## Автоматизация теста к API
 1. Для запуска скрипта автоматического тестирования необходимо клонировать репозиторий к себе на ПК.
 2. Зайти в папку с проектом и выполнить в консоле комманду "pip install -r requirements.txt" для установки зависимостей
 3. Поменять в файле конфигурации "configuration.py" значениее переменной "URL_BASE" на актуальный.
 4. В окне консоли запустить команду "pytest"

