def get_file_extension(description) :
    """Returns the appropriate file extension based on the description."""
    extensions = {
        "python file" : ".py",
        "java file" : ".java",
        "text file" : ".txt",
        "html file" : ".html",
        "css file" : ".css",
        "javascript file" : ".js",
        "json file" : ".json",
        "xml file" : ".xml",
        "csv file" : ".csv",
        "markdown file" : ".md",
        "yaml file" : ".yaml",
        "image file" : ".jpg",  # Add more extensions as needed
        "video file" : ".mp4",
        "audio file" : ".mp3",
        "pdf file" : ".pdf",
        "word file" : ".docx",
        "excel file" : ".xlsx",
        "powerpoint file" : ".pptx",
        "zip file" : ".zip",
        "tar file" : ".tar"
    }
    return extensions.get(description, "")  # Default to empty string if no match


def clean_description(description) :
    """Removes specific keywords from the description."""
    keywords = [
        "python file", "java file", "text file", "html file", "css file",
        "javascript file", "json file", "xml file", "csv file", "markdown file",
        "yaml file", "image file", "video file", "audio file", "pdf file",
        "word file", "excel file", "powerpoint file", "zip file", "tar file",
        "named", "with name", "create"
    ]
    for keyword in keywords :
        description = description.replace(keyword, "")
    return description.strip()


def create_file(description) :
    """Creates a file based on the provided description."""
    file_extension = get_file_extension(description)
    file_name = clean_description(description)

    if file_name :
        file_name = f"{file_name}{file_extension}"
    else :
        file_name = f"demo{file_extension}"

    try :
        with open(file_name, "w") as file :
            pass
        print(f"File '{file_name}' created successfully.")
    except Exception as e :
        print(f"Error creating file: {e}")


# Example usage:
if __name__ == "__main__" :
    create_file("Create a python file named example")
