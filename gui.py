#!/usr/bin/env python
#
#    This file is part of <Crystal Spells Package>
#
#    Copyright Xiaoyu Wang (xwang224@buffalo.edu)
#
#    Department of Wizardary and Alchemical Engineering
#    State University of New York at Buffalo, U.S.A.
#
#    Fall 2019
#
#    "gui.py"
#
#    This script set-up a graphical user interface

import sys
try:
    import Tkinter as tk
except ImportError:
    print("Error import Tkinter, which is critical for the GUI")
    sys.exit(-1)
import crystal

class Application(object):

    def __init__(self, master):
        self.master = master

        tk.Label(
            master,
            text = "Hello Tkinter!",
            ).pack()

        file_manager = tk.Toplevel(
            self.master,
            width = 600,
            height = 100,
            )

        FileManager(file_manager)

class FileManager(object):

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(
            self.master,
            text = "Second Window"
            ).pack()
        self.frame.pack()


def main():

    root = tk.Tk()
    root.geometry("400x500")
    root.resizable(0, 0)

    app = Application(root)
    root.mainloop()


if __name__ == "__main__":

    main()
