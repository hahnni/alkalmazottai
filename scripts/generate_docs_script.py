import os
import openai
import ast

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_code_structure(code):
    """
    Extracts function definitions and docstrings from Python code using ast.
    """
    tree = ast.parse(code)
    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            docstring = ast.get_docstring(node) or "No docstring provided"
            functions.append({"name": function_name, "docstring": docstring})

    return functions

def generate_documentation(code_snippet):
    """
    Uses OpenAI's API to generate documentation from code snippets.
    """
    prompt = f"The following is a code snippet. Generate detailed documentation:\n\n{code_snippet}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for generating code documentation."},
                {"role": "user", "content": prompt},
            ]
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error generating documentation: {str(e)}"

def save_documentation(func_name, documentation):
    """
    Save the generated documentation to a file in the 'docs/' directory.
    """
    output_dir = "docs/"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{func_name}.md")

    with open(output_file, "w") as file:
        file.write(f"### Function: {func_name}\n\n{documentation}\n")

def main():
    # Example: Input Python code
    code = """
def calculate_area(length, width):
    \"\"\"
    Compute the area of a rectangle.
    \"\"\"
    return length * width

def perimeter(length, width):
    \"\"\"Calculate the perimeter of a rectangle.\"\"\"
    return 2 * (length + width)
"""

    # Step 1: Extract code structure
    functions = extract_code_structure(code)

    # Step 2: Generate documentation for each function
    for func in functions:
        print(f"Generating documentation for function: {func['name']}")
        doc = generate_documentation(f"def {func['name']}:\n    {func['docstring']}")
        save_documentation(func['name'], doc)
        print(f"Documentation for {func['name']} saved to docs/{func['name']}.md")

if __name__ == "__main__":
    main()
