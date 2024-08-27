import json


def load_data(file_path):
    """loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animal_name(animal):
    name = animal['name']
    return name


def get_animal_sci_name(animal):
    sci_name = animal['taxonomy']['scientific_name']
    return sci_name


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
        return ''
    return animal_type


def serialize_animal(animal):
    output = ''
    name = get_animal_name(animal)
    diet = get_animal_diet(animal)
    location = get_animal_location(animal)
    animal_type = get_animal_type(animal)
    sci_name = get_animal_sci_name(animal)
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{name}</div>\n'
    output += '<p class="card__text">\n'
    output += '<ul>\n'
    output += f'<li><strong>Scientific Name:</strong> {sci_name}</li>\n'
    output += f'<li><strong>Location:</strong> {location}</li>\n'
    if animal_type:
        output += f'<li><strong>Type:</strong> {animal_type}</li>\n'
    output += f'<li><strong>Diet:</strong> {diet}</li>\n'
    output += '</ul>\n'
    output += '</p>\n'
    output += '</li>\n'
    return output


def get_animal_key_data(animals_data):
    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def get_skin_types_list(animals_data):
    skin_types_list = []
    for animal in animals_data:
        skin_type = animal['characteristics']['skin_type']
        skin_types_list.append(skin_type)
    return skin_types_list


def get_chosen_animal_data(animals_data):
    output = ''
    skin_types_list = get_skin_types_list(animals_data)
    for skin_type in skin_types_list:
        print(skin_type)
    chosen_skin_type = input("Please enter exactly the skin type of your choice: ")
    for animal in animals_data:
        skin_type = animal['characteristics']['skin_type']
        if skin_type == chosen_skin_type:
            output += serialize_animal(animal)

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
    animals_data = get_chosen_animal_data(load_data("animals_data.json"))
    # animals_data = get_animal_key_data(load_data("animals_data.json"))
    template_data = load_html_data("animals_template.html")
    final_output = create_final_output(template_data, animals_data)
    write_data_new_file(final_output, "animals.html")


if __name__ == "__main__":
    main()
