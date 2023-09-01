import os


def search_files(directory, query):
    found_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if query in file:
                found_files.append(os.path.join(root, file))

    return found_files


search_directory = "/path/to/search"

search_query = "example"

found_files = search_files(search_directory, search_query)

if found_files:
    print(f"Found {len(found_files)} files:")
    for file in found_files:
        print(file)
else:
    print("No files found.")
