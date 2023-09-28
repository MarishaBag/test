# Тестовое задание Back-end разработчик

## Технические требования
Версии новее указанных также подойдут
- [X]  Python 3.7 
- [X] pip 23.2.1
- [X] SQLAlchemy 2.0.21
- [X] MySQL
- [X] mysql-connector-python 8.0.33
- [X] mysql workbench 8.0

## Запуск
Создать новое MySQL соединение в MySQL Workbench, нажав на значок "+".

![msql-connection](https://github.com/MarishaBag/test/assets/145065517/5925c70e-8245-4979-b63e-0ba588c5222a)

Заполните Connection name и нажмите "ok".

![connection name](https://github.com/MarishaBag/test/assets/145065517/6837fbdf-65ed-4068-95ac-ed0c74af3350)

В открывшемся окне в разделе "SCHEMAS" правой кнопкой мыши выбрать "Create Schema...", выбрать кодировку utf-8, дать название новой базе данных и создать ее.

В данной строчке кода изменить данные по следующей форме:

```python
engine = create_engine("mysql+mysqlconnector://<имя_пользователя>:<пароль_от_MySQL_Workbench>@localhost/<название_базы_данных>", echo=True)
```
```python
engine = create_engine("mysql+mysqlconnector://root:password@localhost/test", echo=True)
```

После запуска программы вы увидите созданные таблицы в MySQL workbench.

![egergwege](https://github.com/MarishaBag/test/assets/145065517/14f0ad6e-41da-4d54-8631-5fec7b684eee)
