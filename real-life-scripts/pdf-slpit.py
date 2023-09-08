import os
import PyPDF2

def split_pdf(input_path, output_path, start_page, end_page):
    with open(input_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)

        # Create a new PDF writer
        output_pdf = PyPDF2.PdfWriter()

        # Iterate through pages to extract desired range
        for page_number in range(start_page-1, end_page):
            page = pdf.pages[page_number]
            output_pdf.add_page(page)

        # Write the output to a new file
        with open(output_path, 'wb') as new_file:
            output_pdf.write(new_file)
        
        print(f'File saved in {output_path}.')

# Example usage
script_directory = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_directory, 'naghd-ravie.pdf')
output_file = os.path.join(script_directory, 'split_naghd-ravie.pdf')
start_page = 4
end_page = 10

split_pdf(input_file, output_file, start_page, end_page)