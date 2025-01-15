"""
How to use:
e.g.
python .\.foam\index_gen.py "content/Learn/Data Analytics/Power BI/Microsoft Learn" 
"""


import os
import sys
from datetime import datetime

def create_markdown_files(root_folder):
    # Get today's date in the desired format
    today = datetime.today().strftime('%Y-%m-%d')

    # Walk through each folder and subfolder
    for dirpath, dirnames, filenames in os.walk(root_folder):
        # Create the .md file name
        md_filename = os.path.join(dirpath, 'Index - '+os.path.basename(dirpath)+'.md')
        print("----")
        print(dirpath, "||", os.path.basename(dirpath))
        # Prepare the content for the .md file
        content = f"""---
title: {'Index - '+os.path.basename(dirpath)}
created: {today}
updated: {today}
---

"""
        # List all .md files in the folder
        for file in filenames:
            if file.endswith('.md') and file != (os.path.basename(dirpath)+'.md'):
                content += f"- [[{file}]]\n"

        # Write the content to the .md file
        with open(md_filename, 'w') as md_file:
            print(md_filename)
            md_file.write(content)

    print("Markdown files created successfully!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_folder>")
    else:
        root_folder = sys.argv[1]
        create_markdown_files(root_folder)
