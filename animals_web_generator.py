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
    output = ''
    for animal in animals_data:
        name = get_animal_name(animal)
        diet = get_animal_diet(animal)
        location = get_animal_location(animal)
        animal_type = get_animal_type(animal)
        output += f"Name: {name}\nDiet: {diet}\nLocation: {location}\nType: {animal_type}\n\n"
    return output


def load_html_data(file_path):
    with open(file_path, 'r') as handle:
        return handle.read()


def create_final_output(template_data, animals_data):
    final_output = template_data.replace("__REPLACE_ANIMALS_INFO__", animals_data)
    return final_output


def write_data_new_file(output, file_path):
    with open(file_path, "w") as handle:
        handle.write(output)


def main():
    animals_data = get_animal_key_data(load_data("animals_data.json"))
    template_data = load_html_data("animals_template.html")
    final_output = create_final_output(template_data, animals_data)
    write_data_new_file(final_output, "animals.html")

    # print(get_animal_key_data(animals_data))


if __name__ == "__main__":
    main()
