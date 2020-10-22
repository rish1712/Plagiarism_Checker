import tkinter as tk
from Preprocess import *
from tkinter import Entry,Button
from tkinter.scrolledtext import ScrolledText
from functools import partial
from tkinter import messagebox
from Spell_Check import *
from tkinter import filedialog
from tkinter import *
import pickle
import time
flag=0
flag1=0
NUMBER_OF_FILES = 4
mycorpus = Corpus()

def call_result(number1,number2,flag=0):
    try:
        if flag1001==0:
            messagebox.showinfo('ERROR 404', 'Please add documents to preprocess')
            return
    except:
        messagebox.showinfo('ERROR 404', 'Please add documents to preprocess')
        return

    #print("the content vector started at " + str(time.time()))
    txt2 = ScrolledText(window, width=40, height=11, font=("Arial", 12))
    txt2.place(x=75, y=270)
    str1='business/'+number1.get()
    str2=number2.get()
    if str2=="":
        str2=str(0)
    elif str2[0]=='-':
        messagebox.showinfo('ERROR 404', 'Give a correct upper bound')
    elif str2[len(str2)-1]=='%':
        str2=str2[0:len(str2)-1]
    try:
        print(float(str2))
        if not(float(str2)>=0 and float(str2)<=100):
            messagebox.showinfo('ERROR 404', 'Give a correct upper bound')
            return
    except:
        messagebox.showinfo('ERROR 404', 'Give a correct upper bound')
        return

    docx = None
    if mycorpus.getDocInd(number1.get()):
        flag = 1
        docx = Document(str1)

# str2 me percentage hai plagrisam ka

    if docx!=None:
        with open('filename.pickle', 'rb+') as handle:
            unserialized_data = pickle.load(handle)
        list1=docx.tokens
        list1.append(str2)
        if tuple(list1) in unserialized_data:
            txt2.insert(tk.END, unserialized_data[tuple(docx.tokens)])
            txt2.config(state='disabled')
            print("inside cache")
            print(time.time())


        elif flag==0:
            messagebox.showinfo('ERROR 404','The given Document is not available in the given Corpus')


        elif flag==1:
            cache=dict()
            res = mycorpus.cosineSimilarity(docx).reshape(-1)
            docorder = np.argsort(res)
            docorder = np.flip(docorder)
            answer=str()
            lim = 0
            for x in docorder:
                if(round(100 * res[x], 4))<float(str2):
                    break
                answer += mycorpus.doclist[x].name + " has " + str(str(round(100 * res[x], 4))) + "% plagiarism.\n"
            cache[tuple(list1)]=answer
            with open('filename.pickle', 'rb+') as handle:
                un = pickle.load(handle)
            un.update(cache)

            with open('filename.pickle', 'wb') as handle:
                pickle.dump(un, handle, protocol=pickle.HIGHEST_PROTOCOL)
            #print(answer)
            txt2.insert(tk.END,answer)
            txt2.config(state='disabled')

    else:
        str1=number1.get()
        docx = Document(str1)
        res = mycorpus.cosineSimilarity(docx).reshape(-1)
        docorder = np.argsort(res)
        docorder = np.flip(docorder)
        list1 = docx.tokens
        list1.append(str2)

        with open('filename.pickle', 'rb+') as handle:
            unserialized_data = pickle.load(handle)

        if tuple(list1) in unserialized_data:
            txt2.insert(tk.END, unserialized_data[tuple(docx.tokens)])
            txt2.config(state='disabled')
            print("inside cache")
            return

        answer = str()
        lim = 0
        for x in docorder:
            if (round(100 * res[x], 4)) < float(str2):
                break
            answer += mycorpus.doclist[x].name + " has " + str(str(round(100 * res[x], 4))) + "% plagiarism.\n"

        # print(answer)
        cache={}
        cache[tuple(list1)] = answer
        with open('filename.pickle', 'rb+') as handle:
            un = pickle.load(handle)
        un.update(cache)

        with open('filename.pickle', 'wb') as handle:
            pickle.dump(un, handle, protocol=pickle.HIGHEST_PROTOCOL)

        txt2.insert(tk.END, answer)
        txt2.config(state='disabled')
    print("the content ended at started at " + str(time.time()))


def call_results(number3):
    txt2 = ScrolledText(window, width=40, height=7, font=("Arial", 12))
    txt2.place(x=75, y=650)
    try:
        if flag1001 == 0:
            messagebox.showinfo('ERROR 404', 'Please add documents to preprocess')
            return
    except:
        messagebox.showinfo('ERROR 404', 'Please add documents to preprocess')
        return

    str2 = number3.get()
    print(str2)
    if str2=="":
        str2=str(0)
    elif str2[0] == '-':
        messagebox.showinfo('ERROR 404', 'Give a correct lower bound')
    elif str2[len(str2) - 1] == '%':
        str2 = str2[0:len(str2) - 1]

    try:
        if not(float(str2)>=0 and float(str2)<=100):
            messagebox.showinfo('ERROR 404', 'Give a correct upper bound')
            return
    except:
        messagebox.showinfo('ERROR 404', 'Give a correct upper bound')
        return

    string = txt3.get('1.0', tk.END)
    text = string.lower()
    text = text.replace("\n", " ")
    token_orignal = word_tokenize(text)
    spell_check = SpellCheck(token_orignal)
    text1=spell_check.text
    if text !=text1:
        messagebox.showinfo('Did u Mean', 'After correcting some spelling errors the text becomes:-\n'+text1)
    docx = Document(text1,flag = False)
    res = mycorpus.cosineSimilarity(docx)
    if res is None:
        messagebox.showinfo('NO MATCH',"The given text doesn't match with anything based on non stopwords words.")
        return None
    res = res.reshape(-1)
    docorder = np.argsort(res)
    docorder = np.flip(docorder)
    answer=str()
    for x in docorder:
        if (round(100 * res[x], 4)) < float(str2):
            break
        answer += mycorpus.doclist[x].name + " has " + str(str(round(100 * res[x], 4))) + "% plagiarism.\n"
        #print(answer)
    print(answer)
    txt2.insert(tk.END,answer)
    txt2.config(state='disabled')

def call_result1():
    window.filename = filedialog.askopenfilename(initialdir=".", title="Select file",
                                               filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    txt1.delete(0,"end")
    txt1.insert(0,window.filename)
    flag1=1

def call_resultsel():
    mypath = filedialog.askdirectory(initialdir=".")
    global flag1001
    flag1001=1
    # from os import listdir
    # from os.path import isfile, join
    # onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and ]
    import glob
    print(mypath)
    onlyfiles = glob.glob(mypath+"/*.txt")
    messagebox.showinfo('Adding files',"adding files from dir: "+ mypath)
    for x in onlyfiles:
        print(x)
        doc = Document(x)
        mycorpus.addDoc(doc)
    messagebox.showinfo('Loaded',"loaded all files")
    mycorpus.run()
    messagebox.showinfo('Done',"processed all files")

window=tk.Tk()
window.title("Pagriasm Checker")
window.geometry('570x1000')
window.resizable(True,True)
window.config(bg="lightblue")
number1=tk.StringVar()
number2=tk.StringVar()
number3=tk.StringVar()
btsel=Button(window,text="Enter the Path for documents to be preprocessed",bg="cyan",fg="black",bd=3,activebackground="white",command=call_resultsel)
btsel.place(x=130,y=85)

txt2 = ScrolledText(window, width=40, height=10, font=("Arial", 12))
txt2.place(x=75, y=270)
l1=tk.Label(window,text="Plagriasm Checker",font=("ArialBold",50))
l1.place(x=0,y=0,anchor="nw")
l2=tk.Label(window,text="Enter the file to be checked:-",font=("ArialBold",15))
l2.place(x=0,y=120)
l2=tk.Label(window,text="Enter the upper bound of allowed copied content :- ",font=("ArialBold",9))
l2.place(x=0,y=160)
txt100=Entry(window,width=6,bd=0.5,cursor='dot',font=("ArialBold",9),textvariable=number2)
txt100.place(x=285,y=160)
txt1=Entry(window,width=15,bd=0.5,cursor='dot',font=("ArialBold",17),textvariable=number1)
txt1.place(x=265,y=120)
call_result=partial(call_result,number1,number2)
bt1=Button(window,text="Check Plagriasm content",bg="cyan",fg="black",bd=3,activebackground="white",command=call_result)
bt1.place(x=175,y=190)
#txt1=ScrolledText(window,width=40,height=10)
l2=tk.Label(window,text="Enter the text to be checked:-",font=("ArialBold",15))
txt3 = ScrolledText(window, width=20, height=5, font=("Arial", 12),cursor='dot',relief="raised")
l2.place(x=0,y=480,anchor="nw")
txt3.place(x=280,y=480)
l2=tk.Label(window,text="Enter the upper bound of allowed copied content :- ",font=("ArialBold",9))
l2.place(x=0,y=585)
txt101=Entry(window,width=6,bd=0.5,cursor='dot',font=("ArialBold",9),textvariable=number3)
txt101.place(x=285,y=585)
call_results=partial(call_results,number3)

bt2=Button(window,text="Check Plagriasm content",bg="cyan",fg="black",bd=3,activebackground="white",command=call_results)
bt2.place(x=175,y=612)
txt2 = ScrolledText(window, width=40, height=7, font=("Arial", 12))
txt2.place(x=75, y=650)

bt1=Button(window,text="Upload file and check Plagriasm content",bg="cyan",fg="black",bd=3,activebackground="white",command=call_result1)
bt1.place(x=130,y=230)


your_data = {'foo': 'bar'}

# Store data (serialize)

flag100=0
with open('filename.pickle', 'rb') as handle:
    try:
        cache=pickle.load(handle)
    except:
        flag100=1

if flag100==1:
    with open('filename.pickle','wb') as handle:
        pickle.dump({1:2}, handle, protocol=pickle.HIGHEST_PROTOCOL)

window.mainloop()