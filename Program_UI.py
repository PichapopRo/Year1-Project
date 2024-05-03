import tkinter as tk
from tkinter import ttk
from processing import *


class UI:
    def __init__(self, window: tk.Tk):
        self.window = window
        self.graph = None
        self.total_price_value = 0
        self.selected_item_name = ""
        self.previous_component = None
        self.previous_price = 0
        self.selected_component = None
        self.selected_price = 0
        self.selected_components = {}

        self.init_components()

    def init_components(self):
        self.window.title('PC Part Picker')
        self.window.geometry("700x400")

        # Create Notebook
        self.notebook = ttk.Notebook(self.window, width=700, height=400)
        self.notebook.pack(fill='both', expand=True)

        # First Page
        self.first_page = ttk.Frame(self.notebook)
        self.notebook.add(self.first_page, text='Build PC')
        self.init_first_page()

        self.init_second_page()

    def init_first_page(self):
        # Component frame
        self.components_frame = tk.Frame(self.notebook, width=700, height=400)
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
        self.build_button = tk.Button(self.components_frame, command=self.build_handler, text='Build',
                                      width=10)
        self.build_button.pack(side='bottom', pady=10)

        # Total price label
        self.total_price_label = tk.Label(self.components_frame,
                                          text=f'Total Price : {self.total_price_value}',
                                          font=('Arial', 11))
        self.total_price_label.pack(side='left', pady=10)

        # Selection frame
        self.sort_item_selection_frame = tk.Frame(self.notebook)
        self.sort_item_selection_frame.grid(row=0, column=1, sticky='n')

        self.selection_msg = tk.Label(self.sort_item_selection_frame,
                                      text="Select your component to access to sort (Haven't done sort)")
        self.selection_msg.grid(row=0, column=0, pady=5,
                                columnspan=7)

        # Price range label and entry
        self.price_range_label = tk.Label(self.sort_item_selection_frame, text='Price Range:')
        self.price_range_label.grid(row=1, column=0, padx=5)

        self.price_range_entry1 = tk.Entry(self.sort_item_selection_frame, width=15)
        self.price_range_entry1.grid(row=1, column=1)

        self.dash_label = tk.Label(self.sort_item_selection_frame, text='-')
        self.dash_label.grid(row=1, column=2, padx=5)

        self.price_range_entry2 = tk.Entry(self.sort_item_selection_frame, width=15)
        self.price_range_entry2.grid(row=1, column=3)
        # listbox
        self.product_tree = ttk.Treeview(self.notebook, columns=('Name', 'Price'), height=13)
        self.product_tree.heading('#0', text='Number')
        self.product_tree.heading('Name', text='Name')
        self.product_tree.heading('Price', text='Price')
        self.product_tree.column('#0', width=60)
        self.product_tree.column('Name', width=250)
        self.product_tree.column('Price', width=100)
        self.product_tree.grid(row=1, column=1)
        self.product_tree.bind('<<TreeviewSelect>>', self.on_item_select)

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

    def init_second_page(self):
        # Second Page
        self.second_page = ttk.Frame(self.notebook)
        self.notebook.add(self.second_page, text='Comparison')

        # Graph sort frame
        self.graph_sort_frame = tk.Frame(self.second_page)
        self.graph_sort_frame.pack(side='top', fill='x')

        # Components type label and combobox
        self.components_type_label = tk.Label(self.graph_sort_frame, text='Select part to compare:')
        self.components_type_label.grid(row=0, column=0, padx=5, pady=3)

        self.components_type_combobox = ttk.Combobox(self.graph_sort_frame, width=10,
                                                     values=['CPU', 'GPU', 'Motherboard', 'RAM',
                                                             'SSD', 'HDD'])
        self.components_type_combobox.grid(row=0, column=1, padx=5, pady=3)

        # Price range label, entries, and dash
        self.price_range_label = tk.Label(self.graph_sort_frame, text='Price range:')
        self.price_range_label.grid(row=0, column=2, padx=5, pady=3)

        self.price_range_entry1 = tk.Entry(self.graph_sort_frame, width=10)
        self.price_range_entry1.grid(row=0, column=3, padx=5, pady=3)

        self.dash_label = tk.Label(self.graph_sort_frame, text='-')
        self.dash_label.grid(row=0, column=4, padx=5, pady=3)

        self.price_range_entry2 = tk.Entry(self.graph_sort_frame, width=10)
        self.price_range_entry2.grid(row=0, column=5, padx=5, pady=3)

        # Things to compare label and combobox
        self.compare_topic_label = tk.Label(self.graph_sort_frame, text='What to compare:')
        self.compare_topic_label.grid(row=1, column=0, padx=5, pady=3, sticky='w')

        self.compare_combo = ttk.Combobox(self.graph_sort_frame, width=10, values=['None'])
        self.compare_combo.grid(row=1, column=1, padx=5, sticky='w')

        # Type of graph label and combobox
        self.graph_type_label = tk.Label(self.graph_sort_frame, text='Select graph type:')
        self.graph_type_label.grid(row=2, column=0, padx=5, pady=3, sticky='w')

        self.graph_type_combo = ttk.Combobox(self.graph_sort_frame, width=10,
                                             values=['Bar Chart', 'Histogram'])
        self.graph_type_combo.grid(row=2, column=1, pady=3, sticky='w')

        # Overall Comparison
        self.overall_comparison = tk.Checkbutton(self.graph_sort_frame,text='Overall Comparison')
        self.overall_comparison.grid(row=3,column=0)
        # list of comparing product
        self.list_of_product_label = tk.Label(self.graph_sort_frame, text='List of product')
        self.list_of_product_label.grid(row=4,column=0, sticky='w', padx=5)
        self.product_listbox = tk.Listbox(self.graph_sort_frame, width=30, height=13)
        self.product_listbox.grid(row=5,column=0, padx=5, columnspan=1)
        # plot button
        self.plot_button = tk.Button(self.graph_sort_frame, height=1, width=6,text='Plot')
        self.plot_button.grid(row=6,column=0, pady=1, padx=5, sticky='w')
        # select button
        self.select_button = tk.Button(self.graph_sort_frame, height=1, width=6, text='Select')
        self.select_button.grid(row=6, column=0, pady=1, padx=5,columnspan=2, sticky='n')

    def run(self):
        self.window.mainloop()


window = tk.Tk()
Ui = UI(window)
Ui.run()
