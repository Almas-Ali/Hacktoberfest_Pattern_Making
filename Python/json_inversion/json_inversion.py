

def invert_json(json_data, output_file_name="output.txt")
    new_attributes = []
    new_dict_of_dicts = {}
    data = json.loads(json_data)

    for key in data.keys():
        new_attributes.append(key)

    for key in data[new_attributes[0]].keys():
        new_dict_of_dicts[key] = {}
        
    for category, obj in data.items():
        for person, value in obj.items():
            new_dict_of_dicts[person][category] = value

    back_to_json_str = json.dumps(new_dict_of_dicts)

    # Print to outputfile
    with open(output_file_name, "w") as outfile:
        outfile.write(back_to_json_str)

    return back_to_json_str
