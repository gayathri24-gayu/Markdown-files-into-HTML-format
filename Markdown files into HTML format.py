import markdown
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_md_to_html(input_file, output_file="output.html"):
    with open(input_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    html_content = markdown.markdown(md_content)
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)
    return output_file

def gui_interface():
    def select_file():
        file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
        if file_path:
            output_file = "output.html"
            convert_md_to_html(file_path, output_file)
            messagebox.showinfo("Success", f"Markdown converted to HTML and saved as {output_file}")

    root = tk.Tk()
    root.title("Markdown to HTML Converter")
    tk.Button(root, text="Select Markdown File", command=select_file).pack()
    root.mainloop()

def main():
    print("Select Interface Mode:")
    print("1. Console Interface")
    print("2. GUI Interface")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        console_interface()
    elif choice == '2':
        gui_interface()
    else:
        print("Invalid choice. Exiting.")

if _name_ == "_main_":
    main()
