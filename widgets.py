from settings import *
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.figure import Figure
import matplotlib.animation as animation
import customtkinter as ctk
from sympy.printing.str import StrPrinter
import warnings
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import pyplot as plt
import numpy as np


# inherits from ctk.CTkToplevel, which represents a top-level window in the custom tkinter library.
class Graph(ctk.CTkToplevel):
    # The __init__ method is the constructor for the Graph class. It takes two arguments: parent (the parent widget) and operation (the mathematical operation to plot).
    def __init__(self, parent, operation):
        # The __init__ method first calls the constructor of the parent class using super().__init__(master=parent) to initialize the Graph object as a top-level window.
        super().__init__(master=parent)
        # Setup the title of the window and store the mathematical operation in the self.operation attribute
        self.title("Linear Plot")
        self.operation = operation

        self.setup_plot()

        # Create a navigation toolbar and pack it at the bottom of the window
        self.toolbar = NavigationToolbar2Tk(self.fig.canvas, self)
        self.toolbar.update()
        self.toolbar.pack(side=ctk.BOTTOM, fill=ctk.X)

        # Create a canvas to display the plot and pack it at the top of the window
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=1)

        # Start the animation by calling the update_plot method at regular intervals
        self.anim = animation.FuncAnimation(self.fig, self.update_plot, interval=100)

    def setup_plot(self):
        # Configure matplotlib to use automatic figure layout
        plt.rcParams["figure.autolayout"] = True

        # Create a new figure and add a single subplot to it
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)

        # Generate x-values using np.linspace to span from -10 to 10
        x = np.linspace(-10, 10)

        # Evaluate the mathematical operation provided in self.operation for the corresponding y-values
        y = eval(self.operation)

        # Plot the line graph with x and y values, and store the line object for later use
        (self.line,) = self.ax.plot(x, y)

        # Enable the grid on the plot
        self.ax.grid(True)

    def update_plot(self, frame):
        try:
            # Use warnings.catch_warnings and warnings.filterwarnings to ignore RuntimeWarnings
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=RuntimeWarning)

                # Generate x-values using np.linspace to span from -10 to 10
                x = np.linspace(-10, 10)

                # Evaluate the mathematical operation provided in self.operation for the corresponding y-values
                y = eval(self.operation)

            # Update the data of the line object with the new x and y values
            self.line.set_data(x, y)

            # Adjust the axis limits to fit the data
            self.ax.relim()
            self.ax.autoscale_view()

            # Return the line object to indicate that the plot has been updated
            return (self.line,)
        except:
            # If an exception occurs, simply pass and do nothing
            pass


# Create entry widget which inherit from ctkFrame to display the result and the formula
class Entry(ctk.CTkFrame):
    def __init__(self, parent, result, formula):
        super().__init__(master=parent, bg_color=PRIMARY, fg_color=PRIMARY)

        self.grid(column=0, row=0, sticky="nsew")  # take max space in 4 directions

        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1), weight=1)

        font2 = ctk.CTkFont(family=FONT, size=LARGE, weight="normal")
        font1 = ctk.CTkFont(family=FONT, size=SMALL, weight="normal")

        formula = ctk.CTkLabel(
            self, text="", font=font1, textvariable=formula, text_color=WHITE
        )
        result = ctk.CTkLabel(
            self, text="", font=font2, textvariable=result, text_color=WHITE
        )

        formula.grid(column=0, row=0, sticky="se", padx=10)
        result.grid(column=0, row=1, sticky="e", padx=10)


# Create a frame which inherit from ctkFrame to display the number
class NumberFrame(ctk.CTkFrame):
    def __init__(self, parent, func):
        super().__init__(master=parent, fg_color=PRIMARY)
        # take max space in 4 directions

        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="c")
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="c")

        for num, data in BUTTON.items():
            Button(
                self,
                text=num,
                column=data["col"],
                row=data["row"],
                columnspan=data["colspan"],
                rowspan=data["rowspan"],
                func=func,
                hv_color=data["hv_color"],
                color=data["color"],
            )


# Create a button which inherit from ctkButton to display the number
class Button(ctk.CTkButton):
    def __init__(
        self,
        parent,
        text,
        column,
        row,
        hv_color,
        color,
        columnspan=1,
        rowspan=1,
        func=lambda: print("Button pressed"),
    ):
        font3 = ctk.CTkFont(family=FONT, size=SMALL, weight="normal")
        super().__init__(
            master=parent,
            text=text,
            fg_color=color,
            hover_color=hv_color,
            text_color=WHITE,
            font=font3,
            command=lambda: func(text),
        )

        self.grid(
            column=column,
            row=row,
            columnspan=columnspan,
            rowspan=rowspan,
            sticky="nsew",
            padx=1,
            pady=1,
        )

    # TODO: Calculator Logic


# Create a frame which inherit from ctkFrame to display the scientific number
class ScientificFrame(ctk.CTkFrame):
    def __init__(self, parent, func):
        super().__init__(master=parent, fg_color=PRIMARY)
        self.columnconfigure((0, 1, 2, 3), weight=3, uniform="d")
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1, uniform="d")
        # !-----------------WIDGETS-------------------
        for num, data in SCIENTIFIC_BUTTON.items():
            if num == "SHIFT":
                parent.shift_button = Button(
                    self,
                    text=num,
                    column=data["col"],
                    row=data["row"],
                    columnspan=data["colspan"],
                    rowspan=data["rowspan"],
                    func=func,
                    hv_color=data["hv_color"],
                    color=data["color"],
                )
                continue
            Button(
                self,
                text=num,
                column=data["col"],
                row=data["row"],
                columnspan=data["colspan"],
                rowspan=data["rowspan"],
                func=func,
                hv_color=data["hv_color"],
                color=data["color"],
            )


class Unit_Converter(ctk.CTkFrame):
    # widgets for unit converter calculator
    def __init__(self, parent, kilograms, pounds, celcius, fahrenheit, metres, inches):
        super().__init__(master=parent, fg_color=PRIMARY)

        # !---------------WIDGET-------------------
        ctk.CTkLabel(
            self, text="Weight/Mass", text_color=WHITE, font=(FONT, TITLE)
        ).place(relx=0.5, rely=0.05, anchor="center")

        # !---------------KILOGRAMS-------------------
        ctk.CTkLabel(self, text="Kilograms", text_color=WHITE).place(
            relx=0.5, rely=0.1, anchor="center"
        )

        ctk.CTkEntry(self, textvariable=kilograms).place(
            relx=0.5, rely=0.15, relwidth=0.8, relheight=0.05, anchor="center"
        )

        # !---------------POUNDS-----------------
        ctk.CTkLabel(self, text="Pounds", text_color=WHITE).place(
            relx=0.5, rely=0.2, anchor="center"
        )

        ctk.CTkEntry(self, textvariable=pounds).place(
            relx=0.5, rely=0.25, anchor="center", relwidth=0.8, relheight=0.05
        )
        # !----------------BUTTON-----------------
        ctk.CTkButton(
            self,
            text="Convert to Kg",
            fg_color=BLUE,
            hover_color=ACCENTGREY,
            command=parent.pounds_convert,
        ).place(relx=0.275, rely=0.3, anchor="center", relwidth=0.35, relheight=0.04)

        ctk.CTkButton(
            self,
            text="Convert to Lb",
            fg_color=BLUE,
            hover_color=ACCENTGREY,
            command=parent.kilograms_convert,
        ).place(relx=0.725, rely=0.3, anchor="center", relwidth=0.35, relheight=0.04)

        # !---------------TEMPERATURE-------------------
        ctk.CTkLabel(
            self, text="Temperature", text_color=WHITE, font=(FONT, TITLE)
        ).place(relx=0.5, rely=0.35, anchor="center")

        # !---------------CELCIUS-------------------
        ctk.CTkLabel(self, text="Celcius", text_color=WHITE).place(
            relx=0.5, rely=0.4, anchor="center"
        )

        ctk.CTkEntry(self, textvariable=celcius).place(
            relx=0.5, rely=0.45, relwidth=0.8, relheight=0.05, anchor="center"
        )

        # !---------------FAHRENHEIT-----------------
        ctk.CTkLabel(self, text="Fahrenheit", text_color=WHITE).place(
            relx=0.5, rely=0.5, anchor="center"
        )

        ctk.CTkEntry(self, textvariable=fahrenheit).place(
            relx=0.5, rely=0.55, anchor="center", relwidth=0.8, relheight=0.05
        )
        # !----------------BUTTON-----------------
        ctk.CTkButton(
            self,
            text="Convert to °C",
            fg_color=BLUE,
            hover_color=ACCENTGREY,
            command=parent.fahrenheit_convert,
        ).place(relx=0.275, rely=0.6, anchor="center", relwidth=0.35, relheight=0.04)
        ctk.CTkButton(
            self,
            text="Convert to °F",
            fg_color=BLUE,
            hover_color=ACCENTGREY,
            command=parent.celcius_convert,
        ).place(relx=0.725, rely=0.6, anchor="center", relwidth=0.35, relheight=0.04)

        # !---------------LENGTH-------------------
        ctk.CTkLabel(self, text="Length", text_color=WHITE, font=(FONT, TITLE)).place(
            relx=0.5, rely=0.65, anchor="center"
        )
        ctk.CTkLabel(self, text="Metres", text_color=WHITE).place(
            relx=0.5, rely=0.7, anchor="center"
        )

        ctk.CTkEntry(self, textvariable=metres).place(
            relx=0.5, rely=0.75, relwidth=0.8, relheight=0.05, anchor="center"
        )

        # !---------------INCHES-----------------
        ctk.CTkLabel(self, text="Inches", text_color=WHITE).place(
            relx=0.5, rely=0.8, anchor="center"
        )

        ctk.CTkEntry(self, textvariable=inches).place(
            relx=0.5, rely=0.85, anchor="center", relwidth=0.8, relheight=0.05
        )

        # !----------------BUTTON-----------------
        # Button for conversions parts
        ctk.CTkButton(
            self,
            text="Convert to m",
            fg_color=BLUE,
            hover_color=ACCENTGREY,
            command=parent.inches_convert,
        ).place(relx=0.275, rely=0.9, anchor="center", relwidth=0.35, relheight=0.04)
        ctk.CTkButton(
            self,
            text="Convert to inch",
            fg_color=BLUE,
            hover_color=ACCENTGREY,
            command=parent.metres_convert,
        ).place(relx=0.725, rely=0.9, anchor="center", relwidth=0.35, relheight=0.04)


# Create a frame which inherit from ctkFrame to display the programmer number
class Programmer(ctk.CTkFrame):
    # widgets for programmer calculator
    def __init__(self, parent, binary, decimal, hexadecimal, octal):
        super().__init__(master=parent, fg_color=PRIMARY)
        self.configure(corner_radius=0)

        # !---------------WIDGET-------------------
        # !---------------BINARY-------------------
        ctk.CTkLabel(self, text="Binary", text_color=WHITE).place(
            relx=0.5, rely=0.1, anchor="center"
        )
        ctk.CTkEntry(self, textvariable=binary).place(
            relx=0.5, rely=0.15, relwidth=0.8, relheight=0.05, anchor="center"
        )

        # !---------------DECIMAL-----------------
        ctk.CTkLabel(self, text="Decimal", text_color=WHITE).place(
            relx=0.5, rely=0.3, anchor="center"
        )
        ctk.CTkEntry(self, textvariable=decimal).place(
            relx=0.5, rely=0.35, anchor="center", relwidth=0.8, relheight=0.05
        )

        # !---------------HEXADECIMAL-------------------
        ctk.CTkLabel(self, text="Hexadecimal", text_color=WHITE).place(
            relx=0.5, rely=0.5, anchor="center"
        )
        ctk.CTkEntry(self, textvariable=hexadecimal).place(
            relx=0.5, rely=0.55, relwidth=0.8, relheight=0.05, anchor="center"
        )

        # !------------------OCTAL-----------------------
        ctk.CTkLabel(self, text="Octal", text_color=WHITE).place(
            relx=0.5, rely=0.7, anchor="center"
        )

        ctk.CTkEntry(self, textvariable=octal).place(
            relx=0.5, rely=0.75, relwidth=0.8, relheight=0.05, anchor="center"
        )


class SuperscriptPrinter(StrPrinter):
    # function to make derivative result prettier
    def _print_Pow(self, expr, **kwargs):
        # Print the power expression in a formatted manner
        base = self._print(expr.base, **kwargs)  # Get the base of the power expression
        exponent = self._print(
            expr.exp, **kwargs
        )  # Get the exponent of the power expression
        return base + "⁽" + exponent + "⁾"  # Return the formatted power expression
