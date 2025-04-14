import tkinter as tk
from calculator import Calculator

class CalculatorApp:
    def __init__(self, root):
        self.calc = Calculator()
        self.root = root
        self.root.title("Python Calculator")
        
        # Entry widget for display
        self.display = tk.Entry(root, width=20, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4)
        
        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, padx=20, pady=20, 
                              command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)
    
    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                result = eval(self.display.get())  # Simple evaluation (caution!)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()