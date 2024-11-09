import os

def update_title_in_frontmatter(file_path):
    # Get the filename without extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the entire file
        content = file.read()

    # Check if there is frontmatter (--- at the beginning)
    if content.startswith('---'):
        # Split the file content by the frontmatter markers
        parts = content.split('---', 2)

        if len(parts) >= 3:
            # Frontmatter is in parts[1], content after frontmatter is in parts[2]
            frontmatter = parts[1].strip()

            # Check if there is a title field in the frontmatter
            lines = frontmatter.splitlines()
            title_found = False
            updated_lines = []

            for line in lines:
                # If the title field is found, keep it as is
                if line.startswith('title:'):
                    title_found = True
                    updated_lines.append(line)
                else:
                    updated_lines.append(line)

            # If no title field was found, add the title to the frontmatter
            if not title_found:
                updated_lines.insert(0, f"title: {file_name}")

            # Rebuild the frontmatter section
            updated_frontmatter = '\n'.join(updated_lines)

            # Rebuild the content with the updated frontmatter
            updated_content = f"---\n{updated_frontmatter}\n---\n{parts[2]}"

            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)

            print(f"Updated frontmatter for {file_path}")
        else:
            print(f"Invalid frontmatter format in {file_path}")
    else:
        # No frontmatter exists, so create it with the title as the filename
        updated_content = f"---\ntitle: {file_name}\n---\n{content}"

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"Created frontmatter with title for {file_path}")


def update_markdown_files_in_directory(directory_path):
    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Only process markdown files (ending with .md)
        if os.path.isfile(file_path) and filename.endswith('.md'):
            update_title_in_frontmatter(file_path)


# Example usage: Update all markdown files in a directory
if __name__ == "__main__":
    directory = './content'  # Replace with the path to your directory
    update_markdown_files_in_directory(directory)