# project.py
import sys

def parse_args(args):
    if len(args) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    return args[1], args[2]

if __name__ == "__main__":
    input_file, output_file = parse_args(sys.argv)
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")

    
# project.py (dalsza część)
import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError:
        print("Invalid JSON file")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file = parse_args(sys.argv)
    if input_file.endswith('.json'):
        data = load_json(input_file)
        print(data)

import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Opcjonalnie: Weryfikacja składni za pomocą schematu JSON
            return data
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

        if __name__ == "__main__":
    input_file, output_file = parse_arguments()

    if input_file.endswith('.json'):
        data = load_json(input_file)
        print(f"Data: {data}")
    else:
        print("Unsupported input format")
        sys.exit(1)
def save_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving JSON file: {e}")
        sys.exit(1)
        if __name__ == "__main__":
    input_file, output_file = parse_arguments()

    if input_file.endswith('.json'):
        data = load_json(input_file)
    else:
        print("Unsupported input format")
        sys.exit(1)

    if output_file.endswith('.json'):
        save_json(data, output_file)
    else:
        print("Unsupported output format")
        sys.exit(1)
import yaml

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except yaml.YAMLError as e:
        print(f"Invalid YAML format: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
if __name__ == "__main__":
    input_file, output_file = parse_arguments()

    if input_file.endswith('.json'):
        data = load_json(input_file)
    elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
        data = load_yaml(input_file)
    else:
        print("Unsupported input format")
        sys.exit(1)


