import os
import sys
import threading
import tkinter as tk

os.chdir(os.getcwd())

self = tk.Tk()
self.title("meet")
self.resizable(0, 0)
self.grid()


def strt():
    os.system("python main.py")


def exc():
    os.startfile("schedule.xlsx")


def lnk():
    os.startfile("meet-link.json")


def gdsch():
    os.startfile("guide-schedule.txt")


def gdlnk():
    os.system("guide-links.txt")


ch_time = tk.Button(self, text="CHANGE SCHEDULE", command=exc)
ch_time.grid(row=0, column=0, sticky="nswe")
ch_link = tk.Button(self, text="CHANGE LINKS", command=lnk)
ch_link.grid(row=0, column=1, sticky="nswe")
guid_time = tk.Button(self, text="guide schedule", command=gdsch)
guid_time.grid(row=1, column=0, sticky="nswe")
guid_link = tk.Button(self, text="guide links", command=gdlnk)
guid_link.grid(row=1, column=1, sticky="nswe")
start = tk.Button(
    self, text="START", bg="green", activebackground="green", command=strt
)
start.grid(row=2, column=0, sticky="nswe")
bad_gui = tk.Label(self, text="This is a really bad GUI :)")
bad_gui.grid(row=3, column=0, sticky="nswe")
me = tk.Label(self, text="made with <3 by DanyB0")
me.grid(row=3, column=1, sticky="nswe")

if __name__ == "__main__":
    self.mainloop()
