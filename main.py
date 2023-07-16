from settings import *  # import settings module
import threading
import customtkinter as ctk
from widgets import *
import matplotlib  # import matplotlib module
import math
from CTkMessagebox import CTkMessagebox

matplotlib.use("TkAgg")  # set the backend for matplotlib
# library for symbolic maths
import sympy as sp
from PIL import Image  # import image class from PIL module

# this the function to be used to change the
# ctk.set_appearance_mode("light")


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=PRIMARY)
        # APP LAYOUT
        # * -----------GET THE WIDTH AND HEIGHT OF DISPLAY, center app in the middle of the screen----------
        self.app_width = 450
        self.app_height = 800
        display_width = self.winfo_screenwidth()
        display_height = (
            self.winfo_screenheight()
        )  # to make sure that application is in the centre

        left = int((display_width - self.app_width) / 2)
        top = int((display_height - self.app_height) / 2)
        self.geometry(f"{self.app_width}x{self.app_height}+{left}+{top}")
        self.resizable(True, True)  # Disable resize

        self.minsize(width=400, height=550)

        # GRID
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=2, uniform="a")
        self.rowconfigure(1, weight=5, uniform="a")

        self.title("Calculator")

        # !-----------------VARIABLE-------------
        self.binary = ctk.StringVar(value="")  # Variable to store the binary value
        self.hexadecimal = ctk.StringVar(
            value=""
        )  # Variable to store the hexadecimal value
        self.octal = ctk.StringVar(value="")
        self.decimal = ctk.StringVar(value="")
        self.formula = ctk.StringVar(value="")
        self.result = ctk.StringVar(
            value="0"
        )  # Variable to store the result of a calculation or operation and set initially to zero
        self.kilograms = ctk.StringVar(value="")
        self.pounds = ctk.StringVar(value="")
        self.celcius = ctk.StringVar(value="")
        self.fahrenheit = ctk.StringVar(value="")
        self.metres = ctk.StringVar(value="")
        self.inches = ctk.StringVar(value="")
        self.ans = None  # Variable to store the answer of a calculation or operation
        self.differentiate = ctk.StringVar(
            value="off"
        )  # Variable to control differentiation mode, initially set to "off"
        self.display_num = []  # List to store displayed numbers
        self.operation = []  # List to store operations
        self.trigo_num = []  # List to store numbers for trigonometric operations
        self.log_num = []  # List to store numbers for logarithmic operations
        self.num = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "("]
        self.trigo_bool = False  # Boolean flag to indicate if trigonometric mode is active, initially set to False
        self.log_bool = False  # Boolean flag to indicate if logarithmic mode is active, initially set to False
        self.shift = False  # Boolean flag to indicate if shift mode is active, initially set to False
        self.shift_button = None  # Variable to store the shift button state
        # Add a flag to check if the calculation is in progress
        self.calculation_in_progress = False

        # Add a lock to ensure thread safety for GUI updates
        self.gui_lock = threading.Lock()

        # !-------------WIDGETS------------------------------
        self.entry = Entry(self, self.result, self.formula)

        self.frame_normal = NumberFrame(self, self.num_press)
        self.frame_scientific = ScientificFrame(self, self.num_press)
        self.frame_programmer = Programmer(
            self, self.binary, self.decimal, self.hexadecimal, self.octal
        )
        # creating unit_converter widget with the given variables
        self.frame_converter = Unit_Converter(
            self,
            self.kilograms,
            self.pounds,
            self.celcius,
            self.fahrenheit,
            self.metres,
            self.inches,
        )

        # !---------------------TRACING--------------
        self.binary.trace("w", self.binary_trace)
        self.decimal.trace("w", self.decimal_trace)
        self.hexadecimal.trace("w", self.hexadecimal_trace)
        self.octal.trace("w", self.octal_trace)

        # To add theme image
        self.image = ctk.CTkImage(
            light_image=Image.open("image/theme.png"),
            dark_image=Image.open("image/dark.png"),
            size=(30, 30),
        )

        self.theme_button = ctk.CTkButton(
            self,
            text="",
            fg_color=PRIMARY,
            hover_color=PRIMARY,
            text_color=WHITE,
            image=self.image,
            height=30,
            corner_radius=50,
            width=30,
            command=self.toggle_theme,
        )
        self.protocol("WM_DELETE_WINDOW", self.quit)  # Close button

        # different Calculator options(Standard,Scientific or Programmer)
        self.theme_button.place(relx=1, rely=0.0, anchor="ne")
        self.option = ctk.CTkOptionMenu(
            self,
            values=["Normal", "Scientific", "Programmer", "Converter"],
            fg_color=GREY,
            dropdown_fg_color=GREY,
            width=100,
            button_color=GREY,
            button_hover_color=GREY,
            text_color=WHITE,
            corner_radius=5,
            dropdown_text_color=WHITE,
            dropdown_hover_color=ACCENTGREY,
            command=self.scientific,
        )

        self.option.place(relx=0.0, rely=0.0, anchor="nw")

        # checkbox to toggle whether you want to differentiate or not
        self.diff_widget = ctk.CTkCheckBox(
            self,
            text="Differentiate",
            variable=self.differentiate,
            fg_color=GREY,
            bg_color="transparent",
            text_color=WHITE,
            checkbox_height=20,
            checkbox_width=20,
            corner_radius=0,
            onvalue="on",
            offvalue="off",
            checkmark_color=WHITE,
            border_color=GREY,
            hover_color=ACCENTGREY,
            command=lambda: print(self.differentiate.get()),
        )

        # * -----------KEY BINDING TO EXIT THE APP -------------------------
        # Bind the escape key to quit the application and the return key to calculate the result
        self.bind("<Escape>", lambda _: self.quit())
        self.bind("<Return>", lambda _: self.calculate_result())
        # * -----------START APP ----------------------
        # Start the application with the normal calculator option
        self.scientific("Normal")
        # Start the application
        self.mainloop()

    # Function to plot the graph of the equation
    def plot_graph(self, equation):
        Graph(self, equation)

    # !-----------------TRACING-------------------

    # Function to trace the entry of the binary number and convert it to decimal, hexadecimal and octal
    def binary_trace(self, *args):
        binary = self.binary.get()
        try:
            bin = int(binary, 2)  # Convert binary to decimal
            self.decimal.set(
                str(bin)
            )  # Set the decimal variable with the decimal value
            self.hexadecimal.set(
                str(hex(bin)[2:]).upper()
            )  # Set the hexadecimal variable with the hexadecimal value
            self.octal.set(
                str(oct(bin)[2:])
            )  # Set the octal variable with the octal value
        except:
            pass

    # Function to trace the entry of the decimal number and convert it to binary, hexadecimal and octal
    def decimal_trace(self, *args):
        decimal = self.decimal.get()
        try:
            # Convert decimal to binary and set the binary variable
            self.binary.set(bin(int(decimal))[2:])
            # Convert decimal to octal and set the octal variable
            self.octal.set(oct(int(decimal))[2:])
            # Convert decimal to hexadecimal and set the hexadecimal variable
            self.hexadecimal.set(hex(int(decimal))[2:].upper())
        except:
            pass

    # Function to trace the entry of the hexadecimal number and convert it to binary, decimal and octal
    def hexadecimal_trace(self, *args):
        hexa = self.hexadecimal.get()
        try:
            # Convert hexadecimal to binary and set the binary variable
            self.binary.set(bin(int(hexa, 16))[2:])
            # Convert hexadecimal to decimal and set the decimal variable
            self.decimal.set(int(hexa, 16))
            # Convert hexadecimal to octal and set the octal variable
            self.octal.set(oct(int(hexa, 16))[2:])
        except:
            pass

    # Function to trace the entry of the octal number and convert it to binary, decimal and hexadecimal
    def octal_trace(self, *args):
        oct = self.octal.get()
        try:
            # Convert octal to binary and set the binary variable
            self.binary.set(bin(int(oct, 8))[2:])
            # Convert octal to decimal and set the decimal variable
            self.decimal.set(int(oct, 8))
            # Convert octal to hexadecimal and set the hexadecimal variable
            self.hexadecimal.set(hex(int(oct, 8))[2:].upper())
        except:
            pass

    # !-----------------CONVERSION-------------------
    # Function to trace the entry of the kilograms number and convert it to pounds
    def kilograms_convert(self, *args):
        kilograms = self.kilograms.get()
        try:
            kg_value = float(kilograms)
            # perform the calculation
            pounds = kg_value * 2.20462
            # set the pounds variable with the converted value as a string(StringVar contains only string values)
            self.pounds.set(str(pounds))
        except:
            # display an error message if the input is invalid
            CTkMessagebox(
                title="Invalid Input",
                message="Please enter a valid number",
                icon="cancel",
                button_color=BLUE,
                button_hover_color=ACCENTGREY,
            )

    # Function to trace the entry of the pounds number and convert it to kilograms
    def pounds_convert(self, *args):
        pounds = self.pounds.get()
        try:
            lb_value = float(pounds)
            kilograms = (
                lb_value * 0.453592
            )  # Convert pounds to kilograms using the conversion factor
            self.kilograms.set(
                str(kilograms)
            )  # Set the kilograms variable with the converted value as a string
        except:
            # display an error message if the input is invalid
            CTkMessagebox(
                title="Invalid Input",
                message="Please enter a valid number",
                icon="cancel",
                button_color=BLUE,
                button_hover_color=ACCENTGREY,
            )

    # Function to trace the entry of the Celsius temperature and convert it to Fahrenheit
    def celcius_convert(self, *args):
        celcius = self.celcius.get()
        try:
            celsius_value = float(celcius)
            fahrenheit = (
                celsius_value * 1.8 + 32
            )  # Convert celcius to fahrenheit using the conversion formula
            self.fahrenheit.set(
                str(fahrenheit)
            )  # Set the fahrenheit variable with the converted value as a string
        except:
            # display an error message if the input is invalid
            CTkMessagebox(
                title="Invalid Input",
                message="Please enter a valid number",
                icon="cancel",
                button_color=BLUE,
                button_hover_color=ACCENTGREY,
            )

    # Function to trace the entry of the Fahrenheit temperature and convert it to Celsius
    def fahrenheit_convert(self, *args):
        fahrenheit = self.fahrenheit.get()
        try:
            fahrenheit_value = float(fahrenheit)
            celsius = (
                fahrenheit_value - 32
            ) / 1.8  # Convert fahrenheit to celcius using the conversion formula
            self.celcius.set(
                str(celsius)
            )  # Set the fahrenheit variable with the converted value as a string
        except:
            # display an error message if the input is invalid
            CTkMessagebox(
                title="Invalid Input",
                message="Please enter a valid number",
                icon="cancel",
                button_color=BLUE,
                button_hover_color=ACCENTGREY,
            )

    # Function to trace the entry of the meters value and convert it to inches
    def metres_convert(self, *args):
        metres = self.metres.get()
        try:
            metres_value = float(metres)
            inches = metres_value * 39.3701
            self.inches.set(str(inches))
        except:
            # display an error message if the input is invalid
            CTkMessagebox(
                title="Invalid Input",
                message="Please enter a valid number",
                icon="cancel",
                button_color=BLUE,
                button_hover_color=ACCENTGREY,
            )

    # Function to trace the entry of the inches value and convert it to meters
    def inches_convert(self, *args):
        inches = self.inches.get()
        try:
            inches_value = float(inches)
            metres = inches_value * 0.0254
            self.metres.set(str(metres))
        except:
            # display an error message if the input is invalid
            CTkMessagebox(
                title="Invalid Input",
                message="Please enter a valid number",
                icon="cancel",
                button_color=BLUE,
                button_hover_color=ACCENTGREY,
            )

    # !-----------------THEME-----------------------
    # Function to toggle the theme of the calculator
    def toggle_theme(self):
        theme = ctk.get_appearance_mode()
        if theme == "Light":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    # !-----------------CALCULATION-------------------
    # Function to calculate the result of the expression
    def calculate_result(self, *args):
        # to indicate that a calculation is in progress
        self.calculation_in_progress = True
        # Retrieve the displayed number and operation
        result = "".join(self.display_num)
        operation = "".join(self.operation)
        # update the formula display with result
        self.formula.set(result)

        if self.differentiate.get() == "off":
            try:
                # Evaluate the operation and obtain the result
                result = eval(operation)
                with self.gui_lock:
                    # Update the result display with the calculated result
                    self.result.set(str(result))
                    # store the result for further calculations
                self.ans = self.result.get()
            except SyntaxError:
                with self.gui_lock:
                    # display syntax error for invalid expression
                    self.result.set("SYNTAX ERROR")
            except:
                with self.gui_lock:
                    self.result.set("MATH ERROR")
        else:
            try:
                # perform differentiation operation
                self.differentiation_operation(operation)
                # Start a separate thread to plot the graph
                graph = threading.Thread(target=self.plot_graph, args=(operation,))
                graph.start()
            except:
                self.result.set("SYNTAX ERROR")

        # clear operation and display number lists
        self.operation.clear()
        self.display_num.clear()
        # reset calculation in progress flag
        self.calculation_in_progress = False

    # Function to get the input from the user
    def num_press(self, value):
        if value == "=":
            # * -----------THREADING TO CALCULATE THE RESULT ----------------------
            # Start a separate thread to calculate the result
            if self.calculation_in_progress:
                return  # Return if a calculation is already in progress
            calculation_thread = threading.Thread(
                target=self.calculate_result, args=(self.formula, self.result)
            )
            # * -----------START THREAD ----------------------
            calculation_thread.start()
            return
        # * -----------CLEAR THE ENTRY ----------------------
        elif value == "Del":
            self.display_num.pop()
            self.operation.pop()
            # Update the result display with the remaining numbers
            self.result.set("".join(self.display_num))
            return
        # * -----------CLEAR THE ENTRY ----------------------
        elif value == "AC":
            self.display_num.clear()
            self.operation.clear()
            self.result.set("")
            self.formula.set("")
            return
        # * -----------ADD THE VALUE TO THE ENTRY ----------------------
        elif value == ")":
            if self.trigo_bool:
                self.operation.append(")")
                self.display(value, value)
            else:
                self.display(value, value)

        # * -----------OPERATION TOGGLE----------------------
        # Toggle the operation
        if self.option.get() == "Normal":
            # * -----------MATH OPERATION----------------------
            self.basic_operation(value)

        else:
            # * -----------MATH OPERATION----------------------
            self.basic_operation(value)
            self.trigonometry_operation(value)
            self.logarithmic_operation(value)

    # Function to append the value to the operation and display an set the result displayed on the screen
    def display(self, value, operation):
        self.display_num.append(value)
        self.operation.append(operation)
        self.result.set("".join(self.display_num))

    # Function to perform the basic operation
    def basic_operation(self, value):
        # * -----------MATH OPERATION----------------------
        math_operation = [
            "+",
            "-",
            "x",
            "/",
            ".",
            "x²",
            "√",
            "E/Ans",
            "x³/∛",
            "𝛑/x",
            "x!",
            "^",
            "E",
            "SHIFT",
        ]
        self.formula.set("")
        # * -----------CHECK IF THE VALUE IS IN THE MATH OPERATION----------------------
        if value in math_operation:
            if value == "x":
                value == " x "
                self.display(value, " * ")

            elif value == "√":
                value = f"{value}"
                self.operation.append("**0.5")
                self.result.set(f"√({''.join(self.display_num)})")

            elif value == "x²":
                value = f"{value}"
                # Start a separate thread to handle the display operation
                thread = threading.Thread(target=self.display, args=("²", "**2"))
                thread.start()
            elif value == "E/Ans":
                if self.shift == False:
                    value = f"{value}"
                    # Start a separate thread to handle the display operation
                    thread = threading.Thread(target=self.display, args=("E", "*10**"))
                    thread.start()
                else:
                    # Start a separate thread to handle the display operation
                    thread = threading.Thread(
                        target=self.display, args=(self.ans, self.ans)
                    )
                    thread.start()
            elif value == "E":
                value = f"{value}"
                thread = threading.Thread(
                    target=self.display,
                    args=(
                        value,
                        "*10**",
                    ),
                )
                thread.start()

            elif value == "x³/∛":
                if self.shift == False:
                    value = f"{value}"
                    # Start a separate thread to handle the display operation
                    thread = threading.Thread(target=self.display, args=("³", "**3"))
                    thread.start()
                else:
                    self.operation.append("**(1/3)")
                    # Set the result display to show the cube root operation
                    self.result.set(f"∛({''.join(self.display_num)})")
            elif value == ".":
                # Start a separate thread to handle the display operation
                thread = threading.Thread(target=self.display, args=(".", "."))
                thread.start()
            elif value == "^":
                value = f"{value}"
                # Start a separate thread to handle the display operation
                thread = threading.Thread(target=self.display, args=("^", "**"))
                thread.start()
            elif value == "𝛑/x":
                if self.shift == False:
                    value = f"{value}"
                    thread = threading.Thread(
                        target=self.display, args=("𝛑", "math.pi")
                    )
                    thread.start()
                elif self.shift == True:
                    if self.differentiate.get() == "on":
                        thread = threading.Thread(target=self.display, args=("x", "*x"))
                        thread.start()
                    elif self.differentiate.get() == "off":
                        thread = threading.Thread(target=self.display, args=("x", "x"))
                        thread.start()

            elif value == "x!":
                # Start a separate thread to handle the factorial operation
                thread = threading.Thread(target=self.factorial_operation)
                thread.start()
            elif value == "SHIFT":
                if self.shift == True:
                    self.shift_button.configure(fg_color=GREY)
                    self.shift = False
                else:
                    self.shift_button.configure(fg_color=BLUE)
                    self.shift = True
            else:
                value = f" {value} "
                # If the value is a number or other supported characters
                thread = threading.Thread(target=self.display, args=(value, value))
                thread.start()

        elif value in self.num:
            # Start a separate thread to handle the display operation
            thread = threading.Thread(target=self.display, args=(value, value))
            thread.start()

    # Function to perform the factorial operation
    def factorial_operation(self):
        # get the current operation value
        value = self.operation
        self.last_value = "".join(value)
        print(self.last_value)
        # clear the operation list to consider only the last value for factorial
        for i in range(len(value)):
            self.operation.pop()
        thread = threading.Thread(
            target=self.display, args=("!", "math.factorial(int(self.last_value))")
        )
        thread.start()

    # Function to perform the logarithmic operation
    def logarithmic_operation(self, value):
        log_operation = ["log", "ln"]
        # Check if the value is in the log_operation list
        if value in log_operation:
            self.trigo_bool = False
            self.log_bool = True
            if value == "log":
                # Start a separate thread to handle the display operation for log base 10
                thread = threading.Thread(
                    target=self.display, args=("log(", "math.log10(")
                )
                thread.start()
            elif value == "ln":
                # Start a separate thread to handle the display operation for log base e
                thread = threading.Thread(
                    target=self.display, args=("ln(", "math.log(")
                )
                thread.start()
        else:
            pass

    # Function to perform the differentiation operation
    def differentiation_operation(self, formula):
        # Create a symbol 'x' for differentiation
        x = sp.Symbol("x")
        # Create a SuperscriptPrinter instance for pretty printing
        printer = SuperscriptPrinter()
        try:
            # Convert the formula string to a symbolic expression
            formula = sp.sympify(formula)
            # Differentiate the formula with respect to 'x'
            derivative = sp.diff(formula, x)
            # Clear the display and operation lists
            self.display_num.clear()
            self.operation.clear()
            # Convert the derivative to a formatted string using the SuperscriptPrinter
            derivative_str = printer.doprint(derivative)
            # Start a separate thread to handle the display operation of the derivative
            threading.Thread(
                target=self.display, args=(derivative_str, derivative_str)
            ).start()

        except sp.SympifyError:
            self.result.set("SYNTAX ERROR")

    # Function to perform the trigonometric operation
    def trigonometry_operation(self, value):
        trigo_operation = [
            "sin/sin⁻¹",
            "cos/cos⁻¹",
            "tan/tan⁻¹",
            "sinh",
            "cosh",
            "tanh",
        ]
        # * -----------CHECK IF THE VALUE IS IN THE TRIGONOMETRIC OPERATION----------------------
        if value in trigo_operation:
            self.trigo_bool = True
            if self.shift == False:
                # Normal sin,cos,tan trigonometric operations
                if value == "sin/sin⁻¹":
                    # Start a separate thread to handle the display operation for sine
                    # The first argument is the value to be displayed on the screen
                    # The second argument is the value to be appended to the operation list
                    threading.Thread(
                        target=self.display, args=("sin(", "math.sin(math.radians(")
                    ).start()
                elif value == "cos/cos⁻¹":
                    # Start a separate thread to handle the display operation for cosine
                    # The first argument is the value to be displayed on the screen
                    # The second argument is the value to be appended to the operation list
                    threading.Thread(
                        target=self.display, args=("cos(", "math.cos(math.radians(")
                    ).start()
                elif value == "tan/tan⁻¹":
                    # Start a separate thread to handle the display operation for tangent
                    # The first argument is the value to be displayed on the screen
                    # The second argument is the value to be appended to the operation list
                    threading.Thread(
                        target=self.display, args=("tan(", "math.tan(math.radians(")
                    ).start()
                elif value == "sinh":
                    # Start a separate thread to handle the display operation for hyperbolic sine
                    # The first argument is the value to be displayed on the screen
                    # The second argument is the value to be appended to the operation list
                    self.trigo_bool = False
                    threading.Thread(
                        target=self.display, args=("sinh(", "math.sinh(")
                    ).start()
                elif value == "cosh":
                    # Start a separate thread to handle the display operation for hyperbolic cosine
                    # The first argument is the value to be displayed on the screen
                    # The second argument is the value to be appended to the operation list
                    self.trigo_bool = False
                    threading.Thread(
                        target=self.display, args=("cosh(", "math.cosh(")
                    ).start()
                elif value == "tanh":
                    # Start a separate thread to handle the display operation for hyperbolic tangent
                    # The first argument is the value to be displayed on the screen
                    # The second argument is the value to be appended to the operation list
                    self.trigo_bool = False
                    threading.Thread(
                        target=self.display, args=("tanh(", "math.tanh(")
                    ).start()
                else:
                    pass
            else:
                # Inverse trigonometric operations
                if value == "sin/sin⁻¹":
                    # Start a separate thread to handle the display operation for arcsine
                    threading.Thread(
                        target=self.display, args=("sin⁻¹(", "math.degrees(math.asin(")
                    ).start()
                elif value == "cos/cos⁻¹":
                    # Start a separate thread to handle the display operation for arccosine
                    threading.Thread(
                        target=self.display, args=("cos⁻¹(", "math.degrees(math.acos(")
                    ).start()
                elif value == "tan/tan⁻¹":
                    # Start a separate thread to handle the display operation for arctangent
                    threading.Thread(
                        target=self.display, args=("tan⁻¹(", "math.degrees(math.atan(")
                    ).start()

    # Function to change the calculator option
    def scientific(self, choice):
        if choice == "Scientific":
            # Show the scientific calculator frame and hide other frames
            self.frame_converter.place_forget()
            self.diff_widget.place(relx=0.5, rely=0.0, anchor="ne")
            self.frame_normal.grid_forget()
            self.frame_programmer.place_forget()
            self.entry.grid(column=0, row=0, sticky="nsew")
            self.frame_scientific.grid(column=0, row=1, sticky="nsew")

        elif choice == "Normal":
            # Show the normal calculator frame and hide other frames
            self.frame_converter.place_forget()
            self.diff_widget.place_forget()
            self.frame_programmer.place_forget()
            self.frame_scientific.grid_forget()
            self.entry.grid(column=0, row=0, sticky="nsew")
            self.frame_normal.grid(column=0, row=1, sticky="nsew")

        elif choice == "Programmer":
            # Show the programmer calculator frame and hide other frames
            self.frame_converter.place_forget()
            self.diff_widget.place_forget()
            self.entry.grid_forget()
            self.frame_scientific.grid_forget()
            self.frame_normal.grid_forget()
            self.frame_programmer.place(
                relx=0.0, rely=0.0, anchor="nw", relwidth=1, relheight=1
            )
        elif choice == "Converter":
            # Show the converter frame and hide other frames
            self.diff_widget.place_forget()
            self.entry.grid_forget()
            self.frame_scientific.grid_forget()
            self.frame_normal.grid_forget()
            self.frame_programmer.grid_forget()
            self.frame_converter.place(
                relx=0.0, rely=0.0, anchor="nw", relwidth=1, relheight=1
            )

    def quit(self):
        # Quit the calculator application
        self.destroy()


if __name__ == "__main__":
    App()
