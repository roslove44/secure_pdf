from pypdf import PdfReader, PdfWriter
import os


def protect_file(file_name, password):
    reader = PdfReader('src/'+file_name)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    writer.encrypt(password)
    with open("output/" + file_name, "wb") as out_file:
        writer.write(out_file)


files = os.listdir("src")
pdf_files = [file for file in files if file.endswith(".pdf")]
password = "my_password"  # Define your password
for pdf_file in pdf_files:
    print(pdf_file)
    protect_file(pdf_file, password)
