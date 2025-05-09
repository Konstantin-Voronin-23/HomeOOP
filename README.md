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

  ### - __init__ :
      - Метод для инициализации класса с аргументами name | description | price | quantity

</details>

## 2. Модуль Category - модуль для класса Category:


<details>
<summary><b>❗ CATEGORY ❗</b></summary>

### - __init__ :
      - Метод для инициализации класса с аргументами name | description | products

</details>

## 3. Модуль utils - модуль для вспомогательных функций:

<details>
<summary><b>❗ UTILS ❗</b></summary>

  ### - read_json_file :
      - Функция для чтения json файла
  ### - create_object_from_json:
      - Функция которая принимает Json файл и превращает категории в объекты

</details>


# **Тестирование модулей**:

<details>
<summary><b>❗ МОДУЛЬ PRODUCT ❗</b></summary>

### test_product_init:
  - Проверка корректности инициализации продукта
### test_product_attributes_types:
  - Проверка типов атрибутов продукта

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

# Покрытие тестами 100%

# Документация

# Лицензия

## - Этот проект лицензирован по [лицензии MIT](LICENSE).
