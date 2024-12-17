# Sistema de Cadastro Rural - Programa de Segurança Rural

## Descrição

Este é um sistema desenvolvido para o **Programa de Segurança Rural** do **7º Batalhão da Polícia Militar de Rondônia**. O sistema tem como objetivo automatizar o processo de gerar os **PDFs** com os números das propriedades cadastradas.

A aplicação foi construída em **Python** utilizando as bibliotecas **Tkinter** para a interface gráfica e **Fitz (PyMuPDF)** para manipulação de arquivos PDF.

## Funcionalidades

-
- **Geração Automática de PDF**: O sistema gera automaticamente os números  para cada propriedade registrada.
- **Interface Gráfica**: A interface foi desenvolvida com a biblioteca Tkinter, oferecendo uma experiência amigável e intuitiva para o usuário.
- **Manipulação de PDF**: Utiliza a biblioteca Fitz (PyMuPDF) para gerar e manipular documentos PDF, facilitando a criação e o armazenamento de registros oficiais.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do sistema.
- **Tkinter**: Biblioteca de interface gráfica para Python, utilizada para criar as janelas, botões e demais componentes do sistema.
- **Fitz (PyMuPDF)**: Biblioteca para manipulação de arquivos PDF, utilizada para gerar os PDS e documentos relacionados.

## Como Rodar o Sistema

### Requisitos

1. Python >=3.12.3 instalado.
2. Bibliotecas necessárias:
   - Tkinter (já incluído na instalação padrão do Python)
   - Fitz (PyMuPDF)

### Instalação das Dependências

Para instalar a biblioteca Fitz (PyMuPDF), execute o seguinte comando:

```bash
pip install pymupdf
```

### Executando o Sistema

1. Clone o repositório para o seu computador:

```bash
git clone https://github.com/MakalisterAndrade/sistema-automatizador-gerador-placas
```

2. Navegue até o diretório do projeto:

```bash
cd sistema-automatizador-gerador-placas
```

3. Execute o arquivo principal do sistema:

```bash
python Script Original/processa_placas.py
```

Isso abrirá a interface gráfica do sistema onde você poderá gerar os PDF.

## Estrutura do Projeto

```
/sistema-automatizador-gerador-placas
    ├── /placas              # Pasta principal onde são salvos os pdfs(obrigatória)
    ├── /Script Original.py  # Pasta contendo os scripts python
    ├── PLACA.pdf            # Arquivo de modelo para o pdf
    └── README.md            # Este arquivo
```

## Contribuições

Contribuições são bem-vindas! Se você tiver alguma sugestão ou melhoria, sinta-se à vontade para abrir uma **issue** ou enviar um **pull request**.

## Licença

Este projeto está licenciado sob a [Creative Commons License](LICENSE).
