#Justin Hynes-Bruell  8/2/16
#Resource:
#http://www.openbookproject.net/py4fun/gui/tkPhone.html

from Tkinter import *
from phones  import *
from catalogModel  import *

from csv import *

from digi_reader import *


def OnPressEnter():
    print("Submission")

def SearchForPart ():
    code = newBarcode.get().strip()
    barcode.set(code)
    data = barcodeScan(code)

    #Append to phoneList
    phonelist.append ([code, data['provider'], data['provider_pn'], data['manufacturer_pn'], data['description']])
    
    barcode.set(code)
    provider.set(data['provider'])
    partNum.set(data['provider_pn'])
    manPartNum.set(data['manufacturer_pn'])
    description.set(data['description'])

    setSelect ()


def whichSelected () :
    print "At %s of %d" % (select.curselection(), len(phonelist))
    return int(select.curselection()[0])

def addEntry () :
    phonelist.append ([barcode.get(), provider.get(), partNum.get(), manPartNum.get(), description.get()])
    setSelect ()

def updateEntry() :
    phonelist[whichSelected()] = [[barcode.get(), provider.get(), partNum.get(), manPartNum.get(), description.get()]]
    setSelect ()

def deleteEntry() :
    del phonelist[whichSelected()]
    setSelect ()

def hello() :
    import csv

    with open('catalog.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
        write = barcode.get() + ", " + provider.get() + ", " + partNum.get() + ", " + manPartNum.get() + ", "+ description.get()
        print write
        spamwriter.writerow(write)

def loadEntry  () :
    barcode1, provider1, partNum1, manPartNum1, description1 = phonelist[whichSelected()]
    barcode.set(barcode1)
    provider.set(provider1)
    partNum.set(partNum1)
    manPartNum.set(manPartNum1)
    description.set(description1)

def catalogLoad ():
    catalog.loadCSV(csvFileName.get())

def makeWindow () :
    #Fields for input
    global newBarcode, barcode, provider, partNum, manPartNum, description, csvFileName
    
    #selection for editing
    global select
    win = Tk()

    #Search Frame for GUI
    searchFrane = Frame(win)
    searchFrane.pack()
    newBarcode = StringVar()
    name = Entry(searchFrane, textvariable=newBarcode)
    #name.entryVariable.set(u"Enter Barcode")
    name.grid(row=0, column=0, sticky=W)
    searchButton = Button(searchFrane,text=" Search  ",command=SearchForPart)
    searchButton.grid(column=1,row=0)

    #win.bind("<Return>", OnPressEnter())


    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="Barcode").grid(row=0, column=0, sticky=W)
    barcode = StringVar()
    name = Entry(frame1, textvariable=barcode)
    name.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Provider").grid(row=1, column=0, sticky=W)
    provider= StringVar()
    phone= Entry(frame1, textvariable=provider)
    phone.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Provider PN").grid(row=2, column=0, sticky=W)
    partNum= StringVar()
    phone= Entry(frame1, textvariable=partNum)
    phone.grid(row=2, column=1, sticky=W)

    Label(frame1, text="Manufacturer PN").grid(row=3, column=0, sticky=W)
    manPartNum= StringVar()
    phone= Entry(frame1, textvariable=manPartNum)
    phone.grid(row=3, column=1, sticky=W)

    Label(frame1, text="Description").grid(row=4, column=0, sticky=W)
    description= StringVar()
    phone= Entry(frame1, textvariable=description)
    phone.grid(row=4, column=1, sticky=W)

    #Save Button
    SaveFrame = Frame(win)
    SaveFrame.pack()
    searchButton = Button(SaveFrame,text=" Save to CSV  ",command=hello)
    #searchButton.grid(column=1,row=0)
    searchButton.pack(side=TOP)


    # Row of buttons
    frame2 = Frame(win)
    frame2.pack()
    b1 = Button(frame2,text=" Add  ",command=addEntry)
    b2 = Button(frame2,text="Update",command=updateEntry)
    b3 = Button(frame2,text="Delete",command=deleteEntry)
    b4 = Button(frame2,text=" Load ",command=loadEntry)
    b1.pack(side=LEFT); b2.pack(side=LEFT)
    b3.pack(side=LEFT); b4.pack(side=LEFT)

    # select of names
    frame3 = Frame(win)       
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH, expand=1)


    csvFrane = Frame(win)
    csvFrane.pack()
    csvFileName = StringVar()
    name = Entry(csvFrane, textvariable=csvFileName)
    #name.entryVariable.set(u"Enter Barcode")
    name.grid(row=0, column=0, sticky=W)
    searchButton = Button(csvFrane,text=" Load to CSV  ",command=catalogLoad)
    searchButton.grid(column=1,row=0)
    return win

def setSelect () :
    phonelist.sort()
    select.delete(0,END)
    for barcode, provider, partNum, manPartNum, description in phonelist :
        select.insert (END, barcode)

win = makeWindow()
setSelect ()
win.mainloop()