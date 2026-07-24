from markdown_to_html_node import markdown_to_html_node
import os
from pathlib import Path
import shutil
import re

def copy_static_to_public(static: Path, public: Path, public_deleted=False):

    if os.path.exists(public) == False:
        os.mkdir(public)
    
    if len(os.listdir(public)) > 0 and public_deleted == False:
        delete_public_files(public)
        copy_static_to_public(static, public, public_deleted=True)
    else:
        for item in static.iterdir():

            # example item_copy print: /home/peyton/Workspace/code/static-site-generator/public/index.css
            item_copy = (item.parents[1] / public / item.name)
            if item.is_file():
                shutil.copy(item, item_copy)
            elif item.is_dir():
                os.mkdir(item_copy)
                copy_static_to_public(item, item_copy, public_deleted=True)

def delete_public_files(public):

    for item in public.iterdir():
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)

def extract_title(markdown):

    pattern = r"#.+"
    match = re.search(pattern, markdown)

    if match:
        return match.group().replace("# ", "")
    
    raise ValueError("Error: markdown has no h1 header")

def generate_page(from_path, template_path, dest_path):

    with (
        open(from_path) as from_path_file,
        open(template_path) as template_path_file,
    ):
        from_path_contents = from_path_file.read()
        template_path_contents = template_path_file.read()

    md_to_html = markdown_to_html_node(from_path_contents).to_html()
    title = extract_title(from_path_contents)
    template_path_contents = template_path_contents.replace("{{ Title }}", title)
    template_path_contents = template_path_contents.replace("{{ Content }}", md_to_html)
    
    with open(dest_path, "w") as file:
        file.write(template_path_contents)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    temp_file_content = ""
    temp_path = None

    with open(template_path, "r") as file:
        template_file = file.read()

    for item in dir_path_content.iterdir():
        print(item)
        if item.is_file():
            with open(item) as file:
                md = file.read()
            if item.parent.name == "content":
                temp_path = (dest_dir_path / f"{item.stem}.html")
            else:
                temp_path = (dest_dir_path / f"{item.stem}.html")
            
            md_to_html = markdown_to_html_node(md).to_html()
            title = extract_title(md)
            temp_file_content = template_file.replace("{{ Title }}", title)
            temp_file_content = temp_file_content.replace("{{ Content }}", md_to_html)
            with open(temp_path, "w") as file:
                file.write(temp_file_content)
        elif item.is_dir():
            os.mkdir(dest_dir_path / item.name)
            print((dest_dir_path / item.name))
            generate_pages_recursive(dir_path_content=item, template_path=template_path, dest_dir_path=(dest_dir_path / item.name))
            
            





def main():
    # __file__ is a built in variable that automatically holds the path of the current .py script "main.py" in this case.
    # .resolve() Finds the aboslute, real path on your hard drive. It removes any confusing shortcuts or temporary locations.
    # .parent Grabs the folder that CONTAINS your script
    # So the Path object we just created is a path to SRC
    script_dir = Path(__file__).resolve().parent

    # creates a Path object by using the / operator, which detects that script_dir is a path object and appends the .. and static or public locations onto the script_dir path
    # This ensures the Path objects are created using the absolute path to each respective directory. The / operator also forms the paths dynamically, meaning it will work on 
    # Windows, MAC, or Linux. .resolve() looks at the folder path with the .. inside it and actually PROCCESSES the "cd .." on your hard drive
    # This is so the final path becomes a clean, direct line
    STATIC_DIR = (script_dir / ".." / "static").resolve()
    PUBLIC_DIR = (script_dir / ".." / "public").resolve()
    DEST_PATH = (script_dir / ".." / "public" / "index.html")
    FROM_PATH = (script_dir / ".." / "content" / "index.md").resolve()
    CONTENT_PATH = (script_dir / ".." / "content").resolve()
    TEMPLATE_PATH = (script_dir / ".." / "template.html").resolve()
    copy_static_to_public(static=STATIC_DIR, public=PUBLIC_DIR)
    # print(f"Generating page from {FROM_PATH} to {PUBLIC_DIR} using {TEMPLATE_PATH}")
    # generate_page(from_path=FROM_PATH, template_path=TEMPLATE_PATH, dest_path=DEST_PATH)
    generate_pages_recursive(dir_path_content=CONTENT_PATH, template_path=TEMPLATE_PATH, dest_dir_path=PUBLIC_DIR)

    




    

if __name__ == "__main__":
    main()
