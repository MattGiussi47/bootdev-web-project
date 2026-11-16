
import os
import shutil
import sys

from generate_page import generate_pages_recursive


def copy_static(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)

    items = os.listdir(source)

    for item in items:
        print(item)

        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
        else:
            copy_static(source_path, destination_path)


def main():
    basepath = "/"

    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Starting static site generator...")

    copy_static("static", "docs")

    generate_pages_recursive(
        "content",
        "template.html",
        "docs",
        basepath,
    )


main()
