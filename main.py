"""
Editor de Texto - Algoritmo Boye-Moore
Seminario de Solución de Problemas de Algoritmia
Created By: Isaac Eduardo Sánchez Campos
Código: 211172172
"""

import tkinter as tk
import sys
import os
from tkinter import ttk
from tkinter.ttk import *
import random
from random import shuffle
from tkinter import messagebox as mb

class last_occurrence(object):
    def __init__(self, pattern, alphabet):
        self.occurrences = dict()
        for letter in alphabet:
            self.occurrences[letter] = pattern.rfind(letter)
    def __call__(self, letter):
        return self.occurrences[letter]

def boyer_moore_match(text, pattern):
    alphabet = set(text)
    last = last_occurrence(pattern, alphabet)
    m = len(pattern)
    n = len(text)
    i = m - 1
    j = m - 1

    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last(text[i])
            i = i + m - min(j, 1+l)
            j = m - 1
    return -1

class Application:

    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Editor de Texto | Boyer-Moore")
        archivo = open("file.txt", "r")
        readed = archivo.read()
        print(readed)
        self.text = str(readed)
        self.canvas=tk.Canvas(self.window, width=800, height=800, background="white")
        self.name_label=tk.Label(self.window,text="Buscar:")
        self.name_label.grid(column=1, row=0)
        self.name=tk.StringVar()
        self.name_input=tk.Entry(self.window, width=50, textvariable=self.name)
        self.name_input.grid(column=1, row=4)
        self.name_label=tk.Label(self.window,text="Contenido del Archivo:")
        self.name_label.grid(column=1, row=8)
        self.file_name=tk.StringVar()
        self.file_name.set(self.text)
        self.file_content = tk.Entry(self.window, width=90, state="readonly", textvariable=self.file_name)
        self.file_content.grid(column=1, row=12)
        self.add_button=tk.Button(self.window, text="Buscar", command=self.show_match)
        self.add_button.grid(column=1, row=18)

        self.window.mainloop()

    def show_match(self):
        text = self.text
        pattern = self.name.get()
        print(text)
        print(pattern)
        p = boyer_moore_match(text, pattern)
        if p > 1:
            print('Match: %s%s' % ('.'*p, pattern))
            mb.showinfo("Alerta", "Cadena encontrada en el archivo. " + "Match: %s%s" % ("."*p, pattern))
        else:
            mb.showinfo("Alerta", "No existe coincidencia con esa cadena.")

    def search(self):
        mb.showinfo("Alerta", "No existe coincidencia con esa cadena.")

    def ingresar(self):
        self.window.title(self.name.get())
        name = self.name.get()

    def exit(self):
        sys.exit(0)

application = Application()
