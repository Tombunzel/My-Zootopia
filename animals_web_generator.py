import json


def load_data(file_path):
    """loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animal_name(animal):
    name = animal['name']
    return name


def get_animal_diet(animal):
    diet = animal['characteristics']['diet']
    return diet


def get_animal_location(animal):
    first_location = animal['locations'][0]
    return first_location


def get_animal_type(animal):
    try:
        animal_type = animal['characteristics']['type']
    except KeyError:
        animal_type = None
    return animal_type


def get_animal_key_data(animals_data):
    for animal in animals_data:
        name = get_animal_name(animal)
        diet = get_animal_diet(animal)
        location = get_animal_location(animal)
        animal_type = get_animal_type(animal)
        print(f"Name: {name}\nDiet: {diet}\nLocation: {location}\nType: {animal_type}\n")


def main():
    get_animal_key_data(animals_data = load_data("animals_data.json"))


if __name__ == "__main__":
    main()