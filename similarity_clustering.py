

def extract_published_data(published_assignment):
    data = []
    with open(published_assignment, 'r') as f:
        is_collecting_data = False
        current_entry = {}

        for line in f:
            line = line.strip()

            if line == '_Atom_chem_shift.Assigned_chem_shift_list_ID':
                is_collecting_data = True
                current_entry = {}
            elif line == 'stop_':
                is_collecting_data = False
                if current_entry:
                    data.append(current_entry)
            elif is_collecting_data:
                key, value = line.split(None, 1)
                current_entry[key] = value

    return data


def write_published_data_to_table(output_file, data):
    with open(output_file, 'w') as f:
        for entry in data:
            for key, value in entry.items():
                f.write(f"{key}\t{value}\n")
            f.write("\n")

published_assignment = 'tycko_39-95_shifts_3D.txt'
formatted_published_assignment = extract_published_data(published_assignment)

table_formatted_published_assignment = f"formatted_{published_assignment}"
write_published_data_to_table(table_formatted_published_assignment, formatted_published_assignment)
