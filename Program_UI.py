import tkinter as tk
from processing import *


class UI:
    def __init__(self):
        self.window = tk.Tk()
        self.graph = None
        self.total_price_value = 0
        self.init_components()

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

        self.mb_button = tk.Button(self.components_frame, command=self.cpu_handler,
                                   text='Motherboard', width=20)
        self.mb_button.pack(fill='both', pady=5)

        self.gpu_button = tk.Button(self.components_frame, command=self.cpu_handler, text='GPU',
                                    width=20)
        self.gpu_button.pack(fill='both', pady=5)

        self.ram_button = tk.Button(self.components_frame, command=self.cpu_handler, text='RAM',
                                    width=20)
        self.ram_button.pack(fill='both', pady=5)

        self.ssd_button = tk.Button(self.components_frame, command=self.cpu_handler, text='SSD',
                                    width=20)
        self.ssd_button.pack(fill='both', pady=5)

        self.hdd_button = tk.Button(self.components_frame, command=self.cpu_handler, text='HDD',
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

        self.price_range_entry2 = tk.Entry(self.sort_item_selection_frame, width=10)
        self.price_range_entry2.pack(side='left')
        # listbox
        self.product_list = tk.Listbox(self.window,height=15, width=70)
        self.product_list.grid(row=1, column=1)

    def comparison_handler(self):
        pass

    def cpu_handler(self):
        pass

    def gpu_handler(self):
        pass

    def mb_handler(self):
        pass

    def ssd_handler(self):
        pass

    def hdd_handler(self):
        pass

    def run(self):
        self.window.mainloop()
