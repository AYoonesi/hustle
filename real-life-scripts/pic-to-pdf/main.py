import os
import img2pdf

def convert_images_to_pdf(image_paths, output_pdf_path):
    with open(output_pdf_path, "wb") as pdf_file:
        pdf_file.write(img2pdf.convert(sorted(image_paths), size=None))

if __name__ == "__main__":
    # Get the script directory
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Specify the directory containing your JPG files
    jpg_directory = os.path.join(script_directory, 'input')

    # Create the output folder within the script directory
    output_folder = os.path.join(script_directory, 'output')
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all JPG files in the directory
    jpg_files = [f for f in os.listdir(jpg_directory) if f.lower().endswith('.jpg')]

    # Create a list of absolute paths to the JPG files
    jpg_paths = [os.path.join(jpg_directory, jpg_file) for jpg_file in jpg_files]

    # Specify the output PDF file path
    output_pdf_path = os.path.join(output_folder, 'output.pdf')

    # Convert the JPG files to a PDF in alphabetical order
    convert_images_to_pdf(jpg_paths, output_pdf_path)
