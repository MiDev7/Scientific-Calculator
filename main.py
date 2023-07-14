from settings import *
import threading
import customtkinter as ctk
import warnings
from widgets import *


import matplotlib

matplotlib.use("TkAgg")

# library for symbolic maths
import sympy as sp
from PIL import Image
import matplotlib.pyplot as plt

import numpy as np

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
        self.history = []
        self.binary = ctk.StringVar(value="")
        self.hexadecimal = ctk.StringVar(value="")
        self.octal = ctk.StringVar(value="")
        self.decimal = ctk.StringVar(value="")
        self.formula = ctk.StringVar(value="")
        self.result = ctk.StringVar(value="0")
        self.kilograms = ctk.StringVar(value="0.0")
        self.pounds = ctk.StringVar(value="0.0")
        self.celcius = ctk.StringVar(value="0.0")
        self.fahrenheit = ctk.StringVar(value="0.0")
        self.metres = ctk.StringVar(value="0.0")
        self.inches = ctk.StringVar(value="0.0")
        self.ans = None
        self.differentiate = ctk.StringVar(value="off")
        self.display_num = []
        self.operation = []
        self.trigo_num = []
        self.log_num = []
        self.num = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "("]
        self.trigo_bool = False
        self.log_bool = False
        self.shift = False
        self.shift_button = None
        # !-------------WIDGETS------------------------------
        self.entry = Entry(self, self.result, self.formula)

        self.frame_normal = NumberFrame(self, self.num_press)
        self.frame_scientific = ScientificFrame(self, self.num_press)
        self.frame_programmer = Programmer(
            self, self.binary, self.decimal, self.hexadecimal, self.octal
        )
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
        self.kilograms.trace("w", self.kilograms_trace)
        self.pounds.trace("w", self.pounds_trace)
        self.celcius.trace("w", self.celcius_trace)
        self.fahrenheit.trace("w", self.fahrenheit_trace)
        self.metres.trace("w", self.metres_trace)
        self.inches.trace("w", self.inches_trace)

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
        self.bind("<Escape>", lambda _: self.quit())
        # * -----------START APP ----------------------
        self.scientific("Normal")
        self.mainloop()

    def plot_graph(self, equation):
        x = np.linspace(-10, 10)
        y = eval(equation)
        plt.plot(x, y, label=equation)
        plt.ylabel("y-axis")
        plt.xlabel("x-axis")
        plt.legend()
        plt.grid()
        try:
            plt.show(block=True)
        except:
            pass

    # !-----------------TRACING-------------------

    # Function to trace the entry of the binary number and convert it to decimal, hexadecimal and octal
    def binary_trace(self, *args):
        binary = self.binary.get()
        try:
            bin = int(binary, 2)
            self.decimal.set(str(bin))
            self.hexadecimal.set(str(hex(bin)[2:]).upper())
            self.octal.set(str(oct(bin)[2:]))
        except:
            pass

    # Function to trace the entry of the decimal number and convert it to binary, hexadecimal and octal
    def decimal_trace(self, *args):
        decimal = self.decimal.get()
        try:
            self.binary.set(bin(int(decimal))[2:])
            self.octal.set(oct(int(decimal))[2:])
            self.hexadecimal.set(hex(int(decimal))[2:].upper())
        except:
            pass

    # Function to trace the entry of the hexadecimal number and convert it to binary, decimal and octal
    def hexadecimal_trace(self, *args):
        hexa = self.hexadecimal.get()
        try:
            self.binary.set(bin(int(hexa, 16))[2:])
            self.decimal.set(int(hexa, 16))
            self.octal.set(oct(int(hexa, 16))[2:])
        except:
            pass

    # Function to trace the entry of the octal number and convert it to binary, decimal and hexadecimal
    def octal_trace(self, *args):
        oct = self.octal.get()
        try:
            self.binary.set(bin(int(oct, 8))[2:])
            self.decimal.set(int(oct, 8))
            self.hexadecimal.set(hex(int(oct, 8))[2:].upper())
        except:
            pass

    # Function to trace the entry of the kilograms number and convert it to pounds
    def kilograms_trace(self, *args):
        kilograms = self.kilograms.get()
        try:
            self.pounds.set(float(kilograms) * 2.20462)
        except:
            pass

    def pounds_trace(self, *args):
        pounds = self.pounds.get()
        try:
            self.kilograms.set(float(pounds) * 0.453592)
        except:
            pass

    def celcius_trace(self, *args):
        celcius = self.celcius.get()
        try:
            self.fahrenheit.set(float(celcius) * 1.8 + 32)
        except:
            pass

    def fahrenheit_trace(self, *args):
        fahrenheit = self.fahrenheit.get()
        try:
            self.celcius.set((float(fahrenheit) - 32) * 5 / 9)
        except:
            pass

    def metres_trace(self, *args):
        metres = self.metres.get()
        try:
            self.inches.set(float(metres) * 39.3701)
        except:
            pass

    def inches_trace(self, *args):
        inches = self.inches.get()
        try:
            self.metres.set(float(inches) * 0.0254)
        except:
            pass

    # !-----------------THEME-----------------------
    # Function to toggle the theme of the calculator
    def toggle_theme(self):
        theme = ctk.get_appearance_mode()
        print(theme)
        if theme == "Light":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    # !-----------------CALCULATION-------------------
    # Function to calculate the result of the expression
    def calculate_result(self, *args):
        result = "".join(self.display_num)
        operation = "".join(self.operation)
        self.formula.set(result)
        print(operation)
        if self.differentiate.get() == "off":
            try:
                result = eval(operation)
                print(result)
                self.result.set(str(result))
                self.ans = self.result.get()

            except SyntaxError:
                self.result.set("SYNTAX ERROR")
            except ZeroDivisionError:
                self.result.set("MATH ERROR")
        else:
            self.differentiation_operation(operation)
            graph = threading.Thread(target=self.plot_graph, args=(operation,))
            graph.start()

        self.operation.clear()
        self.display_num.clear()

    # Function to get the input from the user
    def num_press(self, value):
        if value == "=":
            # * -----------THREADING TO CALCULATE THE RESULT ----------------------
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
        if self.option.get() == "Normal":
            self.basic_operation(value)

        else:
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
                self.display("²", "**2")

            elif value == "E/Ans":
                if self.shift == False:
                    value = f"{value}"
                    self.display("E", "*10**")
                else:
                    self.display(self.ans, self.ans)

            elif value == "x³/∛":
                if self.shift == False:
                    value = f"{value}"
                    self.display("³", "**3")
                else:
                    self.operation.append("**(1/3)")
                    self.result.set(f"∛({''.join(self.display_num)})")
            elif value == ".":
                self.display(value, value)
            elif value == "^":
                value = f"{value}"
                self.display("^", "**")
            elif value == "𝛑/x":
                if self.shift == False:
                    value = f"{value}"
                    self.display("𝛑", "math.pi")
                elif self.shift == True:
                    if self.differentiate.get() == "on":
                        print("differentiate")
                        self.display("x", "*x")
                    elif self.differentiate.get() == "off":
                        self.display("x", "x")

            elif value == "x!":
                self.factorial_operation()
            elif value == "SHIFT":
                if self.shift == True:
                    self.shift_button.configure(fg_color=GREY)
                    self.shift = False
                else:
                    self.shift_button.configure(fg_color=BLUE)
                    self.shift = True
            else:
                value = f" {value} "
                self.display(value, value)

        elif value in self.num:
            self.display(value, value)

    # Function to perform the factorial operation
    def factorial_operation(self):
        value = self.operation
        self.last_value = "".join(value)
        print(self.last_value)
        for i in range(len(value)):
            self.operation.pop()
        self.display("!", "math.factorial(int(self.last_value))")

    # Function to perform the logarithmic operation
    def logarithmic_operation(self, value):
        log_operation = ["log", "ln"]
        if value in log_operation:
            self.trigo_bool = False
            self.log_bool = True
            if value == "log":
                self.display("log(", "math.log10(")
            elif value == "ln":
                self.display("ln(", "math.log(")
        else:
            pass

    # Function to perform the differentiation operation
    def differentiation_operation(self, formula):
        x = sp.Symbol("x")
        printer = SuperscriptPrinter()
        try:
            formula = sp.sympify(formula)
            derivative = sp.diff(formula, x)
            self.display_num.clear()
            self.operation.clear()
            derivative_str = printer.doprint(derivative)
            self.display(derivative_str, derivative_str)
            self.history.append(derivative_str)

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
                if value == "sin/sin⁻¹":
                    self.display("sin(", "math.sin(math.radians(")
                elif value == "cos/cos⁻¹":
                    self.display("cos(", "math.cos(math.radians(")
                elif value == "tan/tan⁻¹":
                    self.display("tan(", "math.tan(math.radians(")
                elif value == "sinh":
                    self.trigo_bool = False
                    self.display("sinh(", "math.sinh(")
                elif value == "cosh":
                    self.trigo_bool = False
                    self.display("cosh(", "math.cosh(")
                elif value == "tanh":
                    self.trigo_bool = False
                    self.display("tanh(", "math.tanh(")
                else:
                    pass
            else:
                if value == "sin/sin⁻¹":
                    self.display("sin⁻¹(", "math.degrees(math.asin(")
                elif value == "cos/cos⁻¹":
                    self.display("cos⁻¹(", "math.degrees(math.acos(")
                elif value == "tan/tan⁻¹":
                    self.display("tan⁻¹(", "math.degrees(math.atan(")
                self.shift = False

    # Function to change the calculator option
    def scientific(self, choice):
        #
        if choice == "Scientific":
            self.frame_converter.place_forget()
            self.diff_widget.place(relx=0.5, rely=0.0, anchor="ne")
            self.frame_normal.grid_forget()
            self.frame_programmer.place_forget()
            self.entry.grid(column=0, row=0, sticky="nsew")
            self.frame_scientific.grid(column=0, row=1, sticky="nsew")

        elif choice == "Normal":
            self.frame_converter.place_forget()
            self.diff_widget.place_forget()
            self.frame_programmer.place_forget()
            self.frame_scientific.grid_forget()
            self.entry.grid(column=0, row=0, sticky="nsew")
            self.frame_normal.grid(column=0, row=1, sticky="nsew")

        elif choice == "Programmer":
            self.frame_converter.place_forget()
            self.diff_widget.place_forget()
            self.entry.grid_forget()
            self.frame_scientific.grid_forget()
            self.frame_normal.grid_forget()
            self.frame_programmer.place(
                relx=0.0, rely=0.0, anchor="nw", relwidth=1, relheight=1
            )
        elif choice == "Converter":
            self.diff_widget.place_forget()
            self.entry.grid_forget()
            self.frame_scientific.grid_forget()
            self.frame_normal.grid_forget()
            self.frame_programmer.grid_forget()
            self.frame_converter.place(
                relx=0.0, rely=0.0, anchor="nw", relwidth=1, relheight=1
            )


if __name__ == "__main__":
    App()
