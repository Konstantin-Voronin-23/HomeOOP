import pytest

from src.utils import create_object_from_json, read_json_file


class TestReadJsonFile:
    """Тесты для функции чтения JSON файла"""

    def test_read_valid_json(self, temp_json_file):
        """Проверка чтения корректного JSON файла"""
        result = read_json_file(temp_json_file)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]["name"] == "Электроника"
        assert len(result[0]["products"]) == 2

    def test_read_nonexistent_file(self):
        """Проверка обработки отсутствующего файла"""
        result = read_json_file("nonexistent.json")
        assert result == []


class TestCreateObjectFromJson:
    """Тесты для функции создания объектов из JSON"""

    def test_create_objects(self, sample_data):
        """Проверка создания объектов из JSON"""
        result = create_object_from_json(sample_data)

        assert len(result[0].products) == 2

    def test_empty_data(self):
        """Проверка обработки пустых данных"""
        result = create_object_from_json([])
        assert result == []

    def test_invalid_data_structure(self):
        """Проверка обработки некорректной структуры данных"""
        with pytest.raises(KeyError):
            create_object_from_json([{"wrong": "structure"}])


def test_json_decode_error(tmp_path, capsys):
    """Проверка обработки некорректного JSON"""

    file_path = tmp_path / "invalid.json"
    file_path.write_text("{'invalid': 'json'}", encoding="utf-8")  # Одиночные кавычки - невалидный JSON

    result = read_json_file(str(file_path))

    assert result == []

    captured = capsys.readouterr()
    expected_message = f"Ошибка: файл {file_path} содержит некорректный JSON!"
    assert expected_message in captured.out
