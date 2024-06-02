import tkinter as tk
from tkinter import ttk

from octal import *
from Dec_Pra_Hexa import *
from Binario_Pra_Dec import *
from dec_para_bin import *
from dec_para_octal import *

root = tk.Tk()
root.title("Conversores de Bases")
root.geometry("300x600")

option_from = tk.StringVar()
option_from.set("Decimal")

option_to = tk.StringVar()
option_to.set("Decimal")


in_frame = ttk.Frame(root,padding=(10,10,10,10))
in_frame.pack()


frame_from = tk.LabelFrame(in_frame, text="Escolha a base de entrada",padx=10, pady=10)
frame_from.pack(padx=10, pady=10)

drop_from = tk.OptionMenu(frame_from, option_from, "Decimal", "Binario", "Octal", "Hexadecimal")
drop_from.pack()


frame_to = tk.LabelFrame(root, text="Escolha a base de saida",padx=10, pady=10)
frame_to.pack(padx=10, pady=10)

drop_to = tk.OptionMenu(frame_to, option_to, "Decimal", "Binario", "Octal", "Hexadecimal")
drop_to.pack()


label = tk.Label(in_frame, text="Insira um numero:")
label.pack()
input_entry = tk.Entry(in_frame)
input_entry.pack()


convert_button = tk.Button(root, text="Converter", command=lambda: convert_number(input_entry,option_from,option_to))
convert_button.pack()

result_label = tk.Label(in_frame, text="Resultado: ")
result_label.pack()






def convert_number(entry_widget, from_base, to_base):
    number_str = entry_widget.get()
    from_base_val = from_base.get()
    to_base_val = to_base.get()

    def is_valid_number(number_str, valid_chars):
        return all(char in valid_chars for char in number_str)

    # Validate the input based on the selected 'from' base
    if from_base_val == "Binario":
        if not is_valid_number(number_str, '01.'):
            print("entradas binarias devem consistir apenas de digitos 0 e 1")
            result_label.config(text="Result: ")
            return
        decimal_num = binario_para_decimal(number_str)
    elif from_base_val == "Octal":
        if not is_valid_number(number_str, '01234567.'):
            print("entradas octais devem consistir apenas de digitos 0-7")
            result_label.config(text="Result: ")
            return
        decimal_num = octal_to_decimal(number_str)
    elif from_base_val == "Hexadecimal":
        if not is_valid_number(number_str, '0123456789ABCDEFabcdef.'):
            print("entradas hexadecimais devem consistir apenas de digitos 0-9 e A-F")
            result_label.config(text="Result: ")
            return
        decimal_num = hex_to_decimal(number_str)
    elif from_base_val == "Decimal":
        if '.' in number_str:
            if not number_str.replace('.', '', 1).isdigit():
                print("Por favor, insira um numero decimal valido.")
                result_label.config(text="Result: ")
                return
            decimal_num = float(number_str)
        else:
            if not number_str.isdigit():
                print("Por favor, insira um numero decimal valido.")
                result_label.config(text="Result: ")
                return
            decimal_num = int(number_str)
    else:
        print("Por favor, selecione uma base de entrada")
        result_label.config(text="Result: ")
        return

    if to_base_val == "Decimal":
        result = str(decimal_num)
    elif to_base_val == "Binario":
        result = converter_decimal_pra_binario(decimal_num)
    elif to_base_val == "Octal":
        result = dec_pra_octal(decimal_num)
    elif to_base_val == "Hexadecimal":
        result = dec_pra_hexa(decimal_num)
    else:
        print("Por favor, selecione uma base de saida")
        result_label.config(text="Result: ")
        return

    result_label.config(text=f"Result: {result}")



root.mainloop()