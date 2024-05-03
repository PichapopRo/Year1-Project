import tkinter as tk
from tkinter import ttk
from processing import *


class UI:
    def __init__(self):
        self.window = tk.Tk()
        self.graph = None
        self.total_price_value = 0
        self.init_components()
        self.selected_item_name = ""
        self.previous_component = None
        self.previous_price = 0
        self.selected_component = None
        self.selected_price = 0
        self.selected_components = {}

    def init_components(self):
        self.window.title('PC Part Picker')
        self.window.geometry("700x400")

        self.comparison_button = tk.Button(self.window, text='Comparison',
                                           command=self.comparison_handler, width=10, height=1)
        self.comparison_button.grid(row=0, column=0, sticky='nw')

        # Component frame
        self.components_frame = tk.Frame(self.window)
        self.components_frame.grid(row=1, column=0, sticky='nsew', padx=50, pady=20)

        self.cpu_button = tk.Button(self.components_frame, command=self.cpu_handler, text='CPU',
                                    width=20)
        self.cpu_button.pack(fill='both', pady=5)
        self.mb_button = tk.Button(self.components_frame, command=self.mb_handler,
                                   text='Motherboard', width=20)
        self.mb_button.pack(fill='both', pady=5)
        self.gpu_button = tk.Button(self.components_frame, command=self.gpu_handler, text='GPU',
                                    width=20)
        self.gpu_button.pack(fill='both', pady=5)
        self.ram_button = tk.Button(self.components_frame, command=self.ram_handler, text='RAM',
                                    width=20)
        self.ram_button.pack(fill='both', pady=5)
        self.ssd_button = tk.Button(self.components_frame, command=self.ssd_handler, text='SSD',
                                    width=20)
        self.ssd_button.pack(fill='both', pady=5)
        self.hdd_button = tk.Button(self.components_frame, command=self.hdd_handler, text='HDD',
                                    width=20)
        self.hdd_button.pack(fill='both', pady=5)
        self.build_button = tk.Button(self.components_frame, command=self.cpu_handler, text='Build',
                                      width=10)
        self.build_button.pack(side='bottom', pady=10)

        # Total price label
        self.total_price_label = tk.Label(self.components_frame,
                                          text=f'Total Price : {self.total_price_value}',
                                          font=('Arial', 11))
        self.total_price_label.pack(side='left', pady=10)

        # Selection frame
        self.sort_item_selection_frame = tk.Frame(self.window)
        self.sort_item_selection_frame.grid(row=0, column=1, sticky='n')

        self.selection_msg = tk.Label(self.sort_item_selection_frame,
                                      text="Select your component to access to sort (Haven't done sort)")
        self.selection_msg.pack(pady=5)

        # Price range entry
        self.price_range_label = tk.Label(self.sort_item_selection_frame, text='Price Range:')
        self.price_range_label.pack(side='left', padx=5)

        self.price_range_entry1 = tk.Entry(self.sort_item_selection_frame, width=10)
        self.price_range_entry1.pack(side='left')

        self.dash_label = tk.Label(self.sort_item_selection_frame, text='-')
        self.dash_label.pack(side='left', padx=5)

        self.price_range_entry2 = tk.Entry(self.sort_item_selection_frame, width=15)
        self.price_range_entry2.pack(side='left')
        # listbox
        self.product_tree = ttk.Treeview(self.window, columns=('Name', 'Price'), height=13)
        self.product_tree.heading('#0', text='Number')
        self.product_tree.heading('Name', text='Name')
        self.product_tree.heading('Price', text='Price')
        self.product_tree.column('#0', width=60)
        self.product_tree.column('Name', width=250)
        self.product_tree.column('Price', width=100)
        self.product_tree.grid(row=1, column=1)
        self.product_tree.bind('<<TreeviewSelect>>', self.on_item_select)

    def comparison_handler(self):
        self.comparison_button.destroy()
        self.sort_item_selection_frame.destroy()
        self.components_frame.destroy()
        self.product_tree.destroy()

    def build_handler(self):
        pass

    def cpu_handler(self):
        self.product_tree.delete(*self.product_tree.get_children())
        number = 1
        for index, cpu in CPU_data.iterrows():
            self.product_tree.insert('', 'end', text=f'{number}',
                                     values=(cpu['Name'], f"{cpu['Price']} Baht"))
            number += 1
        self.selected_button = self.cpu_button

    def gpu_handler(self):
        self.product_tree.delete(*self.product_tree.get_children())
        number = 1
        for index, gpu in gpu_data.iterrows():
            self.product_tree.insert('', 'end', text=f'{number}',
                                     values=(gpu['Name'], f"{gpu['Price']} Baht"))
            number += 1
        self.selected_button = self.gpu_button

    def mb_handler(self):
        self.product_tree.delete(*self.product_tree.get_children())
        number = 1
        for index, mb in mb_data.iterrows():
            self.product_tree.insert('', 'end', text=f'{number}',
                                     values=(mb['Name'], f"{mb['Price']} Baht"))
            number += 1
        self.selected_button = self.mb_button

    def ssd_handler(self):
        self.product_tree.delete(*self.product_tree.get_children())
        number = 1
        for index, ssd in ssd_data.iterrows():
            self.product_tree.insert('', 'end', text=f'{number}',
                                     values=(ssd['Name'], f"{ssd['Price']} Baht"))
            number += 1
        self.selected_button = self.ssd_button

    def hdd_handler(self):
        self.product_tree.delete(*self.product_tree.get_children())
        number = 1
        for index, hdd in hdd_data.iterrows():
            self.product_tree.insert('', 'end', text=f'{number}',
                                     values=(hdd['Name'], f"{hdd['Price']} Baht"))
            number += 1
        self.selected_button = self.hdd_button

    def ram_handler(self):
        self.product_tree.delete(*self.product_tree.get_children())
        number = 1
        for index, ram in ram_data.iterrows():
            self.product_tree.insert('', 'end', text=f'{number}',
                                     values=(ram['Name'], f"{ram['Price']} Baht"))
            number += 1
        self.selected_button = self.ram_button

    def button_handler(self, handler):
        self.product_tree.delete(*self.product_tree.get_children())
        number = 1
        for index, item in handler['data'].iterrows():
            self.product_tree.insert('', 'end', text=f'{number}',
                                     values=(item['Name'], f"{item['Price']} Baht"))
            number += 1

    def on_item_select(self, event):
        selected_item = self.product_tree.item(self.product_tree.selection())['values']
        if selected_item:
            name, price = selected_item
            price = int(price.split()[0])
            if name in self.selected_components:
                self.total_price_value -= self.selected_components[name]
            self.selected_components[name] = price
            self.total_price_value += price
            self.total_price_label.config(text=f'Total Price: {self.total_price_value} Baht')
            self.update_button(self.selected_button, name)

    def update_button(self, button, selected_item_name=None):
        if selected_item_name:
            self.selected_item_name = selected_item_name
            button.config(text=self.selected_item_name)
        else:
            button.config(text=button.cget('text').split(':')[0])

    def run(self):
        self.window.mainloop()

class SecondPage:
    def __init__(self, window: tk.Tk()):
        self.window = window



Ui = UI()
Ui.run()
