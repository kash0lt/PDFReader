import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

rootwindow = tk.Tk()
rootwindow.title('PDFReader App')
topcanvas = tk.Canvas(rootwindow, width=300, height=300)
topcanvas.grid(columnspan=3, rowspan=4)   # three columns

# logo
logo = ImageTk.PhotoImage(Image.open('logo.png'))
logo_label = tk.Label(image=logo)
logo_label.grid(column=1, row=0)

# instructions
instructions = tk.Label(
    rootwindow, text="Select a PDF file on your computer to extract page 1 text", font="Arial")
instructions.grid(columnspan=3, column=0, row=1)


def open_pdfFile():
    browsetext.set("loading...")
    text_box.delete("1.0", "end")   # Clear out what might be there first
    # Do not include the filetypes tuple on MacOS as the file window does not support file types
    theFile = askopenfile(parent=rootwindow, mode='rb', title='Choose a file')
#    theFile = askopenfile(parent=rootwindow, mode='rb',
#                          title = 'Choose a file', filetype = [('PDF file', '*.pdf')])
    if theFile:
        read_pdf = PyPDF2.PdfFileReader(theFile)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        text_box.insert(1.0, page_content)

    browsetext.set("Browse")


# browse button
browsetext = tk.StringVar()
browse_btn = tk.Button(rootwindow, textvariable=browsetext, command=lambda: open_pdfFile(), font="Arial", bg="#20bebe", fg="white",
                       height=2, width=15)
browsetext.set("Browse")
browse_btn.grid(column=1, row=2)
# add more space at the bottom for the Text results
bottomcanvas = tk.Canvas(rootwindow, width=600, height=250)
bottomcanvas.grid(columnspan=3)   # three columns
# text Box for PDF
text_box = tk.Text(rootwindow, height=10, width=50, padx=15, pady=15)
text_box.grid(column=1, row=4)

rootwindow.mainloop()
