import tkinter as tk
from calculator import Calculator
 
class CalculatorApp:
    def __init__(self):
        self.root = root
        self.root.title("Simple Calculator")
        self.calc = Calculator()
        self.display = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
        self.display.grid(row=0, column=0, columnspan=4)
        self.create_buttons()   
        buttons=[
            (7,1,0),
            (8,1,1),
            (9,1,2),
            ('/',1,3),
            (4,2,0),
            (5,2,1),
            (6,2,2),
            ('*',2,3),
            (1,3,0),
            (2,3,1),
            (3,3,2),
            ('-',3,3),
            (0,4,0),
            ('+',4,1),
            ('=',4,2),
            ('C',4,3)
        ]
        for (text, row, col) in buttons:
            button=tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: self.on_button_click(t))
    
    def on_button_click(self,char):
        if char=='C':
            self.display.delete(0, tk.END)
        elif char=='=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)  
                self.display.insert(0, str(result))

            except Exception as e:
                self.display.delete(0, tk.END)  
                self.display.insert(0, "Error")
        else:
            current_text = self.display.get()
            self.display.delete(0, tk.END)  
            self.display.insert(0, current_text + str(char))
    if __name__ == "__main__":
        root = tk.Tk()
        app = Calculator(root)
        root.mainloop()
