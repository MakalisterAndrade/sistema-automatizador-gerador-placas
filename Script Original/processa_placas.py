import os
import fitz  # PyMuPDF
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def limpar_pasta_placas():
    try:
        folder_path = 'placas'
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        messagebox.showinfo("Concluído", "Pasta 'placas' encontrada e limpa com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao limpar a pasta 'placas'. \
                            Você criou uma pasta chamada 'placas' dentro da pasta raiz? \
                            Você tem um arquivo pdf de dentro da pasta 'placas' que está aberto?")

def processar_dados():
    try:
        limpar_pasta_placas()

        # Caminho do PDF original
        pdf_path = 'PLACA.pdf'

        # Coordenadas da área onde o texto será inserido (x0, y0, x1, y1)
        coordenadas = [(240, 658.6156005859375, 1456.50390625, 808.4784545898438)]

        # Intervalo de placas
        intervalo_inicio = int(input_inicio.get())
        intervalo_fim = int(input_fim.get())

        # Processar o intervalo de placas
        processar_intervalo(pdf_path, coordenadas, intervalo_inicio, intervalo_fim, deslocamento_x=0, deslocamento_y=100)
        messagebox.showinfo("Concluído", "Processamento concluído com sucesso!")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos para o intervalo de placas.")

def inserir_texto_pagina(page, coordenadas, novo_texto, deslocamento_x=0, deslocamento_y=0):
    for area in coordenadas:
        # Criar um retângulo na área especificada
        rect = fitz.Rect(area)

        # Adicionar anotação de redaction para cobrir a área original
        page.add_redact_annot(rect, fill=[1, 1, 1])

    page.apply_redactions()

    for area in coordenadas:
        rect = fitz.Rect(area)
        # Calcular a posição central do retângulo
        center_x = (rect.tl.x + rect.br.x) / 2
        center_y = (rect.tl.y + rect.br.y) / 2
        
        # Ajustar a posição do texto para centralizar no retângulo e aplicar deslocamento
        fontsize = 130  # Ajuste o tamanho da fonte conforme necessário
        text_width = fitz.get_text_length(novo_texto, fontname="helv", fontsize=fontsize)
        text_height = fontsize  # Aproximadamente a altura da fonte
        nova_posicao = fitz.Point(center_x - text_width / 2, center_y - text_height / 2 + deslocamento_y)
        
        page.insert_text(nova_posicao, novo_texto, fontname="helv", fontsize=fontsize, color=(1, 0, 0))

def processar_intervalo(pdf_path, coordenadas, intervalo_inicio, intervalo_fim, deslocamento_x=0, deslocamento_y=0):
    for placa_num in range(intervalo_inicio, intervalo_fim + 1):
        # Abrir o PDF original
        doc = fitz.open(pdf_path)

        # Texto a ser inserido
        novo_texto = f"PROPRIEDADE Nº {placa_num}"

        # Iterar sobre todas as páginas e inserir o texto nas coordenadas especificadas
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            inserir_texto_pagina(page, coordenadas, novo_texto, deslocamento_x, deslocamento_y)

        # Salvar o PDF modificado
        novo_pdf_path = f"placas/PLACA_{placa_num}.pdf"
        doc.save(novo_pdf_path)
        doc.close()

        print(f"Novo PDF salvo em: {novo_pdf_path}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerar Nº Placa em PDF")

# Label e input para o intervalo de placas
label_inicio = ttk.Label(root, text="Número inicial da placa:")
label_inicio.grid(row=0, column=0, padx=5, pady=5)
input_inicio = ttk.Entry(root)
input_inicio.grid(row=0, column=1, padx=5, pady=5)

label_fim = ttk.Label(root, text="Número final da placa:")
label_fim.grid(row=1, column=0, padx=5, pady=5)
input_fim = ttk.Entry(root)
input_fim.grid(row=1, column=1, padx=5, pady=5)

# Botão para processar os dados
btn_processar = ttk.Button(root, text="Gerar PDFs", command=processar_dados)
btn_processar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Label para as informações de contato
label_contato = ttk.Label(root, text="Makalister Andrade da Silva - PVSA\nAuxiliar da Seção Operacional - P3/7ºBPM\nContato: makalister.andrade@outlook.com", justify="center")
label_contato.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
