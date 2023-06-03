import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2
from pdf2docx import Converter

def pdf_edit():
    root = tk.Tk()
    root.title('PDF to DOCX Converter')
    language = "English"

    def browse_pdf():
        file_path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
        if file_path:
            pdf_entry.delete(0, tk.END)
            pdf_entry.insert(tk.END, file_path)

    def convert():
        pdf_path = pdf_entry.get()
        if not pdf_path:
            messagebox.showerror('Error', 'Please select a PDF file.')
            return

        word_file = os.path.splitext(pdf_path)[0] + '.docx'
        cv = Converter(pdf_path)
        cv.convert(word_file, start=0, end=None)
        cv.close()
        messagebox.showinfo('Success', 'Conversion complete.')

    def show_about():
        if language == "English":
            messagebox.showinfo("About", "This software was created by Ionut-Alexandru VIZUROIU.\nContact alexandru.vizuroiu@gmail.com for further info.")
        if language == "Romanian":
            messagebox.showinfo("Despre", "Acest software a fost creat de Ionut-Alexandru VIZUROIU.\nPentru mai multe informații: alexandru.vizuroiu@gmail.com.")

    def change_language():
        nonlocal language
        if language == "English":
            language = "Romanian"
            root.title("Convertor PDF în DOCX")
            browse_button.config(text="Încarcă")
            convert_button.config(text="Convertește")
            language_button.config(text="Schimbă limba")
            about_button.config(text="Despre")
        else:
            language = "English"
            root.title("PDF to DOCX Converter")
            browse_button.config(text="Browse")
            convert_button.config(text="Convert")
            language_button.config(text="Change Language")
            about_button.config(text="About")           
        
    # PDF Entry
    pdf_entry = tk.Entry(root, width=50)
    pdf_entry.pack(pady=10)

    # Browse Button
    browse_button = tk.Button(root, text='Browse', command=browse_pdf)
    browse_button.pack()

    # Convert Button
    convert_button = tk.Button(root, text='Convert', command=convert)
    convert_button.pack()

    language_button = tk.Button(root, text="Change Language", command=change_language)
    language_button.pack()
    
    about_button = tk.Button(root, text="About", command=show_about)
    about_button.pack()


    # Start the GUI main loop
    root.mainloop()

if __name__ == '__main__':
    pdf_edit()
