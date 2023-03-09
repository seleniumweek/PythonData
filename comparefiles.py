import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import font as tkFont
from tkinter import scrolledtext
from pdfminer.high_level import extract_text
import module as md
from tkinter import messagebox

my_w = tk.Tk()
my_w.geometry("1200x700")  # Size of the window 
my_w.title('File Compare')
my_font1=('verdana', 20, 'bold')
my_w.configure(background='grey')
l1 = Label(my_w, text = "File1:",font="verdana")
l2 = Label(my_w, text = "File2:", font="verdana")

l1.grid(row = 0, column = 0, sticky = W, pady = 1, padx=20)
l2.grid(row = 1, column = 0, sticky = W+N, pady = 1,padx=20)

my_str1 = tk.StringVar()
my_str2 = tk.StringVar()
difference = tk.StringVar()
font = tkFont.Font(family='verdana', size=12, weight=tkFont.BOLD)
e1 = Entry(my_w,width=50, font=('Verdana'),textvariable=my_str1,state='disabled')
e2 = Entry(my_w,width=50, font=('Verdana'),textvariable=my_str2,state='disabled')
e1.grid(row = 0, column = 1, pady = 3, sticky = W)
e2.grid(row = 1, column = 1, pady = 3, sticky = W+N)
my_str1.set("")
my_str2.set("")
difference.set("")
b1 = tk.Button(my_w, text='Browse',font=font,
   width=8,command = lambda:upload_file(1))
b1.grid(row = 0, column = 2, pady = 20,padx=20,sticky = W+N) 

b2 = tk.Button(my_w, text='Browse',font=font,
   width=8,command = lambda:upload_file(2))
b2.grid(row = 1, column = 2, pady = 0,padx=20,sticky = W+N) 

b3 = tk.Button(my_w, text='Compare',font=font,
   width=8,command = lambda:read_file())
b3.grid(row = 0, column = 3,pady = 20,padx=50,sticky = W+N) 

b4 = tk.Button(my_w, text='Clear',font=font,
   width=8,command = lambda:delete())
b4.grid(row = 1, column = 3, pady =0,padx=50,sticky = W+N) 

text = scrolledtext.ScrolledText(my_w, font=('verdana', 10, 'normal'), wrap=tk.WORD,height=28, width=110)
text.grid(row=2,column=1,sticky=W+N,padx=2,rowspan=10,pady=10,columnspan=3)
text.delete("1.0","end")


f_types = [('All Files', '*.*'), 
            ('Python Files', '*.py'),
            ('Text Document', '*.txt'),
            ('CSV files',"*.csv")]
def upload_file(fileid):
    file = filedialog.askopenfilename(
          filetypes=f_types)
    if (file):
        if fileid ==1:
              my_str1.set(file)
        else:
              my_str2.set(file)
    else:
        print("No file chosen")  


def delete():
   text.config(state=NORMAL)   
   text.delete("1.0","end") 
   e1.config(state=NORMAL)    
   e1.delete("0","end")     
   e2.config(state=NORMAL)  
   e2.delete("0","end")      
   e1.config(state=DISABLED)  
   e2.config(state=DISABLED)  
   text.config(state=DISABLED)  

def read_file():
      file1name=my_str1.get()
      file2name=my_str2.get()

      if((file1name !="") and(file2name !="")):
            if(( 'csv' in file1name and  'csv' in file2name) or 
            ('txt' in file1name and  'txt' in file2name)):
                  value = md.readCSVText(file1name,file2name)
                  text.delete('1.0',END) 
                  text.insert(END,value)  

            elif ('html' in file1name and  'html' in file2name):
                  value = md.readHTMLDocument(file1name,file2name)
                  text.delete('1.0',END) 
                  text.insert(END,value)   

            elif ('pdf' in file1name and  'pdf' in file2name):      
                  wordtext1 = md.readPdfFileAndConvertString(file1name)
                  wordtext2 = md.readPdfFileAndConvertString(file2name)
                  final = ""
                  for lists in wordtext1:
                        count =0
                        for j in range(len(lists)):
                              cur = ''
                              if wordtext1[count][j] != wordtext2[count][j]:
                                    cur ="Line Number: {} and Page Number{}\nFile1:{}\nFile2:{}\n\n".format(j+1,count+1,wordtext1[count][j],wordtext2[count][j])
                                    final = final + cur
                              elif(wordtext1[count][j] != wordtext2[count][j]):
                                    pass
                        count = count +1      
                  text.delete('1.0',END) 
                  text.insert(END,final)

            elif ('docx' in file1name and  'docx' in file2name):
                  value = md.readandSaveDocxDifferences(file1name,file2name)
                  text.delete('1.0',END) 
                  text.insert(END,value)

            elif('xlsx' in file1name and 'xlsx' in file2name):
                  dfvalues = md.ReadExcelData()
                  text.delete('1.0',END) 
                  text.insert(END,dfvalues.to_string(index=False))
            text.config(state=DISABLED)        
            messagebox.showinfo("Information","Comparision Completed")      
      else:
            messagebox.showerror("Error","Please select valid files")            
              
my_w.mainloop()