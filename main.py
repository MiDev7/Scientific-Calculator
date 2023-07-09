from settings import *
import threading, time
import math
import customtkinter as ctk
import sympy as sp
from sympy.printing.str import StrPrinter


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

        # Multithreading

        #! --------------VARIABLE--------------------------
        self.formula = ctk.StringVar(value="")
        self.result = ctk.StringVar(value="0")
        self.differentiate = ctk.StringVar(value="off")
        self.display_num = []
        self.operation = []
        self.trigo_num = []
        self.log_num = []
        self.num = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "("]
        self.trigo_bool = False
        self.log_bool = False
        self.shift = False
        # !-------------WIDGETS------------------------------
        Entry(self, self.result, self.formula)

        self.frame_normal = NumberFrame(self, self.num_press)
        self.frame_scientific = ScientificFrame(self, self.num_press)
        # testing

        self.option = ctk.CTkOptionMenu(
            self,
            values=["Normal", "Scientific"],
            fg_color=ACCENTBROWN,
            dropdown_fg_color=ACCENTBROWN,
            width=100,
            button_color=DEEPBROWN,
            button_hover_color=ACCENTBROWN,
            text_color=PRIMARY,
            corner_radius=5,
            dropdown_text_color=PRIMARY,
            dropdown_hover_color=DEEPBROWN,
            command=self.scientific,
        )

        self.option.place(relx=0.0, rely=0.0, anchor="nw")

        self.diff_widget = ctk.CTkCheckBox(
            self,
            text="Differentiate",
            variable=self.differentiate,
            fg_color=ACCENTBROWN,
            text_color=ACCENTBROWN,
            checkbox_height=20,
            checkbox_width=20,
            onvalue="on",
            offvalue="off",
            checkmark_color=PRIMARY,
            border_color=ACCENTBROWN,
            hover_color=DEEPBROWN,
            command=lambda: print(self.differentiate.get()),
        )

        self.diff_widget.place(relx=0.5, rely=0.0, anchor="ne")

        # * -----------KEY BINDING TO EXIT THE APP -------------------------
        self.bind("<Escape>", lambda _: self.quit())
        # * -----------START APP ----------------------
        self.scientific("Normal")
        self.mainloop()

    def num_press(self, value):
        if value == "=":
            result = "".join(self.display_num)
            operation = "".join(self.operation)
            self.formula.set(result)
            print(operation)
            if self.differentiate.get() == "off":
                try:
                    self.result.set(eval(operation))

                except SyntaxError:
                    self.result.set("SYNTAX ERROR")

                except ZeroDivisionError:
                    self.result.set("MATH ERROR")
                    self.operation.clear()
                    self.display_num.clear()
                return
            else:
                self.differentiation_operation(operation)
        elif value == "Del":
            self.display_num.pop()
            self.operation.pop()
            self.result.set("".join(self.display_num))
            return

        elif value == "AC":
            self.display_num.clear()
            self.operation.clear()
            self.result.set("")
            return

        elif value == ")":
            if self.trigo_bool:
                self.operation.append(")")
                self.display(value, value)
            else:
                self.display(value, value)

        if self.option.get() == "Normal":
            self.basic_operation(value)

        else:
            self.basic_operation(value)
            self.trigonometry_operation(value)
            self.logarithmic_operation(value)
            print(self.operation)

    def display(self, value, operation):
        self.display_num.append(value)
        self.operation.append(operation)
        self.result.set("".join(self.display_num))

    def basic_operation(self, value):
        math_operation = [
            "+",
            "-",
            "x",
            "/",
            "x²",
            "√",
            "E",
            "x³",
            "𝛑/x",
            "x!",
            "^",
            "SHIFT",
        ]
        self.formula.set("")
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

            elif value == "E":
                value = f"{value}"
                self.display("E", "*10**")

            elif value == "x³":
                value = f"{value}"
                self.display("³", "**3")
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
                self.shift = True
            else:
                value = f" {value} "
                self.display(value, value)

        elif value in self.num:
            self.display(value, value)

    def factorial_operation(self):
        self.last_value = self.operation[-1]
        self.operation.pop()
        self.display("!", "math.factorial(int(self.last_value))")

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
        except sp.SympifyError:
            self.result.set("SYNTAX ERROR")

    def trigonometry_operation(self, value):
        trigo_operation = [
            "sin/sin⁻¹",
            "cos/cos⁻¹",
            "tan/tan⁻¹",
            "sinh",
            "cosh",
            "tanh",
        ]

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

    def scientific(self, choice):
        if choice == "Scientific":
            self.frame_normal.grid_forget()
            self.frame_scientific.grid(column=0, row=1, sticky="nsew")

        if choice == "Normal":
            self.frame_scientific.grid_forget()
            self.frame_normal.grid(column=0, row=1, sticky="nsew")


class Entry(ctk.CTkFrame):
    def __init__(self, parent, result, formula):
        super().__init__(master=parent, bg_color=PRIMARY, fg_color=PRIMARY)

        self.grid(column=0, row=0, sticky="nsew")  # take max space in 4 directions

        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1), weight=1)

        font2 = ctk.CTkFont(family=FONT, size=LARGE, weight="normal")
        font1 = ctk.CTkFont(family=FONT, size=SMALL, weight="normal")

        formula = ctk.CTkLabel(
            self, text="", font=font1, textvariable=formula, text_color=DEEPBROWN
        )
        result = ctk.CTkLabel(
            self, text="", font=font2, textvariable=result, text_color=DEEPBROWN
        )

        formula.grid(column=0, row=0, sticky="se", padx=10)
        result.grid(column=0, row=1, sticky="e", padx=10)


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
            text_color=PRIMARY,
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


class ScientificFrame(ctk.CTkFrame):
    def __init__(self, parent, func):
        super().__init__(master=parent, fg_color=PRIMARY)
        self.columnconfigure((0, 1, 2, 3), weight=3, uniform="d")
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1, uniform="d")
        for num, data in SCIENTIFIC_BUTTON.items():
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


class SuperscriptPrinter(StrPrinter):
    def _print_Pow(self, expr, **kwargs):
        base = self._print(expr.base, **kwargs)
        exponent = self._print(expr.exp, **kwargs)
        return base + "⁽" + exponent + "⁾"


if __name__ == "__main__":
    App()
