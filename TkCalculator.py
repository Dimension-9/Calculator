import tkinter as tk

# COLOR
bg_color = "light green"
fg_color = "red"
bg_color_btn = "yellow"

class Calculator:
    def __init__(self):
        size = "400x450"
        self.root = tk.Tk()
        self.root.geometry(size)

        self.string_var = tk.StringVar()

        # TextField
        self.textField = tk.Entry(self.root, textvariable=self.string_var, justify=tk.RIGHT, font="arial 50")
        self.textField.place(x=0, y=0, height=200, width=size[:3])

        # # Ans label
        # self.label_var = tk.StringVar()
        # self.label = tk.Label(self.root, textvariable=self.label_var, relief=tk.RAISED)
        # self.label_var.set("Ans = ")
        # self.label.place(x=400, y=500, height=50, width=100)

        # Ans
        self.ans_string_var = tk.StringVar()
        # Ans textField
        self.ansTextField = tk.Entry(self.root, textvariable=self.ans_string_var, justify=tk.RIGHT, font="arial 20")
        self.ansTextField.place(x=0, y=0, height=50, width=400)

        # Utility functions
        # Reading button's value
        def read_button(x):
            if self.ansTextField.get() == self.textField.get():
                self.textField.delete(0, tk.END)
            value = str(x)
            self.textField.insert(10000, value)
            # self.string_var.set(value)

        # AC button function
        def clear_text():
            self.textField.delete(0, tk.END)
            self.ansTextField.delete(0, tk.END)

        # Backspace button function
        def backspace():
            value = self.textField.get()
            self.string_var.set(value[:-1])

        # Equal button function to evaluate result
        def evaluate():
            value = self.textField.get()
            try:
                self.string_var.set(eval(value))
                set_ans()
            except:
                self.string_var.set("undefined")
                self.ans_string_var.set("0")

        def set_ans():
            value = self.textField.get()
            self.ans_string_var.set(value)

        # Buttons
        def buttons_():
            # background color
            global bg_color
            global fg_color
            global bg_color_btn
            # 0-9 buttons
            b0 = tk.Button(self.root, text="0", command=lambda: read_button('0'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b1 = tk.Button(self.root, text="1", command=lambda: read_button('1'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b2 = tk.Button(self.root, text="2", command=lambda: read_button('2'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b3 = tk.Button(self.root, text="3", command=lambda: read_button('3'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b4 = tk.Button(self.root, text="4", command=lambda: read_button('4'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b5 = tk.Button(self.root, text="5", command=lambda: read_button('5'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b6 = tk.Button(self.root, text="6", command=lambda: read_button('6'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b7 = tk.Button(self.root, text="7", command=lambda: read_button('7'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b8 = tk.Button(self.root, text="8", command=lambda: read_button('8'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b9 = tk.Button(self.root, text="9", command=lambda: read_button('9'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)

            # operators buttons
            b_add = tk.Button(self.root, text="+", command=lambda: read_button('+'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b_sub = tk.Button(self.root, text="-", command=lambda: read_button('-'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b_mul = tk.Button(self.root, text="*", command=lambda: read_button('*'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b_div = tk.Button(self.root, text="/", command=lambda: read_button('/'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b_power = tk.Button(self.root, text="^", command=lambda: read_button('^'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b_modulus = tk.Button(self.root, text="%", command=lambda: read_button('%'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b_dot = tk.Button(self.root, text=".", command=lambda: read_button('.'), activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b_equal = tk.Button(self.root, text="=", command=evaluate, activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)

            # Utility buttons
            b_clear = tk.Button(self.root, text="AC", command=clear_text, activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)
            b_backspace = tk.Button(self.root, text="del", command=backspace, activebackground=bg_color, activeforeground=fg_color, bg=bg_color_btn)

            ############################################################################################################
            # Placing all buttons on the screen // packing buttons
            # Row 1
            b_clear.place(x=0, y=200, height=50, width=100)
            b_backspace.place(x=100, y_=200, height=50, width=100)
            b_modulus.place(x=200, y=200, height=50, width=100)
            b_div.place(x=300, y=200, height=50, width=100)

            # Row 2
            b7.place(x=0, y=250, height=50, width=100)
            b8.place(x=100, y=250, height=50, width=100)
            b9.place(x=200, y=250, height=50, width=100)
            b_mul.place(x=300, y=250, height=50, width=100)

            # Row 3
            b4.place(x=0, y=300, height=50, width=100)
            b5.place(x=100, y=300, height=50, width=100)
            b6.place(x=200, y=300, height=50, width=100)
            b_sub.place(x=300, y=300, height=50, width=100)

            # Row 4
            b1.place(x=0, y=350, height=50, width=100)
            b2.place(x=100, y=350, height=50, width=100)
            b3.place(x=200, y=350, height=50, width=100)
            b_add.place(x=300, y=350, height=50, width=100)

            # Row 5
            b_power.place(x=0, y=400, height=50, width=100)
            b0.place(x=100, y=400, height=50, width=100)
            b_dot.place(x=200, y=400, height=50, width=100)
            b_equal.place(x=300, y=400, height=50, width=100)

        buttons_()

        self.root.mainloop()


if __name__ == '__main__':
    x = Calculator()
