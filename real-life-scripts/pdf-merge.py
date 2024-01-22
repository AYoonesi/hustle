import os
import PyPDF2

def merge_pdf(input_paths = [], output_path = 'merge-output.pdf'):
    merger = PyPDF2.PdfWriter()
    for file in input_paths:
        with open(file, 'rb') as pdffile:
            merger.append(pdffile)
    output = open(output_path, "wb")
    merger.write(output)
    merger.close()
    output.close()
    print(f'File saved in {output_path}.')

# Example usage
script_directory = os.path.dirname(os.path.abspath(__file__))
input_paths = [
    os.path.join(script_directory, 'The 13 Steps of Successful Academic Legal Research - p1.pdf'),
    os.path.join(script_directory, 'The 13 Steps of Successful Academic Legal Research -et.pdf'),
]
merge_pdf(input_paths, 'The 13 Steps of Successful Academic Legal Research - merged.pdf')