
import os

from markdown_to_html import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html)

    page = page.replace('href="/', f'href="{basepath}')
    page = page.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path) or ".", exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(page)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    entries = os.listdir(dir_path_content)

    for entry in entries:
        source_path = os.path.join(dir_path_content, entry)
        destination_path = os.path.join(dest_dir_path, entry)

        if os.path.isfile(source_path):
            if entry.endswith(".md"):
                destination_path = os.path.splitext(destination_path)[0] + ".html"

                generate_page(
                    source_path,
                    template_path,
                    destination_path,
                    basepath,
                )
        else:
            generate_pages_recursive(
                source_path,
                template_path,
                destination_path,
                basepath,
            )
