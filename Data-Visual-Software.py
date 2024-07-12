import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataVisualizationSoftware(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Data Visual Software")

        self.data = []
        self.chart_type = tk.StringVar()
        self.chart_type.set("Pie Chart")

        self.create_widgets()

        def create_widgets(self):
            input_frame = tk.Frame(self)
            input_frame.pack(pady=10)

            tk.Label(input_frame, text = "Data Type:").grid(row = 0,column = 0,padx = 5,pady = 5)
            self.data_type_entry = tk.Entry(input_frame)
            self.data_type_entry.grid(row = 0, column = 1, padx = 5, pady = 5)

            tk.Label(input_frame, text = "Value:").grid(row = 1,column = 0, padx = 5, pady = 5)
            self.data_type_entry = tk.Entry(input_frame)
            self.data_type_entry.grid(row = 1, column = 1, padx = 5, pady = 5)

            add_button = tk.Button(input_frame, text = "Add Data", command=self.add_data)
            add_button.grid(row = 2, column = 0, columnspan= 2, padx = 5, pady = 5)

            chart_frame = tk.Frame(self)
            chart_frame.pack(pady = 10)

            tk.Label(chart_frame, text = "Select Chart Type:").grid(row = 0, column = 0, padx = 5, pady = 5)
            chart_types = ["Pie Chart", "Column Chart", "Bar Chart", "Line Chart"]
            for i, chart_type in enumerate(chart_types):
                tk.Radiobutton(chart_frame, text = chart_type, variable = self.chart_type, value = chart_type).grid(row = i + 1, column = 0, padx = 5, pady = 2)

            generate_button = tk.Button(chart_frame, text = "Generate Chart", command = self.generate_chart)
            generate_button.grid(row = len(chart_type) + 1, column = 0, padx = 5, pady = 5)