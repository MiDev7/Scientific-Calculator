from settings import *
import customtkinter as ctk
from sympy.printing.str import StrPrinter


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
    def __init__(self, parent, kilograms, pounds, celcius, fahrenheit, metres, inches):
        super().__init__(master=parent, fg_color=PRIMARY)

        # !---------------WIDGET-------------------


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
        base = self._print(expr.base, **kwargs)
        exponent = self._print(expr.exp, **kwargs)
        return base + "⁽" + exponent + "⁾"
