import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('My App')
        self.geometry('800x600')
        self.configure(bg = '#1E1E2E')
        self.resizable(True, True)
        self.__build_ui()
    
        
    def __build_ui(self):
        label = tk.Label(self, text="""Hello World
                         My name is the LOST BOY of NEVERLAND,
                         and this is my story.
                         
                         
                         """,
                            fg='#00FFFF', bg='#1E1E2E',
                            font=('Arial', 24, 'bold'))
                    
        label.pack(pady=40)
        
        
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
