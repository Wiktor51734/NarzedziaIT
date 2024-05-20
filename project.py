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
