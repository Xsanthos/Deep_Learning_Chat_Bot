from Functions import *
from tkinter.ttk import *
from tkinter import *
import tkinter as tk


def gui():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Spectral Analyser")
    root.configure(bg="#84817a")
    root.geometry("900x640")

    # Creating Frame
    frame = tk.Frame(root, bg="#aaa69d")
    frame.place(relwidth=0.95, relheight=0.95, relx=0.025, rely=0.025)

    # Embedding Terminal
    TextField = tk.Text(frame, bg="#222222", fg="#9e1a1a", width=82, height=20)
    TextField.grid(row=5, column=1)

    # Creating Labels
    label1 = tk.Label(frame, text="Vegitation Index \nAnalyser", font=('calibri', 10, 'italic'),
                      bg=("#aaa69d"))
    label1.grid(row=2, column=0)

    label2 = tk.Label(frame, text="Water Index \nAnalyser", font=('calibri', 10, 'italic'), bg=("#aaa69d"))
    label2.grid(row=2, column=2)

    label3 = tk.Label(frame, text="Infrared \nAnalyser", font=('calibri', 10, 'italic'), bg=("#aaa69d"))
    label3.grid(row=4, column=0)

    Title = tk.Label(frame, text="Spectral Analyser", font=('calibri', 36, 'bold'), bg=("#aaa69d"))
    Title.grid(row=1, column=1, sticky=N + E + W + S)

    SubTitle = tk.Label(frame, text="  This application allows \nusers to calculate NDVI,\n NDWI and IR values and\n "
                                    "save them as images  ", font=('calibri', 14), bg=("#aaa69d"))
    SubTitle.grid(row=3, column=1, sticky=N + E + W + S)

    # GUI functions
    def onClickNDVI():
        TextField.delete(1.0, tk.END)
        prompt = "Please rename your file:--- \n"
        TextField.insert(tk.END, prompt)
        NDVI()
        time.sleep(5)
        TextField.delete(1.0, tk.END)
        Name = TextField.get(1.0, tk.END)
        renameFile(Name)

    def onClickThermal():
        TextField.delete(1.0, tk.END)
        prompt = "Please rename your file:--- \n"
        TextField.insert(tk.END, prompt)
        thermalIR()
        time.sleep(5)
        TextField.delete(1.0, tk.END)
        Name = TextField.get(1.0, tk.END)
        renameFile(Name)
        renameFile(Name)

    def onClickNDWI():
        TextField.delete(1.0, tk.END)
        prompt = "Please rename your file:--- \n"
        TextField.insert(tk.END, prompt)
        NDWI()
        time.sleep(5)
        TextField.delete(1.0, tk.END)
        Name = TextField.get(1.0, tk.END)
        renameFile(Name)
        renameFile(Name)

    def Quit():
        root.destroy()

    # Creating Button
    btn1 = Button(frame, text="NDVI", font=('calibri', 20, 'bold'), fg="#9e1a1a", bg="#84817a", state="normal",
                  command=onClickNDVI, borderwidth='2')
    btn1.grid(row=1, column=0)

    btn2 = Button(frame, text="NDWI", font=('calibri', 20, 'bold'), fg="#9e1a1a", bg="#84817a", state="normal",
                  command=onClickNDWI, borderwidth='2')
    btn2.grid(row=1, column=2)

    btn3 = Button(frame, text="   IR   ", font=('calibri', 20, 'bold'), fg="#9e1a1a", bg="#84817a", state="normal",
                  command=onClickThermal, borderwidth='2')
    btn3.grid(row=3, column=0)

    btn4 = Button(frame, text="  Quit  ", font=('calibri', 20, 'bold'), fg="#9e1a1a", bg="#84817a", state="normal",
                  command=Quit, borderwidth='2')
    btn4.grid(row=3, column=2)

    root.mainloop()


def main():
    gui()


main()
