from tkinter import *
import tkinter.ttk
from tkinter import filedialog,messagebox,colorchooser
import os
from datetime import datetime
from tkinter.font import *
from datetime import date
import webbrowser

class Notepad():
    filename="none"
    def clear(self,event=""):
        self.txtbox.delete(1.0,END)
    ##########  Open Menu----------------------if  not s.strip() and self.filename=="none" :
    def open(self):
        s=self.txtbox.get(1.0,END)
        if not  s.strip() and self.filename=="none" :
            result = filedialog.askopenfile(initialdir='/', title="Open File",
                                            filetypes=(("Text Document", "*.txt"), ("All Files", "*.*")))
            for data in result:
                self.txtbox.insert(INSERT, data)
                self.filename = result.name


        else:
            result = messagebox.askyesnocancel("Write Book", "Do you want to save changes")
            if result == True:
                f = filedialog.asksaveasfile(mode="w", initialfile="Untitled.txt", defaultextension=".txt", )
                data = self.txtbox.get(1.0, END)
                f.write(data)
                self.filename = f.name
                f.close()
                self.clear()
                result = filedialog.askopenfile(initialdir='/', title="Open File",
                                                filetypes=(("Text Document", "*.txt"), ("All Files", "*.*")))
                for data in result:
                    self.txtbox.insert(INSERT, data)
                    self.filename = result.name
            elif result == False:
                result=filedialog.askopenfile(initialdir='/',title="Open File",filetypes=(("Text Document","*.txt"),("All Files","*.*")))
                for data in result:
                    self.txtbox.insert(INSERT,data)
                    self.filename=result.name

    #########   Save File ##########
    def save(self):
        if self.filename=="none":
            self.saveas()
        else:
            f=open(self.filename,mode='w')
            f.write(self.txtbox.get(1.0,END))
            f.close()

    def cut(self):
        self.copy()
        self.delete()
    def copy(self):
        self.txtbox.clipboard_clear()
        self.txtbox.clipboard_append(self.txtbox.selection_get())
    def paste(self):
        self.txtbox.insert(INSERT,self.txtbox.clipboard_get())
    def delete(self):
        self.txtbox.delete('sel.first', 'sel.last')
    def selectall(self,event=""):
        self.txtbox.tag_add(SEL,"1.0",END)
        self.txtbox.mark_set(INSERT,"1.0")
        #self.txtbox.see(INSERT)
    def datetime(self):
        today=datetime.now()

        timebox=today.strftime("%Y-%m-%d %H:%M:%S ")
        #date = today.strftime("%Y-%m-%d ")
        #print(today.strftime("%H:%M:%S "))
        self.txtbox.insert(INSERT,timebox)
    def color(self):
        backcolor=colorchooser.askcolor()
        self.txtbox.configure(background=backcolor[1])
    def font(self):
        fontcolor=colorchooser.askcolor()
        self.txtbox.configure(foreground=fontcolor[1])

    def callback2(self):
        webbrowser.open_new(r"https://www.pubg.com/")
    def callback(self):
        webbrowser.open_new(r"https://en.wikipedia.org/wiki/Microsoft_Notepad")

     ########### Save As #############
    def saveas(self):
        f=filedialog.asksaveasfile(mode="w",initialfile="Untitled.txt",defaultextension=".txt")
        data=self.txtbox.get(1.0,END)
        f.write(data)
        self.filename=f.name
        self.final.title(os.path.basename(self.filename) + "Notepad")

        f.close()

    def new1(self):
        s=self.txtbox.get(1.0 , END)
        if not s.strip():
            pass
        else:
            result=messagebox.askyesnocancel("Write Book","Do you want to save changes")
            if result==True:
                f = filedialog.asksaveasfile(mode="w", initialfile="Untitled.txt", defaultextension=".txt" ,)
                data = self.txtbox.get(1.0, END)
                f.write(data)
                self.filename = f.name
                f.close()
                self.clear()
            elif result==False:
                self.clear()

    def exit(self):
        s=self.txtbox.get(1.0,END)
        if not s.strip():
            quit()
        else:
            result = messagebox.askyesnocancel("Write Book", "Do you want to save changes")
            if result == True:
                f = filedialog.asksaveasfile(mode="w", initialfile="Untitled.txt", defaultextension=".txt", )
                data = self.txtbox.get(1.0, END)
                f.write(data)
                self.filename = f.name
                f.close()
                quit()
            elif result == False:
                quit()

    def font1(self):
        Font(family="Arial", size=80, weight="bold",
                       underline=0, slant='roman' , overstrike=0)






############### Create Layout ############
    def __init__(self,final):
        '''
        menubar=Menu(final)
        final.config(menu=menubar)
        file_menu=Menu(menubar,tearoff=False)
        menubar.add_cascade(label="File",menu=file_menu,)
        file_menu.add_cascade(label="New",) '''



        self.txtbox=Text(final,padx=3,pady=3,wrap=WORD,insertwidth=3,selectbackground="pink",font=self.font1)
        self.txtbox.pack(fill=BOTH,expand=1)
        '''
        scrollbar1=Scrollbar(self.txtbox)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=self.txtbox.yview)
        self.txtbox.config(yscrollcommand=scrollbar1.set)'''
        self.menubar=Menu()
        self.final=final
        self.final.config(menu=self.menubar)


        #####     FILE MENU     #######
        self.filemenu=Menu(self.menubar,tearoff=False)
        # r=tkinter.ttk.Separator(final,orient=VERTICAL).grid(column=1,row=0,rowspan=7,sticky="ns")
        self.menubar.add_cascade(label="File ",menu=self.filemenu,)
        ########### Members of File Menu      #######
        '''
                      \u22EE    unicod 
        '''

        self.filemenu.add_command(label="New""                            Ctrl+N",command=self.new1)
        self.filemenu.add_command(label="Open""                          Ctrl+O",command=self.open)
        self.filemenu.add_command(label="Save""                            Ctrl+S",command=self.save)
        self.filemenu.add_command(label="Save as",command=self.saveas)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Page Setup")
        self.filemenu.add_command(label="Print""                            Ctrl+P")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit" , command=self.exit)


        ########   Edit Menu   ######
        self.editmenu=Menu(self.menubar,tearoff=False)
        self.menubar.add_cascade(label="Edit",menu=self.editmenu)
        self.editmenu.add_command(label="Undo"   "    "  "     "  "        Ctrl+Z")
        self.editmenu.add_command(label="Redo                      Ctrl+Y")
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut                       Ctrl+Z",command=self.cut)
        self.editmenu.add_command(label="Copy                       Ctrl+Z",command=self.copy)
        self.editmenu.add_command(label="Paste                      Ctrl+Z",command=self.paste)
        self.editmenu.add_command(label="Delete                     Ctrl+Z",command=self.delete)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Find                        Ctrl+Z")
        self.editmenu.add_command(label="Find Next                   Ctrl+Z")
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Replace                     Ctrl+Z")
        self.editmenu.add_command(label="Go to                       Ctrl+Z")
        self.editmenu.add_command(label="Select All                       Ctrl+Z",command=self.selectall)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Time/Date                          Ctrl+Z",command=self.datetime)

        ####   Format Menu ######
        self.formatmenu=Menu(self.menubar,tearoff=False)
        self.menubar.add_cascade(label="Formate",menu=self.formatmenu)
        self.formatmenu.add_command(label="Color",command=self.color)
        self.formatmenu.add_command(label="Font",command=self.font)

        #####  View Menu    ##########
        self.viewmenu=Menu(self.menubar,tearoff=False)
        self.menubar.add_cascade(label="View" ,menu=self.viewmenu)
        self.viewmenu.add_command(label="Status Bar")

        ##### Help menu   ########
        self.helpmenu=Menu(self.menubar,tearoff=False)
        self.menubar.add_cascade(label="Help",menu=self.helpmenu)
        self.helpmenu.add_command(label="View Help")
        self.helpmenu.add_command(label="About Notepad",command=self.callback)
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label="About Aayushmaan Notepad ",command=self.callback2)


ti=Tk()
ti.title("Untitled - Notepad")
#ti.geometry("800x550+300+70")
note=Notepad(ti)

mainloop()