import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from product_value import *
import webbrowser
from processing import *


class PCPartModel:
    def __init__(self):
        self.selected_components = {}


class PCPartView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title('PC Part Picker')
        self.init_components()

    def init_components(self):
        # Menu Bar
        menubar = tk.Menu(self)
        menubar.add_cascade(label="Exit", command=self.controller.exit_program)
        self.config(menu=menubar)

        # Notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        # First Page
        self.first_page = ttk.Frame(self.notebook)
        self.notebook.add(self.first_page, text='Build PC')
        self.init_first_page()
        self.init_second_page()
        self.init_third_page()

    def init_first_page(self):
        self.components_frame = ttk.Frame(self.first_page)
        self.components_frame.pack(side='left', fill='y', padx=20)

        # Total price label
        self.total_price_label = tk.Label(self.first_page, text='', font=('Arial', 11))
        self.total_price_label.pack(side='bottom', pady=10, anchor='w')

        # Price range frame
        self.price_range_frame = ttk.Frame(self.first_page)
        self.price_range_frame.pack(side='top', fill='x', pady=(20, 0))

        self.price_range1_label = ttk.Label(self.price_range_frame, text='Price range :')
        self.price_range1_label.pack(side='left', padx=(0, 10))

        self.price_range1_entry1 = ttk.Entry(self.price_range_frame, width=10)
        self.price_range1_entry1.pack(side='left', padx=(0, 5))
        self.price_range1_entry1.bind('<KeyRelease>', self.controller.filter_items)

        self.dash_label = ttk.Label(self.price_range_frame, text='-')
        self.dash_label.pack(side='left', padx=(0, 5))

        self.price_range1_entry2 = ttk.Entry(self.price_range_frame, width=10)
        self.price_range1_entry2.pack(side='left')
        self.price_range1_entry2.bind('<KeyRelease>', self.controller.filter_items)

        # Search
        self.search_frame = ttk.Frame(self.first_page)
        self.search_frame.pack(side='top', fill='x', pady=(5, 0))

        self.search_label = ttk.Label(self.search_frame, text='Search :')
        self.search_label.pack(side='left', padx=(0, 10))

        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self.search_frame, textvariable=self.search_var, width=50)
        self.search_entry.pack(side='left', fill='x', expand=True, padx=15, pady=5)
        self.search_entry.bind('<KeyRelease>', self.controller.search_items)

        # Treeview
        self.product_tree = ttk.Treeview(self.first_page, columns=('Name', 'Price'), height=13)
        self.product_tree.heading('#0', text='Number')
        self.product_tree.heading('Name', text='Name')
        self.product_tree.heading('Price', text='Price')
        self.product_tree.pack(side='left', fill='both', expand=True, padx=15)
        self.product_tree.bind('<<TreeviewSelect>>', self.controller.on_item_select)

        self.cpu_button = ttk.Button(self.components_frame, command=self.controller.cpu_handler,
                                     text='CPU',
                                     width=20)
        self.cpu_button.pack(fill='both', pady=10)
        self.mb_button = ttk.Button(self.components_frame, command=self.controller.mb_handler,
                                    text='Motherboard', width=20)
        self.mb_button.pack(fill='both', pady=5)
        self.gpu_button = ttk.Button(self.components_frame, command=self.controller.gpu_handler,
                                     text='GPU',
                                     width=20)
        self.gpu_button.pack(fill='both', pady=5)
        self.ram_button = ttk.Button(self.components_frame, command=self.controller.ram_handler,
                                     text='RAM',
                                     width=20)
        self.ram_button.pack(fill='both', pady=5)
        self.ssd_button = ttk.Button(self.components_frame, command=self.controller.ssd_handler,
                                     text='SSD',
                                     width=20)
        self.ssd_button.pack(fill='both', pady=5)
        self.hdd_button = ttk.Button(self.components_frame, command=self.controller.hdd_handler,
                                     text='HDD',
                                     width=20)
        self.hdd_button.pack(fill='both', pady=5)

        # Total price label
        self.total_price_label = tk.Label(self.components_frame,
                                          text=f'Total Price : {self.controller.total_price_value}',
                                          font=('Arial', 11))
        self.total_price_label.pack(side='top', pady=10)

        self.build_button = ttk.Button(self.components_frame, command=self.controller.build_handler,
                                       text='Build',
                                       width=10)
        self.build_button.pack(side='top', pady=10)

    def init_second_page(self):
        # Second Page
        self.second_page = ttk.Frame(self.notebook)
        self.notebook.add(self.second_page, text='Comparison')
        self.graph_frame = ttk.Frame(self.second_page)
        self.graph_frame.pack(side='left', fill='both', expand=True)

        # Graph sort frame
        self.graph_sort_frame = ttk.Frame(self.second_page)
        self.graph_sort_frame.pack(side='right', fill='y', padx=20)

        # Price range label, entries, and dash
        self.price_range_frame = ttk.Frame(self.graph_sort_frame)
        self.price_range_frame.pack(side='top', fill='x', pady=(20, 0))

        self.price_range_label = ttk.Label(self.price_range_frame, text='Price range :')
        self.price_range_label.pack(side='left', padx=(0, 10))

        self.price_range_entry1 = ttk.Entry(self.price_range_frame, width=10)
        self.price_range_entry1.pack(side='left', padx=(0, 5))

        self.dash_label = ttk.Label(self.price_range_frame, text='-')
        self.dash_label.pack(side='left', padx=(0, 5))

        self.price_range_entry2 = ttk.Entry(self.price_range_frame, width=10)
        self.price_range_entry2.pack(side='left')

        # Components type label and combobox
        self.components_type_label = ttk.Label(self.graph_sort_frame,
                                               text='Select part to compare:')
        self.components_type_label.pack(side='top', padx=5, pady=(20, 5), anchor='w')

        self.components_type_combobox = ttk.Combobox(self.graph_sort_frame, width=10,
                                                     state='readonly',
                                                     values=['CPU', 'GPU', 'Motherboard', 'RAM',
                                                             'SSD', 'HDD'])
        self.components_type_combobox.pack(side='top', padx=5, pady=(0, 5), anchor='w')

        # Things to compare label and combobox
        self.compare_topic_label = ttk.Label(self.graph_sort_frame, text='What to compare :')
        self.compare_topic_label.pack(side='top', padx=5, pady=(0, 5), anchor='w')

        self.compare_combo = ttk.Combobox(self.graph_sort_frame, width=10, values=['None'],
                                          state='readonly')
        self.compare_combo.pack(side='top', padx=5, pady=(0, 5), anchor='w')

        # Type of graph label and combobox
        self.graph_type_label = ttk.Label(self.graph_sort_frame, text='Select graph type :')
        self.graph_type_label.pack(side='top', padx=5, pady=(0, 5), anchor='w')

        self.graph_type_combo = ttk.Combobox(self.graph_sort_frame, width=10,
                                             values=['Bar Chart'], state='readonly')
        self.graph_type_combo.pack(side='top', padx=5, pady=(0, 5), anchor='w')

        # Overall Comparison
        self.var = tk.IntVar()
        self.overall_comparison = tk.Checkbutton(self.graph_sort_frame, text='Overall Comparison',
                                                 variable=self.var,
                                                 command=self.controller.overall_checkbox_handler)
        self.overall_comparison.pack(side='top', padx=5, pady=(0, 5), anchor='w')

        # List of comparing product
        self.list_of_product_label = tk.Label(self.graph_sort_frame, text='List of product')
        self.list_of_product_label.pack(side='top', padx=5, pady=(0, 5), anchor='w')
        self.product_listbox = tk.Listbox(self.graph_sort_frame, width=30, height=13)
        self.product_listbox.pack(side='top', padx=5, pady=(0, 5), anchor='w')

        self.plot_button = ttk.Button(self.graph_sort_frame, width=6, text='Plot',
                                      command=self.controller.plot_handler)
        self.plot_button.pack(side='left', padx=5, pady=(0, 5))

        # Select button
        self.select_button = ttk.Button(self.graph_sort_frame, width=6, text='Select',
                                        command=self.controller.select_handler)
        self.select_button.pack(side='left', padx=5, pady=(0, 5))

        # Clear button
        self.clear_button = ttk.Button(self.graph_sort_frame, width=6, text='Clear',
                                       command=self.controller.clear_handler)
        self.clear_button.pack(side='left', padx=5, pady=(0, 5))

        # graph
        fig, ax = plt.subplots(figsize=(7, 4))
        fig.set_dpi(100)
        self.graph = FigureCanvasTkAgg(fig, master=self.graph_frame)
        self.graph.get_tk_widget().pack(fill='both', expand=True)
        self.components_type_combobox.bind('<<ComboboxSelected>>', self.controller.load_filter)
        self.compare_combo.bind('<<ComboboxSelected>>', self.controller.price_range_compare_handler)
        self.price_range_entry1.config(state='disabled')
        self.price_range_entry2.config(state='disabled')

    def init_third_page(self):
        # Third Page
        self.third_page = ttk.Frame(self.notebook)
        self.notebook.add(self.third_page, text='Descriptive Statistic and Correlation')
        # Descriptive Statistics Frame
        self.statistic_frame = ttk.Frame(self.third_page)
        self.statistic_frame.pack(side='top', fill='both', expand=True)

        # Display for statistics
        self.stats_display_frame = ttk.Frame(self.statistic_frame)
        self.stats_display_frame.pack(side='top', fill='both', expand=True)

        self.cpu_frame = ttk.Frame(self.stats_display_frame)
        self.cpu_frame.pack(side='left', padx=10, pady=10, anchor='n')
        # Display CPU-Core statistics
        cpu_SD_label = ttk.Label(self.cpu_frame,
                                 text='CPU')
        cpu_SD_label.pack(side='top', anchor='w', padx=15)
        cpu_mean_label = ttk.Label(self.cpu_frame,
                                   text=f'Mean Core: {np.mean(CPU_data["Cores"]):.4f}')
        cpu_mean_label.pack(side='top', anchor='w', padx=15)
        cpu_SD_label = ttk.Label(self.cpu_frame,
                                 text=f'Standard Deviation Core: {np.std(CPU_data["Cores"]):.4f}')
        cpu_SD_label.pack(side='top', anchor='w', padx=15)

        # Display CPU-TDP statistics
        CPU_data["TDP_Numeric"] = CPU_data["TDP"].apply(extract_numeric_value)
        cpu_mean_label = ttk.Label(self.cpu_frame,
                                   text=f'Mean TDP: {np.mean(CPU_data["TDP_Numeric"]):.4f}')
        cpu_mean_label.pack(side='top', anchor='w', padx=15)
        cpu_SD_label = ttk.Label(self.cpu_frame,
                                 text=f'Standard Deviation TDP: {np.std(CPU_data["TDP_Numeric"]):.4f}')
        cpu_SD_label.pack(side='top', anchor='w', padx=15)

        self.gpu_frame = ttk.Frame(self.stats_display_frame)
        self.gpu_frame.pack(side='left', padx=10, pady=10, anchor='n')
        # Display GPU-Clock Speed statistics
        GPU_label = ttk.Label(self.gpu_frame,
                              text='GPU')
        GPU_label.pack(side='top', anchor='w', padx=15)
        gpu_data["Boost Clock Numeric"] = gpu_data["Boost Clock"].apply(extract_numeric_value)
        gpu_data["TDP Numeric"] = gpu_data["TDP"].apply(extract_numeric_value)
        gpu_mean_label = ttk.Label(self.gpu_frame,
                                   text=f'Mean Boost Clock: {np.mean(gpu_data["Boost Clock Numeric"]):.4f}')
        gpu_mean_label.pack(side='top', anchor='n', padx=15)
        gpu_sd = ttk.Label(self.gpu_frame,
                           text=f'Standard Deviation Boost Clock: {np.std(gpu_data["Boost Clock Numeric"]):.4f}')
        gpu_sd.pack(side='top', anchor='w', padx=15)

        self.ssd_frame = ttk.Frame(self.stats_display_frame)
        self.ssd_frame.pack(side='left', padx=10, pady=10, anchor='n')
        # Display SSD-Size statistics
        ssd_label = ttk.Label(self.ssd_frame,
                              text='SSD')
        ssd_label.pack(side='top', anchor='w', padx=15)
        ssd_data["Size Numeric"] = ssd_data["Size"].apply(extract_numeric_value)
        ssd_mean_label = ttk.Label(self.ssd_frame,
                                   text=f'Mean size: {np.mean(ssd_data["Size Numeric"]):.4f}')
        ssd_mean_label.pack(side='top', anchor='w', padx=15)
        ssd_SD_label = ttk.Label(self.ssd_frame,
                                 text=f'Standard Deviation size: {np.std(ssd_data["Size Numeric"]):.4f}')
        ssd_SD_label.pack(side='top', anchor='w', padx=15)

        self.hdd_frame = ttk.Frame(self.stats_display_frame)
        self.hdd_frame.pack(side='left', padx=10, pady=10, anchor='n')
        # Display HDD-Size
        hdd_label = ttk.Label(self.hdd_frame,
                              text='HDD')
        hdd_label.pack(side='top', anchor='w', padx=15)
        hdd_data["Size Numeric"] = hdd_data["Size"].apply(extract_numeric_value)
        hdd_mean_label = ttk.Label(self.hdd_frame,
                                   text=f'Mean size: {np.mean(hdd_data["Size Numeric"]):.4f}')
        hdd_mean_label.pack(side='top', anchor='w', padx=15)
        hdd_SD_label = ttk.Label(self.hdd_frame,
                                 text=f'Standard Deviation size: {np.std(hdd_data["Size Numeric"]):.4f}')
        hdd_SD_label.pack(side='top', anchor='w', padx=15)
        self.data_type_label = tk.Label(self.cpu_frame, text='Choose data type :')
        self.data_type_combo = ttk.Combobox(self.cpu_frame,
                                            values=['CPU', 'RAM', 'SSD', 'HDD', 'GPU'],
                                            state='readonly')
        self.data_type_combo.bind('<<ComboboxSelected>>', self.controller.plot_correlation_graph)
        self.data_type_label.pack(side='top', anchor='w', pady=5)
        self.data_type_combo.pack(side='top', anchor='w', pady=5)
        fig, ax = plt.subplots(figsize=(7, 4))
        fig.set_dpi(100)
        self.correlation_canvas = FigureCanvasTkAgg(fig, master=self.statistic_frame)
        self.correlation_canvas.get_tk_widget().pack(side='top', fill='both', expand=True)


class PCPartController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.total_price_value = 0
        self.selected_components = {}
        self.component_data = {
            'CPU': CPU_data,
            'Motherboard': mb_data,
            'GPU': gpu_data,
            'RAM': ram_data,
            'SSD': ssd_data,
            'HDD': hdd_data
        }

    def exit_program(self):
        self.view.quit()

    def search_items(self, event=None):
        search_query = self.view.search_var.get().lower()
        if not search_query:
            return
        all_items = [(self.view.product_tree.item(child, 'values'), child) for child in
                     self.view.product_tree.get_children()]
        filtered_items = [(item_values, child) for item_values, child in all_items if
                          item_values and search_query in item_values[0].lower()]
        self.view.product_tree.delete(*self.view.product_tree.get_children())
        filtered_items.sort(
            key=lambda x: x[0][0].lower())
        number = 1
        for item_values, child in filtered_items:
            self.view.product_tree.insert('', 'end', text=f'{number}', values=item_values)
            number += 1

    def filter_items(self, event=None):
        min_price = self.view.price_range1_entry1.get()
        max_price = self.view.price_range1_entry2.get()
        try:
            min_price = int(min_price)
        except ValueError:
            min_price = 0

        try:
            max_price = int(max_price)
        except ValueError:
            max_price = float('inf')
        if max_price <= min_price:
            pass
        search_query = self.view.search_var.get().lower()
        filtered_items = []
        for child in self.view.product_tree.get_children():
            item = self.view.product_tree.item(child)
            values = item["values"]
            if values:
                price_str = values[1].split()[0]
                try:
                    price = int(price_str)
                    if min_price <= price <= max_price and (
                            not search_query or search_query in values[0].lower()):
                        filtered_items.append((item["text"], values))
                except ValueError:
                    pass

        self.view.product_tree.delete(*self.view.product_tree.get_children())
        number = 1
        for item_text, item_values in filtered_items:
            self.view.product_tree.insert('', 'end', text=f'{number}', values=item_values)
            number += 1

    def build_handler(self):
        build_window = tk.Toplevel()
        build_window.title("Build Details")

        build_text = tk.Text(build_window, wrap="word", height=20, width=50)
        build_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        current_row = 0
        for button in [self.view.cpu_button, self.view.mb_button, self.view.gpu_button,
                       self.view.ram_button,
                       self.view.ssd_button, self.view.hdd_button]:
            product_name = button['text']
            # Search for product page and price based on product name
            product_page = ""
            price = ""
            for category, data in self.component_data.items():
                if data['Name'].str.contains(product_name).any():
                    product_data = data[data['Name'].str.contains(product_name)]
                    product_page = product_data['Product Page'].iloc[0] if not product_data[
                        'Product Page'].empty else "N/A"
                    price = product_data['Price'].iloc[0] if not product_data[
                        'Price'].empty else "N/A"
                    break

            if product_page != "N/A":
                component_link_text = f"{product_name}: {price} Baht - Product Page:"
                build_text.insert("end", f"{component_link_text}\n")
                hyperlink = tk.Label(build_text, text=product_page, fg="blue", cursor="hand2")
                hyperlink.bind("<Button-1>", lambda e, link=product_page: webbrowser.open_new(link))
                hyperlink.grid(row=current_row, column=0, sticky="w")
                current_row += 1
            else:
                build_text.insert("end", f"{product_name}: {price} Baht - Product Page: N/A\n\n")
        build_text.config(state="disabled")

    def cpu_handler(self):
        self.view.product_tree.delete(*self.view.product_tree.get_children())
        number = 1
        for index, cpu in CPU_data.iterrows():
            self.view.product_tree.insert('', 'end', text=f'{number}',
                                          values=(cpu['Name'], f"{cpu['Price']} Baht"))
            number += 1
        self.selected_button = self.view.cpu_button

    def gpu_handler(self):
        self.view.product_tree.delete(*self.view.product_tree.get_children())
        number = 1
        for index, gpu in gpu_data.iterrows():
            self.view.product_tree.insert('', 'end', text=f'{number}',
                                          values=(gpu['Name'], f"{gpu['Price']} Baht"))
            number += 1
        self.selected_button = self.view.gpu_button

    def mb_handler(self):
        self.view.product_tree.delete(*self.view.product_tree.get_children())
        number = 1
        for index, mb in mb_data.iterrows():
            self.view.product_tree.insert('', 'end', text=f'{number}',
                                          values=(mb['Name'], f"{mb['Price']} Baht"))
            number += 1
        self.selected_button = self.view.mb_button

    def ssd_handler(self):
        self.view.product_tree.delete(*self.view.product_tree.get_children())
        number = 1
        for index, ssd in ssd_data.iterrows():
            self.view.product_tree.insert('', 'end', text=f'{number}',
                                          values=(ssd['Name'], f"{ssd['Price']} Baht"))
            number += 1
        self.selected_button = self.view.ssd_button

    def hdd_handler(self):
        self.view.product_tree.delete(*self.view.product_tree.get_children())
        number = 1
        for index, hdd in hdd_data.iterrows():
            self.view.product_tree.insert('', 'end', text=f'{number}',
                                          values=(hdd['Name'], f"{hdd['Price']} Baht"))
            number += 1
        self.selected_button = self.view.hdd_button

    def ram_handler(self):
        self.view.product_tree.delete(*self.view.product_tree.get_children())
        number = 1
        for index, ram in ram_data.iterrows():
            self.view.product_tree.insert('', 'end', text=f'{number}',
                                          values=(ram['Name'], f"{ram['Price']} Baht"))
            number += 1
        self.selected_button = self.view.ram_button

    def on_item_select(self, event):
        selected_item = self.view.product_tree.item(self.view.product_tree.selection())['values']
        if selected_item:
            name, price = selected_item
            try:
                price = int(price.split()[0])
            except ValueError:
                return

            category_selected = False
            components_copy = self.selected_components.copy()
            for category, item_price in components_copy.items():
                if category != name.split()[0]:  # Compare category names
                    continue
                category_selected = True
                self.total_price_value -= item_price
                self.selected_components.pop(category)
            self.selected_components[name.split()[0]] = price
            self.total_price_value += price
            self.view.total_price_label.config(
                text=f'Total Price: {self.total_price_value} Baht')
            self.update_button(self.selected_button, name)
            if category_selected:
                self.update_button(self.selected_button)

    def update_button(self, button, selected_item_name=None):
        if selected_item_name:
            self.selected_item_name = selected_item_name
            button.config(text=self.selected_item_name)
        else:
            button.config(text=button.cget('text').split(':')[0])

    def overall_checkbox_handler(self):
        overall_comparison_checked = self.view.var.get()
        if overall_comparison_checked == 1:
            self.view.graph_type_combo['values'] = ['Histogram']
            self.view.graph_type_combo['value'] = 'Histogram'
            self.view.graph_type_combo.config(state='readonly')
        else:
            self.view.graph_type_combo['values'] = ['Bar Chart']
            self.view.graph_type_combo['value'] = 'Bar Chart'
            self.view.price_range_entry1['value'] = ''
            self.view.price_range_entry2['value'] = ''
            self.view.price_range_entry1.config(state='disabled')
            self.view.price_range_entry2.config(state='disabled')

    def plot_handler(self):
        try:
            selected_graph_type = self.view.graph_type_combo.get()

            if self.view.graph is not None:
                self.view.graph.get_tk_widget().destroy()

            fig, ax = plt.subplots(figsize=(7, 4))
            fig.set_dpi(100)
            data = self.data_search(self.view.components_type_combobox.get())

            if selected_graph_type == 'Histogram':
                compare_attribute = self.view.compare_combo.get()
                price_range_min = self.view.price_range_entry1.get()
                price_range_max = self.view.price_range_entry2.get()
                if price_range_max < price_range_min and self.view.var.get() == 1 and self.view.compare_combo.get() == 'Price':
                    messagebox.showerror("Maximum must be higher than minimum price.")
                    return

                if price_range_min and price_range_max:
                    data_to_plot = data[(data[compare_attribute] >= int(price_range_min)) & (
                            data[compare_attribute] <= int(price_range_max))]
                    ax.hist(data_to_plot[compare_attribute], bins=5)
                    ax.set_xlabel('Value')
                    ax.set_ylabel('Frequency')
                    ax.set_title('Histogram')
                else:
                    # Plot histogram based on all items in the data
                    ax.hist(data[compare_attribute], bins=5)
                    ax.set_xlabel('Value')
                    ax.set_ylabel('Frequency')
                    ax.set_title('Histogram')

            elif selected_graph_type == 'Bar Chart':
                values = []
                labels = self.view.product_listbox.get(0, tk.END)
                for item in labels:
                    for index, row in data.iterrows():
                        if row['Name'] == item:
                            values.append(row[self.view.compare_combo.get()])

                ax.bar(labels, values)
                ax.set_xlabel('Category')
                ax.set_ylabel('Value')
                ax.set_title('Bar Chart')

            self.view.graph = FigureCanvasTkAgg(fig, master=self.view.graph_frame)
            self.view.graph.get_tk_widget().pack(fill='both', expand=True)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def search_items_select(self, event=None):
        search_query = self.view.search_entry_select.get().lower()
        if not search_query:
            return
        all_items = [(self.view.list_select.item(child, 'values'), child) for child in
                     self.list_select.get_children()]
        filtered_items = [(item_values, child) for item_values, child in all_items if
                          item_values and search_query in item_values[0].lower()]
        self.list_select.delete(*self.list_select.get_children())
        filtered_items.sort(key=lambda x: x[0][0].lower())
        number = 1
        for item_values, child in filtered_items:
            self.list_select.insert('', 'end', text=f'{number}', values=item_values)
            number += 1

    def select_handler(self):
        self.select_window = tk.Tk()
        self.select_type_label = tk.Label(self.select_window, text='Select Component')
        self.select_type_label.pack(side='top', expand=True)

        # Search box
        self.search_label_select = tk.Label(self.select_window, text='Search:')
        self.search_label_select.pack(side='top', pady=5, expand=True)

        self.search_var_select = tk.StringVar()
        self.search_entry_select = tk.Entry(self.select_window, textvariable=self.search_var_select)
        self.search_entry_select.pack(side='top', padx=5, pady=5, fill='x', expand=True)

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
            selected_component = self.view.components_type_combobox.get()
            populate_treeview(selected_component)

        on_select()
        self.search_entry_select.bind('<KeyRelease>', self.search_items_select)

        def add_to_select_handler(event):
            selected_item = self.list_select.item(self.list_select.selection())['values']
            if selected_item:
                name = selected_item[0]
                self.view.product_listbox.insert(tk.END, name)

        self.list_select.bind('<<TreeviewSelect>>', add_to_select_handler)
        self.done_button = tk.Button(self.select_window, text='Done',
                                     command=self.select_window.destroy)
        self.done_button.pack(side='bottom', pady=10, expand=True)

    def price_range_compare_handler(self, *args):
        overall_comparison_checked = self.view.var.get()
        if overall_comparison_checked == 1 and self.view.compare_combo.get() == 'Price':
            self.view.price_range_entry1.config(state='normal')
            self.view.price_range_entry2.config(state='normal')
        else:
            self.view.price_range_entry1.config(state='disable')
            self.view.price_range_entry2.config(state='disable')

    def clear_handler(self):
        self.view.product_listbox.delete(0, tk.END)

    def load_filter(self, *args):
        selected_component = self.view.components_type_combobox.get()
        if selected_component == 'GPU':
            self.view.compare_combo['values'] = Component.GPU.value
        elif selected_component == 'CPU':
            self.view.compare_combo['values'] = Component.CPU.value
        elif selected_component == 'Motherboard':
            self.view.compare_combo['values'] = Component.Motherboard.value
        elif selected_component == 'RAM':
            self.view.compare_combo['values'] = Component.RAM.value
        elif selected_component == 'SSD':
            self.view.compare_combo['values'] = Component.SSD.value
        elif selected_component == 'HDD':
            self.view.compare_combo['values'] = Component.HDD.value

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

    def plot_correlation_graph(self, *args):

        self.view.correlation_canvas.get_tk_widget().destroy()

        selected_data_type = self.view.data_type_combo.get()
        if selected_data_type not in DataType.__members__:
            return

        selected_data = DataType[selected_data_type].value
        if selected_data_type == 'CPU':
            data_source = CPU_data
        elif selected_data_type == 'RAM':
            data_source = ram_data
        elif selected_data_type == 'HDD':
            data_source = hdd_data
        elif selected_data_type == 'SSD':
            data_source = ssd_data
        elif selected_data_type == 'GPU':
            data_source = gpu_data
        else:
            return
        ram_data['Size Numeric'] = ram_data["Size"].apply(extract_numeric_value)
        ssd_data['Size Numeric'] = ssd_data["Size"].apply(extract_numeric_value)
        gpu_data['TDP Numeric'] = gpu_data['TDP'].apply(extract_numeric_value)

        self.correlation_fig = plt.Figure(figsize=(7, 4))
        ax = self.correlation_fig.add_subplot(111)
        ax.scatter(data_source[selected_data[0]], data_source[selected_data[1]], alpha=0.7)

        # Setting labels and title
        ax.set_xlabel(selected_data[0])
        ax.set_ylabel(selected_data[1])
        ax.set_title(f'Scatter Plot: {selected_data[0]} vs. {selected_data[1]}')

        self.view.correlation_canvas = FigureCanvasTkAgg(self.correlation_fig,
                                                         master=self.view.statistic_frame)
        self.view.correlation_canvas.draw()
        self.view.correlation_canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

    def run(self):
        self.view.mainloop()


def main():
    model = PCPartModel()
    controller = PCPartController(model, None)
    view = PCPartView(controller)
    controller.view = view
    view.mainloop()


if __name__ == "__main__":
    main()
