import tkinter as tk
from tkinter import ttk
from tkinter import font
import customtkinter
import customtkinter as ctk
from tkinter import messagebox


# MAIN WINDOW
class App(ctk.CTk):
    def __init__(self, parent_output):
        self.parent_output = parent_output
        super().__init__()
        customtkinter.set_appearance_mode("light")
        self.geometry("450x600")
        # self.maxsize(500, 600)
        # self.minsize(450,  600)
        self.title("UNIT CONVERTER")

        # frames
        self.create_frames()
        print(font.families())
        self.mainloop()

    def create_frames(self):
        top_frame = TopFrame(parent=self, parent_output=parent_output)
        bottom_frame = BottomFrame(parent=self, parent_output=parent_output)
        top_frame.place(relx=0, rely=0, relheight=0.6, relwidth=1)
        bottom_frame.place(relx=0, rely=0.6, relheight=0.4, relwidth=1)


class TopFrame(ctk.CTkFrame):
    def __init__(self, parent, parent_output):
        super().__init__(parent)
        self.parent_output = parent_output
        # TOP NAME LABEL
        name_label = ctk.CTkLabel(master=self,
                                  text="Conversion Aid",
                                  bg_color="#f0295a",
                                  anchor="w",
                                  text_color="white",
                                  font=("Arial CV", 22, "bold"))

        # INPUT FRAME
        input_frame = ctk.CTkFrame(master=self,
                                   fg_color="#f0295a")

        # TEXT NOTICE
        text_button = ctk.CTkButton(master=self,
                                    text="TAP TO CONVERT",
                                    fg_color="#f0295a",
                                    text_color="white",
                                    font=("Arial CV", 10),
                                    anchor="n",
                                    hover_color="#f2164d",
                                    command=self.converter)

        # input frame
        self.values_conversions = ["Meter To Kilometer", "Meter To Miles", "Meter To Feet", "Meter To Inch",
                              "___________________",
                              "Grams To Kilograms", "Kilograms to Pound", "Kilograms to Ton",
                              "___________________",
                              "Celsius (°C) to Fahrenheit (°F)", "Celsius (°C) to Kelvin (K)"]
        self.option_selected = ctk.StringVar(value="Meter To Kilometer")
        conversion_options = ctk.CTkOptionMenu(master=input_frame,
                                               width=150,
                                               height=60,
                                               fg_color="#f0295a",
                                               button_color="#f0295a",
                                               font=("Arial CV", 30, "bold"),
                                               button_hover_color="white",
                                               values=self.values_conversions,
                                               dropdown_font=("Arial CV", 20),
                                               dropdown_text_color="white",
                                               dropdown_fg_color="#f0295a",
                                               dropdown_hover_color="white",
                                               variable=self.option_selected)

        # CONVERSION INPUT FRAME
        conversion_input_frame = ctk.CTkFrame(master=input_frame, fg_color="#f0295a")

        self.input_ = ctk.StringVar()
        conversion_input = ctk.CTkEntry(master=conversion_input_frame,
                                        width=300,
                                        height=60,
                                        fg_color="#f0295a",
                                        font=("Arial CV", 50),
                                        justify="center",
                                        border_color="#f0295a",
                                        text_color="white",
                                        textvariable=self.input_)

        conversion_input_text_down_border = ctk.CTkLabel(master=conversion_input_frame,
                                                         text=" ",
                                                         width=200,
                                                         height=1,
                                                         fg_color="white",
                                                         font=("Arial", 1))

        conversion_options.pack(pady=10)
        conversion_input_frame.pack(pady=10, expand=True, fill="both")

        # CONVERSION INPUT LAYOUT
        conversion_input_frame.columnconfigure(index=0, weight=1, uniform="a")
        conversion_input_frame.rowconfigure(index=0, weight=1)
        conversion_input_frame.rowconfigure(index=0, weight=1)

        conversion_input.grid(row=0, column=0)
        conversion_input_text_down_border.grid(row=1)

        name_label.pack(expand=True, fill="both", padx=10)
        input_frame.pack(expand=True, fill="both", pady=15)
        text_button.pack(expand=True, fill="both")
        self.configure(fg_color="#f0295a")

    # CONVERTER FUNCTION
    def converter(self):
        options = self.values_conversions.copy()
        unit_multipliers = {options[0]: 0.001, options[1]: 0.000621371, options[2]: 3.28084, options[3]: 39.37008,
                            options[5]: 0.001, options[6]: 2.20462, options[7]: 1000,
                            options[9]: 32, options[10]: 273}

        # conversion logic
        input_value = self.input_.get()
        mult = unit_multipliers[self.option_selected.get()]

        if not input_value.isalpha():
            input_value = int(input_value)
            return input_value*mult
        else:
            messagebox.showerror(title="VALUE ERROR", message="Please Enter Int Value :)")
            self.input_.set(value=" ")




class BottomFrame(ctk.CTkFrame):
    def __init__(self, parent, parent_output):
        self.parent_output = parent_output
        super().__init__(parent)

        # main frame to hold everything
        main_frame = ctk.CTkFrame(master=self, fg_color="#DBDBDB")
        main_frame.pack(expand=True, fill="both", pady=50)

        # from unit , to unit
        unit_info = ctk.CTkLabel(master=main_frame,
                                 text=" - Kilometers To Meters - ",
                                 font=("Arial CV",13, "bold"),
                                 text_color="gray")

        # OUTPUT LABEL
        output_label = ctk.CTkLabel(master=main_frame,
                                    text=self.parent_output,
                                    text_color="black",
                                    font=("Arial CV", 50, "bold"))

        unit_info.pack(anchor="center")
        output_label.pack()
        self.configure(fg_color="#DBDBDB")



parent_output = 0
app = App(parent_output)


