import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from settings import *


class App(ctk.CTk):
    def __init__(self):

        # window setup
        super().__init__(fg_color=GREEN)
        self.title("BMI CALCULATOR")
        self.geometry("400x400")
        self.resizable(False, False)

        # data
        self.height_int = ctk.IntVar(value=170)
        self.weight_float = ctk.DoubleVar(value=65)
        self.bmi_string = ctk.StringVar()
        self.update_bmi()

        # tracing - check if any variable is changed, then again call the function and update the output
        self.height_int.trace('w', self.update_bmi)  # 'w' --> writing into
        self.weight_float.trace('w', self.update_bmi)
        # in using this, tkinter adds some couple of new arguments in the update_bmi, so we pass it down as *args

        # widgets
        ResultText(parent=self, bmi_string=self.bmi_string)
        WeightInput(parent=self, weight_var=self.weight_float)
        HeightInput(parent=self, height_var=self.height_int)
        UnitSwitcher(parent=self)

        # layout
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1, uniform="a")
        self.rowconfigure(index=1, weight=1, uniform="a")
        self.rowconfigure(index=2, weight=1, uniform="a")
        self.rowconfigure(index=3, weight=1, uniform="a")

        self.mainloop()

    def update_bmi(self, *args):
        height_meter = self.height_int.get() / 100  # to get in meters
        weight_kg = self.weight_float.get()
        bmi_result = round(weight_kg / height_meter**2, 2)
        self.bmi_string.set(bmi_result)


class ResultText(ctk.CTkLabel):
    def __init__(self, parent, bmi_string):
        font = ctk.CTkFont(family=FONT, size=MAIN_TEXT_SIZE, weight="bold")
        super().__init__(master=parent, text=22.5, font=font, text_color=WHITE, textvariable=bmi_string)
        self.grid(column=0, row=0, rowspan=2, sticky='nsew', )


class WeightInput(ctk.CTkFrame):
    def __init__(self, parent, weight_var):
        self.weight_var = weight_var
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(column=0, row=2, sticky="nsew", padx=10, pady=10)

        # layout
        self.rowconfigure(index=0, weight=1, uniform="b")
        self.columnconfigure(index=0, weight=2, uniform="b")  # weights here act like row-span in one sense
        self.columnconfigure(index=1, weight=1, uniform="b")
        self.columnconfigure(index=2, weight=3, uniform="b")
        self.columnconfigure(index=3, weight=1, uniform="b")
        self.columnconfigure(index=4, weight=2, uniform="b")

        # text
        font = ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE)
        label = ctk.CTkLabel(self, text="70kg", text_color=BLACK, font=font)
        label.grid(row=0, column=2)

        # buttons
        minus_button = ctk.CTkButton(self, text='-',
                                     font=font, text_color=BLACK, fg_color=LIGHT_GRAY,
                                     hover_color=GRAY, corner_radius=BUTTON_CORNER_RADIUS,
                                     command=lambda: self.update_weight_method(('minus', 'large')))
        minus_button.grid(column=0, row=0, sticky="ns", padx=8, pady=8)
        # -----------------------------------------------------------------------
        plus_button = ctk.CTkButton(self, text='+',
                                    font=font, text_color=BLACK, fg_color=LIGHT_GRAY,
                                    hover_color=GRAY, corner_radius=BUTTON_CORNER_RADIUS,
                                    command=lambda: self.update_weight_method(('plus', 'large')))
        plus_button.grid(column=4, row=0, sticky="ns", padx=8, pady=8)
        # -----------------------------------------------------------------------
        small_plus_button = ctk.CTkButton(self, text='+',
                                          font=font, text_color=BLACK, fg_color=LIGHT_GRAY,
                                          hover_color=GRAY, corner_radius=BUTTON_CORNER_RADIUS,
                                          command=lambda: self.update_weight_method(('plus', 'small')))
        small_plus_button.grid(column=3, row=0, padx=4, pady=4)
        # -----------------------------------------------------------------------
        small_minus_button = ctk.CTkButton(self, text='-',
                                           font=font, text_color=BLACK, fg_color=LIGHT_GRAY,
                                           hover_color=GRAY, corner_radius=BUTTON_CORNER_RADIUS,
                                           command=lambda: self.update_weight_method(('minus', 'small')))
        small_minus_button.grid(column=1, row=0, padx=4, pady=4)

    # We need a functon which changes the weight var accordingly to the 4 buttons
    def update_weight_method(self, info=None):
        # info gets which button we are pressing, like ('minus', 'small')
        amount = 1 if info[1] == 'large' else 0.1  # if large change by 1 kg else 0.1 kg
        if info[0] == 'plus':
            self.weight_var.set(self.weight_var.get() + amount)
        else:
            self.weight_var.set(self.weight_var.get() - amount)


class HeightInput(ctk.CTkFrame):
    def __init__(self, parent, height_var):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

        # widgets
        slider = ctk.CTkSlider(master=self,
                               button_color=GREEN,
                               button_hover_color=GRAY,
                               progress_color=GREEN,
                               fg_color=LIGHT_GRAY,
                               variable=height_var,
                               from_=100,
                               to=250)
        slider.pack(side='left', fill="x", expand=True, pady=10, padx=10)

        output_text = ctk.CTkLabel(master=self,
                                   text="1.80m",
                                   text_color=BLACK,
                                   font=ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE),
                                   )
        output_text.pack(side="left", padx=20)


class UnitSwitcher(ctk.CTkLabel):
    def __init__(self, parent):
        super().__init__(master=parent, text="metric", text_color=DARK_GREEN,
                         font=ctk.CTkFont(family=FONT, size=SWITCH_FONT_SIZE, weight="bold"))
        self.place(relx=0.98, rely=0.01, anchor='ne')



if __name__ == '__main__':
    App()

