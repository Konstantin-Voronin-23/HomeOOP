from config import PATH_TO_JSON
from src.utils import create_object_from_json, read_json_file

if __name__ == "__main__":
    json_data = read_json_file(PATH_TO_JSON)
    json_obj = create_object_from_json(json_data)
    print(json_obj)
