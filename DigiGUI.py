#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import tkMessageBox
import Tkinter

from digi_reader import *

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter Barcode")

        button = Tkinter.Button(self,text=u"Submit",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Hello !")


        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        data = barcodeScan(self.entryVariable.get())
        self.labelVariable.set( self.entryVariable.get())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
        data = barcodeScan(self.entryVariable.get())
        self.labelVariable.set( "provider " + data['provider'] + "\nBarcode: self.entryVariable.get()")
        #, data['provider_pn'], data['manufacturer_pn'], data['description']
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)


def Submission(line):
    print("Submission")

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
