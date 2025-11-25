import tkinter as tk
from tkinter import messagebox
import math

class ScientificCalculator:
    """Uma calculadora científica com interface gráfica usando Tkinter."""

    def __init__(self, master):
        self.master = master
        master.title("Calculadora Científica (Tkinter)")
        master.configure(bg="#2E2E2E")  # Fundo escuro
        
        # Variável para armazenar a expressão atual
        self.current_expression = ""
        
        # Variável para armazenar o resultado da última operação
        self.result = 0
        
        # --- 1. Display ---
        self.display = tk.Entrya(
            master, 
            width=30, 
            font=('Arial', 18), 
            bd=5, 
            relief=tk.FLAT, 
            justify='right',
            bg="#444444",
            fg="white"
        )
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        
        # --- 2. Criação dos Botões ---
        self.create_buttons()

    def create_buttons(self):
        """Define e organiza todos os botões (números, operadores, científicos)."""
        
        # Estilo dos botões
        btn_style = {
            'font': ('Arial', 12, 'bold'), 
            'fg': 'white', 
            'relief': tk.RAISED, 
            'bd': 3, 
            'padx': 15, 
            'pady': 15
        }
        
        # Botões numéricos e de ponto
        num_btn_style = {**btn_style, 'bg': '#555555'}
        # Botões de operadores básicos
        op_btn_style = {**btn_style, 'bg': '#FFA500'}
        # Botões de controle (AC, =, C)
        ctrl_btn_style = {**btn_style, 'bg': '#6A5ACD'}
        # Botões científicos
        sci_btn_style = {**btn_style, 'bg': '#4682B4'}


        # Layout dos botões (Texto, Linha, Coluna, Estilo, Command)
        buttons = [
            # Linha 1: Funções Científicas
            ('AC', 1, 0, ctrl_btn_style, self.clear_all),
            ('C', 1, 1, ctrl_btn_style, self.clear_entry),
            ('√', 1, 2, sci_btn_style, lambda: self.scientific_op('sqrt')),
            ('sin', 1, 3, sci_btn_style, lambda: self.scientific_op('sin')),
            ('cos', 1, 4, sci_btn_style, lambda: self.scientific_op('cos')),
            
            # Linha 2: Mais Funções Científicas e Operador
            ('tan', 2, 0, sci_btn_style, lambda: self.scientific_op('tan')),
            ('log', 2, 1, sci_btn_style, lambda: self.scientific_op('log')),
            ('ln', 2, 2, sci_btn_style, lambda: self.scientific_op('ln')),
            ('(', 2, 3, op_btn_style, lambda: self.append_to_expression('(')),
            (')', 2, 4, op_btn_style, lambda: self.append_to_expression(')')),

            # Linha 3: Números e Operador
            ('7', 3, 0, num_btn_style, lambda: self.append_to_expression('7')),
            ('8', 3, 1, num_btn_style, lambda: self.append_to_expression('8')),
            ('9', 3, 2, num_btn_style, lambda: self.append_to_expression('9')),
            ('/', 3, 3, op_btn_style, lambda: self.append_to_expression('/')),
            ('^', 3, 4, op_btn_style, lambda: self.append_to_expression('**')), # Potência
            
            # Linha 4: Números e Operador
            ('4', 4, 0, num_btn_style, lambda: self.append_to_expression('4')),
            ('5', 4, 1, num_btn_style, lambda: self.append_to_expression('5')),
            ('6', 4, 2, num_btn_style, lambda: self.append_to_expression('6')),
            ('*', 4, 3, op_btn_style, lambda: self.append_to_expression('*')),
            ('pi', 4, 4, sci_btn_style, lambda: self.append_to_expression(str(math.pi))),

            # Linha 5: Números e Operador
            ('1', 5, 0, num_btn_style, lambda: self.append_to_expression('1')),
            ('2', 5, 1, num_btn_style, lambda: self.append_to_expression('2')),
            ('3', 5, 2, num_btn_style, lambda: self.append_to_expression('3')),
            ('-', 5, 3, op_btn_style, lambda: self.append_to_expression('-')),
            ('e', 5, 4, sci_btn_style, lambda: self.append_to_expression(str(math.e))),

            # Linha 6: Números e Operadores Especiais
            ('0', 6, 0, num_btn_style, lambda: self.append_to_expression('0')),
            ('.', 6, 1, num_btn_style, lambda: self.append_to_expression('.')),
            ('=', 6, 2, ctrl_btn_style, self.calculate),
            ('+', 6, 3, op_btn_style, lambda: self.append_to_expression('+')),
        ]

        # Posiciona os botões na grade
        for (text, row, col, style, command) in buttons:
            button = tk.Button(self.master, text=text, **style, command=command)
            # O botão '=' se estende por 2 colunas
            if text == '=':
                button.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
            else:
                button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
                
        # Garante que as colunas se expandam uniformemente
        for i in range(5):
            self.master.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.master.grid_rowconfigure(i, weight=1)

    # --- 3. Métodos de Evento (Manipuladores de Clique) ---

    def append_to_expression(self, text):
        """Adiciona o texto (número ou operador) à expressão atual."""
        self.current_expression += str(text)
        self.update_display()

    def clear_all(self):
        """Limpa a expressão e o resultado (AC - All Clear)."""
        self.current_expression = ""
        self.result = 0
        self.update_display()

    def clear_entry(self):
        """Remove o último caractere da expressão (C - Clear)."""
        self.current_expression = self.current_expression[:-1]
        self.update_display()
    
    def scientific_op(self, op):
        """Aplica uma operação científica à expressão atual."""
        try:
            # Tenta calcular o resultado da expressão atual para usar o último valor
            # Ex: Se a expressão é '5+', o resultado é 5
            current_value = eval(self.current_expression)
        except Exception:
            # Se não conseguir, assume que o usuário quer aplicar a função no 'display'
            current_value = self.result if self.result != 0 else 0
        
        try:
            if op == 'sqrt':
                new_value = math.sqrt(current_value)
            elif op == 'sin':
                new_value = math.sin(math.radians(current_value)) # Converte para radianos
            elif op == 'cos':
                new_value = math.cos(math.radians(current_value)) # Converte para radianos
            elif op == 'tan':
                new_value = math.tan(math.radians(current_value)) # Converte para radianos
            elif op == 'log':
                new_value = math.log10(current_value) # Logaritmo base 10
            elif op == 'ln':
                new_value = math.log(current_value) # Logaritmo natural (base e)
            else:
                return

            self.result = new_value
            self.current_expression = str(new_value)
            self.update_display()
            
        except ValueError as e:
            messagebox.showerror("Erro Científico", f"Erro: {e}\nEntrada inválida para a função.")
            self.clear_all()
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida para função científica.")
            self.clear_all()

    def calculate(self):
        """Avalia a expressão matemática e exibe o resultado."""
        try:
            # Usa eval() para calcular o resultado da string de expressão
            self.result = eval(self.current_expression)
            self.current_expression = str(self.result)
            self.update_display()
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Divisão por zero não é permitida.")
            self.clear_all()
        except SyntaxError:
            messagebox.showerror("Erro", "Expressão matemática inválida.")
            self.clear_all()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
            self.clear_all()

    def update_display(self):
        """Atualiza o widget Entry com a expressão atual."""
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_expression)


# --- 4. Inicialização da Aplicação ---
if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()