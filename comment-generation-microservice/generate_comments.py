def generate_comment(parsed_data):
    comments = {}
    for function_name in parsed_data.get("functions", []):
        comments[function_name] = f"This function {function_name} performs..."
    for class_name in parsed_data.get("classes", []):
        comments[class_name] = f"This class {class_name} is responsible for..."
    return comments
