import os
import threading
import tkinter as tk

os.chdir(os.getcwd())

self = tk.Tk()
self.title("meet")
self.resizable(0, 0)
self.grid()

def stop():
    os.startfile("stop.bat")


def strt():
    os.system("python main.py")


def exc():
    os.startfile("orario.xlsx")


def lnk():
    os.startfile("meet-link.json")


def gdsch():
    os.startfile("guide-schedule.txt")


def gdlnk():
    os.system("guide-links.txt")


ch_time = tk.Button(self, text="CHANGE SCHEDULE ", command=exc).grid(row=0, column=0, sticky="nsw")
ch_link = tk.Button(self, text=" CHANGE LINKS  ", command=lnk).grid(row=0, column=1, sticky="nsw")
guid_time = tk.Button(self, text="    guide schedule      ", command=gdsch).grid(row=1, column=0, sticky="nsw")
guid_link = tk.Button(self, text="     guide links      ", command=gdlnk).grid(row=1, column=1, sticky="nsw")
start = tk.Button(self, text="             START             ", bg="green", activebackground="green", command=strt).grid(row=2, column=0, sticky="nsw")
bad_gui = tk.Label(self, text="really bad GUI :)").grid(row=2, column=1, sticky="nsw")

if __name__ == "__main__":
    self.mainloop()
