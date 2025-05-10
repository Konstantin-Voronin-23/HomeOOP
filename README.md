# ООП: Домашний проект по объекто-ориентированному программированию


# **Описание**

## Данный проект реализует работу над классами и объектами
### 


# **Установка**:

### Для работы приложения необходимо установить интерпретатор *poetry*:

```pip install --user poetry```

### Так же клонируйте репозиторий:

```git clone https://github.com/Konstantin-Voronin-23/HomeOOP.git```


# **Установка зависимостей**:

### Для работы проекта воспользуйтесь командами для установок зависимостей:

```
poetry add --group lint flake8
poetry add --group lint mypy
poetry add --group lint black
poetry add --group lint isort

poetry add --group dev pytest
poetry add --group dev pytest-cov
poetry add python-dotenv
poetry add requests
poetry add pandas
poetry add openpyxl
```
# **Реализация модулей**:

## 1. Модуль Product - модуль для класса Product:

<details>
<summary><b>❗ PRODUCT ❗</b></summary>

###  __init__ :
  - Метод для инициализации класса с аргументами name | description | price | quantity
### new_product:
  - Метод класса, принимает на вход параметры товара в словаре и возвращать созданный объект класса
### price:
  - Setter проверяет: в случае если цена равна или ниже нуля, выводит сообщение в консоль, так же предлагает пользователю подтвердить смену цены, если новая просто ниже актуальной 

</details>

## 2. Модуль Category - модуль для класса Category:


<details>
<summary><b>❗ CATEGORY ❗</b></summary>

###  __init__ :
  - Метод для инициализации класса с аргументами name | description | products
### add_product:
  - Метод для добавления товаров в категорию
### products:
  - Getter, возвращает строковое представление товаров

</details>

## 3. Модуль utils - модуль для вспомогательных функций:

<details>
<summary><b>❗ UTILS ❗</b></summary>

###  read_json_file :
      - Функция для чтения json файла
###  create_object_from_json:
      - Функция которая принимает Json файл и превращает категории в объекты

</details>

## 4. Модуль iterators - модуль для класса iterators:

<details>
<summary><b>❗ ITERATORS ❗</b></summary>

### __init__:
  - Инициализатор
### __iter__:
  - Итератор
### __next__:
  - Переход к следующему значение в итерации

</details>

# **Тестирование модулей**:

<details>
<summary><b>❗ МОДУЛЬ PRODUCT ❗</b></summary>

### test_product_init:
  - Проверка корректности инициализации продукта
### test_product_attributes_types:
  - Проверка типов атрибутов продукта
### test_new_product_creates_new_instance:
  - Тест создания нового продукта, когда такого продукта еще нет в списке
### test_new_product_updates_existing_product:
  - Тест обновления существующего продукта
### test_new_product_keeps_higher_price:
  - Тест что сохраняется более высокая цена при обновлении продукта
### test_price_getter:
  - Тест геттера цены
### test_price_setter_valid_price:
  - Тест сеттера цены с валидным значением
### test_price_setter_invalid_price:
  - Тест сеттера цены с невалидным значением (<= 0)
### test_price_setter_lower_price_rejected:
  - Тест отмены понижения цены
### test_price_setter_lower_price_accepted:
  - Тест подтверждения понижения цены
### test_new_product_with_empty_list:
  - Тест создания нового продукта при пустом списке
### test_product_str:
  - Тест метода __str__ класса Product
### test_product_add:
  - Тест метода __add__ класса Product

</details>

<details>
<summary><b>❗ МОДУЛЬ CATEGORY ❗</b></summary>

### test_category_init:
  - Проверка корректности инициализации категории
### test_category_with_products:
  - Проверка инициализации категории с продуктами
### test_total_categories_counter:
  - Проверка подсчета количества категорий
### test_product_counter_with_products:
  - Проверка подсчета количества продуктов
### test_product_counter_empty_category:
  - Проверка, что пустая категория не увеличивает счетчик продуктов
### test_add_product_valid:
  - Тест добавления корректного продукта в категорию
### test_add_product_invalid_type:
  - Тест попытки добавления объекта не типа Product
### test_products_property:
  - Тест свойства products, возвращающего строковое представление
### test_products_property_empty:
  - Тест свойства products с пустым списком продуктов
### test_category_str:
  - Тест метода __str__ класса Category
### test_category_add_product:
  - Тест добавления продукта и проверка __str__
### test_iterator_returns_all_products:
  - Проверка на то, что корректно возвращаются все продукты
### test_iterator_stops_after_last_product:
  - Проверка, что после последнего продукта итератор останавливается
### test_empty_category:
  - Проверка пустого знеачения
### test_iterator_is_iterable:
  - Проверяет, что объект CategoryIterator является корректным итерируемым объектом
### test_category_iter_returns_iterator:
  - Проверяет, что возвращается итератор
### test_products_property_returns_list:
  - Тест, проверяет что возвращается список продуктов

</details>

<details>
<summary><b>❗ МОДУЛЬ UTILS ❗</b></summary>

### test_read_valid_json:
  - Проверка чтения корректного JSON файла
### test_read_nonexistent_file:
  - Проверка обработки отсутствующего файла
### test_create_objects:
  - Проверка создания объектов из JSON
### test_empty_data:
  - Проверка обработки пустых данных
### test_invalid_data_structure:
  - Проверка обработки некорректной структуры данных
### test_json_decode_error:
  - Проверка обработки некорректного JSON

</details>

<details>
<summary><b>❗ МОДУЛЬ ITERATORS ❗</b></summary>

### test_iterator_returns_all_products:
  - Проверка на то, что корректно возвращаются все продукты
### test_iterator_stops_after_last_product:
  - Проверка, что после последнего продукта итератор останавливается
### test_empty_category:
  - Проверка пустого знеачения
### test_iterator_is_iterable:
  - Проверяет, что объект CategoryIterator является корректным итерируемым объектом

</details>

# Покрытие тестами 99%

# Документация

# Лицензия

## - Этот проект лицензирован по [лицензии MIT](LICENSE).
