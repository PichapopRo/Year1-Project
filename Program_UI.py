import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from product_value import *

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
        self.init_components()
        self.selected_item = []
        self.selected_components = {}

    def init_components(self):
        self.window.title('PC Part Picker')
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        # Create Menu Bar
        menubar = tk.Menu(self.window)
        menubar.add_cascade(label="Exit", command=self.exit_program)
        self.window.config(menu=menubar)

        # Create Notebook
        self.notebook = ttk.Notebook(self.window, width=700, height=400)
        self.notebook.pack(fill='both', expand=True)

        # First Page
        self.first_page = ttk.Frame(self.notebook)
        self.notebook.add(self.first_page, text='Build PC')
        self.init_first_page()

        self.init_second_page()

    def exit_program(self):
        self.window.quit()

    def init_first_page(self):
        # Component frame
        self.components_frame = tk.Frame(self.notebook, width=700, height=400)
        self.components_frame.grid(row=1, column=0, sticky='nsew', padx=50, pady=20)
        self.components_frame.rowconfigure(0, weight=1)
        self.components_frame.columnconfigure(0, weight=1)

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
        self.build_button = tk.Button(self.components_frame, command=self.build_handler,
                                      text='Build',
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
        self.sort_item_selection_frame.rowconfigure(0, weight=1)
        self.sort_item_selection_frame.columnconfigure(1, weight=1)

        self.selection_msg = tk.Label(self.sort_item_selection_frame,
                                      text="")
        self.selection_msg.grid(row=0, column=0, pady=5)
        self.selection_msg.columnconfigure(0, weight=1)
        self.selection_msg.rowconfigure(0, weight=1)

        # Price range label and entry
        self.price_range_label = tk.Label(self.sort_item_selection_frame, text='Price Range:')
        self.price_range_label.grid(row=1, column=0, padx=5)
        self.price_range_label.columnconfigure(0, weight=1)
        self.price_range_label.rowconfigure(1, weight=1)

        self.price_range_entry1 = tk.Entry(self.sort_item_selection_frame, width=15)
        self.price_range_entry1.grid(row=1, column=1)
        self.price_range_entry1.columnconfigure(1, weight=1)
        self.price_range_entry1.rowconfigure(1, weight=1)

        self.dash_label = tk.Label(self.sort_item_selection_frame, text='-')
        self.dash_label.grid(row=1, column=2, padx=5)
        self.price_range_entry1.columnconfigure(2, weight=1)
        self.price_range_entry1.rowconfigure(1, weight=1)

        self.price_range_entry2 = tk.Entry(self.sort_item_selection_frame, width=15)
        self.price_range_entry2.grid(row=1, column=3)
        self.price_range_entry2.columnconfigure(3, weight=1)
        self.price_range_entry2.rowconfigure(1, weight=1)
        # Search box and label
        self.search_label = tk.Label(self.sort_item_selection_frame, text='Search:')
        self.search_label.grid(row=0, column=0, padx=5, pady=5)

        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.sort_item_selection_frame, textvariable=self.search_var)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        # Treeview for displaying components
        self.product_tree = ttk.Treeview(self.notebook, columns=('Name', 'Price'), height=13)
        self.product_tree.heading('#0', text='Number')
        self.product_tree.heading('Name', text='Name')
        self.product_tree.heading('Price', text='Price')
        self.product_tree.column('#0', width=60)
        self.product_tree.column('Name', width=250)
        self.product_tree.column('Price', width=100)
        self.product_tree.grid(row=1, column=1, padx=10)
        self.product_tree.columnconfigure(1, weight=1)
        self.product_tree.rowconfigure(1, weight=1)
        self.product_tree.bind('<<TreeviewSelect>>', self.on_item_select)
        self.search_entry.bind('<KeyRelease>', self.search_items)

    def search_items(self, event=None):
        search_query = self.search_var.get().lower()
        if not search_query:
            return
        all_items = [(self.product_tree.item(child, 'values'), child) for child in
                     self.product_tree.get_children()]
        filtered_items = [(item_values, child) for item_values, child in all_items if
                          item_values and search_query in item_values[0].lower()]
        self.product_tree.delete(*self.product_tree.get_children())
        filtered_items.sort(
            key=lambda x: x[0][0].lower())

        # Populate the treeview with the filtered and sorted items
        number = 1
        for item_values, child in filtered_items:
            self.product_tree.insert('', 'end', text=f'{number}', values=item_values)
            number += 1

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

    def on_item_select(self, event):
        selected_item = self.product_tree.item(self.product_tree.selection())['values']
        if selected_item:
            name, price = selected_item
            try:
                price = int(price.split()[0])
            except ValueError:
                return

            # Check if a component of the same category has already been selected
            category_selected = False
            components_copy = self.selected_components.copy()  # Create a copy of the dictionary
            for category, item_price in components_copy.items():
                if category != name.split()[0]:  # Compare category names
                    continue
                category_selected = True
                self.total_price_value -= item_price  # Subtract the price of the previous component
                self.selected_components.pop(category)  # Remove the previous component

            # Add the newly selected component
            self.selected_components[name.split()[0]] = price
            self.total_price_value += price

            # Update the total price label
            self.total_price_label.config(text=f'Total Price: {self.total_price_value} Baht')

            # Update the button label
            self.update_button(self.selected_button, name)

            # If a component of the same category was previously selected, update the button label
            if category_selected:
                self.update_button(self.selected_button)

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
        self.graph_sort_frame.pack(side='top', fill=tk.BOTH, expand=True)

        # Price range label, entries, and dash
        self.price_range_label = tk.Label(self.graph_sort_frame, text='Price range :')
        self.price_range_label.grid(row=1, column=1, padx=5, pady=3)
        self.price_range_label.columnconfigure(1, weight=1)
        self.price_range_label.rowconfigure(1, weight=1)

        self.price_range_entry1 = tk.Entry(self.graph_sort_frame, width=10)
        self.price_range_entry1.grid(row=2, column=1, padx=5, pady=1)
        self.price_range_label.columnconfigure(1, weight=1)
        self.price_range_label.rowconfigure(2, weight=1)

        self.dash_label = tk.Label(self.graph_sort_frame, text='-')
        self.dash_label.grid(row=3, column=1, padx=5, pady=1)
        self.dash_label.columnconfigure(1, weight=1)
        self.dash_label.rowconfigure(3, weight=1)

        self.price_range_entry2 = tk.Entry(self.graph_sort_frame, width=10)
        self.price_range_entry2.grid(row=4, column=1, padx=5, pady=1)
        self.price_range_entry2.columnconfigure(1, weight=1)
        self.price_range_entry2.rowconfigure(4, weight=1)

        # Components type label and combobox
        self.components_type_label = tk.Label(self.graph_sort_frame, text='Select part to compare:')
        self.components_type_label.grid(row=1, column=0, padx=5, pady=3, sticky='w')
        self.price_range_entry2.columnconfigure(0, weight=1)
        self.price_range_entry2.rowconfigure(1, weight=1)

        self.components_type_combobox = ttk.Combobox(self.graph_sort_frame, width=10,
                                                     values=['CPU', 'GPU', 'Motherboard', 'RAM',
                                                             'SSD', 'HDD'])
        self.components_type_combobox.grid(row=1, column=1, padx=1, pady=3, sticky='w')
        self.components_type_combobox.columnconfigure(1, weight=1)
        self.components_type_combobox.rowconfigure(1, weight=1)

        # Things to compare label and combobox
        self.compare_topic_label = tk.Label(self.graph_sort_frame, text='What to compare :')
        self.compare_topic_label.grid(row=2, column=0, padx=5, pady=3, sticky='w')
        self.compare_topic_label.columnconfigure(1, weight=1)
        self.compare_topic_label.rowconfigure(2, weight=1)

        self.compare_combo = ttk.Combobox(self.graph_sort_frame, width=10, values=['None'])
        self.compare_combo.grid(row=2, column=1, sticky='w')
        self.compare_combo.columnconfigure(1, weight=1)
        self.compare_combo.rowconfigure(2, weight=1)

        # Type of graph label and combobox
        self.graph_type_label = tk.Label(self.graph_sort_frame, text='Select graph type :')
        self.graph_type_label.grid(row=3, column=0, padx=5, pady=3, sticky='w')
        self.graph_type_label.columnconfigure(0, weight=1)
        self.graph_type_label.rowconfigure(3, weight=1)

        self.graph_type_combo = ttk.Combobox(self.graph_sort_frame, width=10,
                                             values=['Bar Chart', 'Histogram'])
        self.graph_type_combo.grid(row=3, column=1, pady=3, sticky='w')
        self.graph_type_combo.columnconfigure(1, weight=1)
        self.graph_type_combo.rowconfigure(3, weight=1)

        # Overall Comparison
        self.var = tk.IntVar()
        self.overall_comparison = tk.Checkbutton(self.graph_sort_frame, text='Overall Comparison',
                                                 variable=self.var)
        self.overall_comparison.grid(row=4, column=0, pady=3, sticky='w')
        self.overall_comparison.columnconfigure(0, weight=1)
        self.overall_comparison.rowconfigure(4, weight=1)

        # List of comparing product
        self.list_of_product_label = tk.Label(self.graph_sort_frame, text='List of product')
        self.list_of_product_label.grid(row=5, column=0, sticky='w', padx=5)
        self.product_listbox = tk.Listbox(self.graph_sort_frame, width=30, height=13)
        self.product_listbox.grid(row=6, column=0, padx=5, columnspan=1, sticky='w')
        self.product_listbox.columnconfigure(0, weight=1)
        self.product_listbox.rowconfigure(6, weight=1)

        # Plot and Select buttons
        self.plot_button = tk.Button(self.graph_sort_frame, height=1, width=6, text='Plot',
                                     command=self.plot_handler)
        self.plot_button.grid(row=7, column=0, pady=1, padx=5, sticky='w')
        self.plot_button.columnconfigure(0, weight=1)
        self.plot_button.rowconfigure(7, weight=1)

        # select button
        self.select_button = tk.Button(self.graph_sort_frame, height=1, width=6, text='Select',
                                       command=self.select_handler)
        self.select_button.grid(row=7, column=0, pady=1, padx=5, sticky='n')
        self.select_button.columnconfigure(0, weight=1)
        self.select_button.rowconfigure(7, weight=1)
        # Clear button
        self.clear_button = tk.Button(self.graph_sort_frame, height=1, width=6, text='Clear',
                                      command=self.clear_handler)
        self.clear_button.grid(row=7, column=0, pady=1, padx=5, sticky='e')
        self.clear_button.columnconfigure(0, weight=1)
        self.clear_button.rowconfigure(7, weight=1)

        # graph
        fig, ax = plt.subplots(figsize=(5, 2))
        fig.set_dpi(100)
        self.graph = FigureCanvasTkAgg(fig, master=self.graph_sort_frame)
        self.graph.get_tk_widget().grid(row=6, column=1, padx=5, sticky='nsew')
        self.graph.get_tk_widget().columnconfigure(1, weight=1)
        self.graph.get_tk_widget().rowconfigure(6, weight=1)
        self.components_type_combobox.bind('<<ComboboxSelected>>', self.load_filter)
        self.compare_combo.bind('<<ComboboxSelected>>')
        self.price_range_entry1.config(state='disabled')
        self.price_range_entry2.config(state='disabled')
        overall_comparison_checked = self.var
        if overall_comparison_checked == 1:
            self.graph_type_combo.config(state='readonly')
            self.price_range_entry1.config(state='normal')
            self.price_range_entry2.config(state='normal')

    def plot_handler(self):
        try:
            overall_comparison_checked = self.var.get()

            if overall_comparison_checked == 1:
                self.graph_type_combo['values'] = ['Histogram', 'Bar Chart']
            else:
                if self.product_listbox.size() == 0:
                    messagebox.showerror("Error",
                                         "Please select at least one product for comparison.")
                    return

            selected_graph_type = self.graph_type_combo.get()

            if self.graph is not None:
                self.graph.get_tk_widget().destroy()

            fig, ax = plt.subplots(figsize=(5, 2))
            fig.set_dpi(100)
            data = self.data_search(self.components_type_combobox.get())

            if selected_graph_type == 'Histogram':
                # Get the data to plot
                compare_attribute = self.compare_combo.get()
                data_to_plot = data[compare_attribute]

                # Plot histogram
                ax.hist(data_to_plot, bins=5)
                ax.set_xlabel('Value')
                ax.set_ylabel('Frequency')
                ax.set_title('Histogram')
            elif selected_graph_type == 'Bar Chart':
                values = []
                labels = self.product_listbox.get(0, tk.END)
                for item in labels:
                    for index, row in data.iterrows():
                        if row['Name'] == item:
                            values.append(row[self.compare_combo.get()])

                ax.bar(labels, values)
                ax.set_xlabel('Category')
                ax.set_ylabel('Value')
                ax.set_title('Bar Chart')

            # Grid the new graph
            self.graph = FigureCanvasTkAgg(fig, master=self.graph_sort_frame)
            self.graph.get_tk_widget().grid(row=6, column=1, padx=5)
            self.graph.get_tk_widget().columnconfigure(1, weight=1)
            self.graph.get_tk_widget().rowconfigure(6, weight=1)
        except Exception:
            messagebox.showerror("Error",
                                 "Please fill in all attribute")
            return

    def select_handler(self):
        self.select_window = tk.Tk()
        self.select_type_label = tk.Label(self.select_window, text='Select Component')
        self.select_type_label.pack(side='top', expand=True)

        # Search box
        self.search_label = tk.Label(self.select_window, text='Search:')
        self.search_label.pack(side='top', pady=5, expand=True)

        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.select_window, textvariable=self.search_var)
        self.search_entry.pack(side='top', padx=5, pady=5, fill='x', expand=True)

        # Create the treeview to display the selected items
        self.list_select = ttk.Treeview(self.select_window, columns=('Name', 'Price'), height=10)
        self.list_select.heading('#0', text='Number')
        self.list_select.heading('Name', text='Name')
        self.list_select.heading('Price', text='Price')
        self.list_select.column('#0', width=60)
        self.list_select.column('Name', width=250)
        self.list_select.column('Price', width=100)
        self.list_select.pack(fill='both', expand=True)

        def populate_treeview(selected_component):
            self.list_select.delete(*self.list_select.get_children())  # Clear existing items
            number = 1
            if selected_component == 'GPU':
                component_data = gpu_data
            elif selected_component == 'CPU':
                component_data = CPU_data
            elif selected_component == 'Motherboard':
                component_data = mb_data
            elif selected_component == 'RAM':
                component_data = ram_data
            elif selected_component == 'SSD':
                component_data = ssd_data
            elif selected_component == 'HDD':
                component_data = hdd_data
            try:
                for index, item in component_data.iterrows():
                    self.list_select.insert('', 'end', text=f'{number}',
                                            values=(item['Name'], f"{item['Price']} Baht"))
                    number += 1
            except Exception:
                messagebox.showerror("Error",
                                     "Please select part to compare first.")
                return

        def on_select(*args):
            selected_component = self.components_type_combobox.get()
            populate_treeview(selected_component)

        on_select()

        def search_items(event=None):
            search_query = self.search_var.get().lower()
            if not search_query:
                return
            all_items = [(self.list_select.item(child, 'values'), child) for child in
                         self.list_select.get_children()]
            filtered_items = [(item_values, child) for item_values, child in all_items if
                              item_values and search_query in item_values[0].lower()]
            self.list_select.delete(*self.list_select.get_children())
            filtered_items.sort(
                key=lambda x: x[0][0].lower())
            number = 1
            for item_values, child in filtered_items:
                self.list_select.insert('', 'end', text=f'{number}', values=item_values)
                number += 1

        # Bind the search box to trigger search on key release
        self.search_entry.bind('<KeyRelease>', search_items)

        # Bind the search box to filter items when the user types in it
        self.search_var.trace_add('write', lambda *args: search_items())

        def add_to_select_handler(event):
            selected_item = self.list_select.item(self.list_select.selection())['values']
            if selected_item:
                name = selected_item[0]
                self.product_listbox.insert(tk.END, name)

        self.list_select.bind('<<TreeviewSelect>>', add_to_select_handler)
        self.done_button = tk.Button(self.select_window, text='Done',
                                     command=self.select_window.destroy)
        self.done_button.pack(side='bottom', pady=10, expand=True)

    def clear_handler(self):
        self.product_listbox.delete(0, tk.END)

    def load_filter(self, *args):
        selected_component = self.components_type_combobox.get()
        if selected_component == 'GPU':
            self.compare_combo['values'] = Component.GPU.value
        elif selected_component == 'CPU':
            self.compare_combo['values'] = Component.CPU.value
        elif selected_component == 'Motherboard':
            self.compare_combo['values'] = Component.Motherboard.value
        elif selected_component == 'RAM':
            self.compare_combo['values'] = Component.RAM.value
        elif selected_component == 'SSD':
            self.compare_combo['values'] = Component.SSD.value
        elif selected_component == 'HDD':
            self.compare_combo['values'] = Component.HDD.value

    def data_search(self, data_type):
        if data_type == 'GPU':
            return gpu_data
        elif data_type == 'CPU':
            return CPU_data
        elif data_type == 'Motherboard':
            return mb_data
        elif data_type == 'RAM':
            return ram_data
        elif data_type == 'SSD':
            return ssd_data
        elif data_type == 'HDD':
            return hdd_data

    def run(self):
        self.window.mainloop()


