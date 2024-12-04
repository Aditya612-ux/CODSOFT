import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.result_var, font=('calibri', 30), bd=10, insertwidth=2, width=20, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Create buttons
        buttons = [
            'AC','+\-','%','/',
            '7','8','9','*',
            '4','5','6','-',
            '1','2','3','+',
            '0','.','=',
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(master, text=button, padx=20, pady=20, font=('calibri', 16),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == 'AC':
            self.result_var.set("")
        elif char == '=':
            try:
                expression = self.result_var.get()
                result = eval(expression)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            new_text = current_text + str(char)
            self.result_var.set(new_text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()