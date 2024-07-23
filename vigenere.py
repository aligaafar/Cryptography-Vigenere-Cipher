# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 18:05:18 2022

@author: Lenovo
"""
#Vigenere Cipher
import re
import tkinter as tk
from tkinter import messagebox
from tkinter import *


E_dic ={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z"}
A_dic ={0:"ا",1:"ب",2:"ت",3:"ث",4:"ج",5:"ح",6:"خ",7:"د",8:"ذ",9:"ر",10:"ز",11:"س",12:"ش",13:"ص",14:"ض",15:"ط",16:"ظ",17:"ع",18:"غ",19:"ف",20:"ق",21:"ك",22:"ل",23:"م",24:"ن",25:"ه",26:"و",27:"ي"}
A_reg = re.compile(r'[ا-ي]')
E_reg = re.compile(r'[A-Z]')
def E_Encrypt():
    cipher=""
    plain=E_plain.get()
    plain=plain.replace(" ","")
    plain=plain.upper()
    if E_var.get()==2:
        key_int=E_key.get()
        key=str(key_int)
        if key.isdigit() and len(plain)==len(key):
            if E_reg.match(plain) and plain.isalpha():
                for p,kl in zip(plain,key):
                    pk = [k for k, v in E_dic.items() if v == p][0]
                    kk = int(kl)
                    n=(pk+kk)%26
                    cipher += E_dic[n]
                #E_Enc_Result.set(cipher)
                E_cipher.delete(0,END)
                E_cipher.insert(0,cipher)
            else:
                messagebox.showerror('Invalid Input','Only English letters are allowed!')
        else:
            messagebox.showerror('Invalid Input','Invalid OTP key!')
    else:
        key=E_key.get()
        key=key.upper()
        if E_reg.match(plain) and E_reg.match(key) and plain.isalpha() and key.isalpha():
            key=key*(len(plain)//len(key))+key[:len(plain)%len(key)]
            for p,kl in zip(plain,key):
                pk = [k for k, v in E_dic.items() if v == p][0]
                kk = [k for k, v in E_dic.items() if v == kl][0]
                n=(pk+kk)%26
                cipher += E_dic[n]
            #E_Enc_Result.set(cipher)
            E_cipher.delete(0,END)
            E_cipher.insert(0,cipher)
            print(cipher)
            #print(E_var.get())
        else:
            messagebox.showerror('Invalid Input','Only English letters are allowed!')

def E_Decrypt():
    plain=""
    cipher=E_cipher.get()
    cipher=cipher.replace(" ","")
    cipher=cipher.upper()
    if E_var.get()==2:
        key_int=E_key.get()
        key=str(key_int)
        if key.isdigit() and len(cipher)==len(key):
            if E_reg.match(cipher) and cipher.isalpha():
                for c,kl in zip(cipher,key):
                    ck = [k for k, v in E_dic.items() if v == c][0]
                    kk = int(kl)
                    n=(ck-kk)%26
                    plain += E_dic[n]
                #E_Dec_Result.set(plain)
                E_plain.delete(0,END)
                E_plain.insert(0,plain)
            else:
                messagebox.showerror('Invalid Input','Only English letters are allowed!')
        else:
            messagebox.showerror('Invalid Input','Invalid OTP key!')
    else:
        key=E_key.get()
        key=key.upper()
        if E_reg.match(cipher) and E_reg.match(key) and cipher.isalpha() and key.isalpha():
            key=key*(len(cipher)//len(key))+key[:len(cipher)%len(key)]
            for c,kl in zip(cipher,key):
                ck = [k for k, v in E_dic.items() if v == c][0]
                kk = [k for k, v in E_dic.items() if v == kl][0]
                n=(ck-kk)%26
                plain += E_dic[n]
            #E_Dec_Result.set(plain)
            E_plain.delete(0,END)
            E_plain.insert(0,plain)
            print(plain)
            #print(E_var.get())
        else:
            messagebox.showerror('Invalid Input','Only English letters are allowed!')

def A_Encrypt():
    cipher=""
    plain=A_plain.get()
    plain=plain.replace(" ","")
    #plain=plain.upper()
    if A_var.get()==2:
        key_int=A_key.get()
        key=str(key_int)
        if key.isdigit() and len(plain)==len(key):
            if A_reg.match(plain) and plain.isalpha():
                for p,kl in zip(plain,key):
                    pk = [k for k, v in A_dic.items() if v == p][0]
                    kk = int(kl)
                    n=(pk+kk)%28
                    cipher += A_dic[n]
                #A_Enc_Result.set(cipher)
                A_cipher.delete(0,END)
                A_cipher.insert(0,cipher)
            else:
                messagebox.showerror('Invalid Input','Only Arabic letters are allowed!')
        else:
            messagebox.showerror('Invalid Input','Invalid OTP key!')
    else:
        key=A_key.get()
        #key=key.upper()
        if A_reg.match(plain) and A_reg.match(key) and plain.isalpha() and key.isalpha():
            key=key*(len(plain)//len(key))+key[:len(plain)%len(key)]
            for p,kl in zip(plain,key):
                pk = [k for k, v in A_dic.items() if v == p][0]
                kk = [k for k, v in A_dic.items() if v == kl][0]
                n=(pk+kk)%28
                cipher += A_dic[n]
            #A_Enc_Result.set(cipher)
            A_cipher.delete(0,END)
            A_cipher.insert(0,cipher)
            print(cipher)
            #print(E_var.get())
        else:
            messagebox.showerror('Invalid Input','Only Arabic letters are allowed!')
    
def A_Decrypt():
    plain=""
    cipher=A_cipher.get()
    cipher=cipher.replace(" ","")
    cipher=cipher.upper()
    if A_var.get()==2:
        key_int=A_key.get()
        key=str(key_int)
        if key.isdigit() and len(cipher)==len(key):
            if A_reg.match(cipher) and cipher.isalpha():
                for c,kl in zip(cipher,key):
                    ck = [k for k, v in A_dic.items() if v == c][0]
                    kk = int(kl)
                    n=(ck-kk)%28
                    plain += A_dic[n]
                #A_Dec_Result.set(plain)
                A_plain.delete(0,END)
                A_plain.insert(0,plain)
            else:
                messagebox.showerror('Invalid Input','Only Arabic letters are allowed!')
        else:
            messagebox.showerror('Invalid Input','Invalid OTP key!')
    else:
        key=A_key.get()
        key=key.upper()
        if A_reg.match(cipher) and A_reg.match(key) and cipher.isalpha() and key.isalpha():
            key=key*(len(cipher)//len(key))+key[:len(cipher)%len(key)]
            for c,kl in zip(cipher,key):
                ck = [k for k, v in A_dic.items() if v == c][0]
                kk = [k for k, v in A_dic.items() if v == kl][0]
                n=(ck-kk)%28
                plain += A_dic[n]
            #A_Dec_Result.set(plain)
            A_plain.delete(0,END)
            A_plain.insert(0,plain)
            print(plain)
            #print(E_var.get())
        else:
            messagebox.showerror('Invalid Input','Only Arabic letters are allowed!')
            
#GUI part            
#---------------------------------------------------------------------------------------
master = tk.Tk()
master.geometry('500x300')
master.title('Vigenere Cipher')
master.configure(background='#ccffff')
tk.Label(master, text='For English',font=("Helvetica", 13),fg='#005580',bg='#ccffff', pady=5, padx=5).grid(row=0)
tk.Label(master, text='Key',bg='#ccffff',fg='#270c0c').grid(row=1)
E_key = tk.Entry(master,bg="#f2f2f2")
E_key.grid(row=1, column=1)

E_var = tk.IntVar()
E_Rad1 = tk.Radiobutton(master, text="Auto key", variable=E_var, value=1,bg='#ccffff')
E_Rad2 = tk.Radiobutton(master, text="OTP", variable=E_var, value=2,bg='#ccffff')
E_Rad1.grid(row=1, column=2)
E_Rad2.grid(row=1, column=3)

tk.Label(master, text='Plain Text',bg='#ccffff',fg='#270c0c').grid(row=2)
tk.Label(master, text='Cipher Text',bg='#ccffff',fg='#270c0c').grid(row=3)
E_plain= tk.Entry(master,bg="#f2f2f2")
E_cipher= tk.Entry(master,bg="#f2f2f2")
E_plain.grid(row=2, column=1)
E_cipher.grid(row=3, column=1)
button1 = tk.Button(master, text='Encrypt', width=15, command=lambda: E_Encrypt(),bg='#005580',fg='white')
button2 = tk.Button(master, text='Decrypt', width=15, command=lambda: E_Decrypt(),bg='#005580',fg='white')
button1.grid(row=2, column=2,padx=10, pady=5)
button2.grid(row=3, column=2,padx=10, pady=5)
E_Enc_Result=tk.StringVar()
E_Dec_Result=tk.StringVar()
#result=tk.Label(master, text='Result',bg='#009999',fg='white').grid(row=1,column=3)
E_R1= tk.Label(master,textvariable = E_Enc_Result,bg='#ccffff',fg='#270c0c')
E_R2=tk.Label(master,textvariable = E_Dec_Result,bg='#ccffff',fg='#270c0c')
E_R1.grid(row=2, column=3)
E_R2.grid(row=3, column=3)

tk.Label(master,fg='#005580',bg='#ccffff', pady=5).grid(row=4)

tk.Label(master, text='For Arabic',font=("Helvetica", 13),fg='#005580',bg='#ccffff', pady=5, padx=5).grid(row=5)
tk.Label(master, text='Key',bg='#ccffff',fg='#270c0c').grid(row=6)
A_key = tk.Entry(master,bg="#f2f2f2")
A_key.grid(row=6, column=1)

A_var = tk.IntVar()
A_Rad1 = tk.Radiobutton(master, text="Auto key", variable=A_var, value=1,bg='#ccffff')
A_Rad2 = tk.Radiobutton(master, text="OTP", variable=A_var, value=2,bg='#ccffff')
A_Rad1.grid(row=6, column=2)
A_Rad2.grid(row=6, column=3)

tk.Label(master, text='Plain Text',bg='#ccffff',fg='#270c0c').grid(row=7)
tk.Label(master, text='Cipher Text',bg='#ccffff',fg='#270c0c').grid(row=8)
A_plain= tk.Entry(master,bg="#f2f2f2")
A_cipher= tk.Entry(master,bg="#f2f2f2")
A_plain.grid(row=7, column=1)
A_cipher.grid(row=8, column=1)
button3 = tk.Button(master, text='Encrypt', width=15, command=lambda: A_Encrypt(),bg='#005580',fg='white')
button4 = tk.Button(master, text='Decrypt', width=15, command=lambda: A_Decrypt(),bg='#005580',fg='white')
button3.grid(row=7, column=2,padx=10, pady=5)
button4.grid(row=8, column=2,padx=10, pady=5)
'''
A_Enc_Result=tk.StringVar()
A_Dec_Result=tk.StringVar()
#result=tk.Label(master, text='Result',bg='#009999',fg='white').grid(row=1,column=3)
A_R1= tk.Label(master,textvariable = A_Enc_Result,bg='#ccffff',fg='#270c0c')
A_R2=tk.Label(master,textvariable = A_Dec_Result,bg='#ccffff',fg='#270c0c')
A_R1.grid(row=7, column=3)
A_R2.grid(row=8, column=3)
'''
master.mainloop()