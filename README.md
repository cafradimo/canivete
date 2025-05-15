# 🧰 Canivete Suíço Python

Um utilitário Python com diversas ferramentas úteis em um único programa, apresentado com uma interface rica usando a biblioteca Rich.

## 📋 Funcionalidades

1. **🔐 Gerador de Senha Segura** - Gera senhas aleatórias com letras, números e símbolos
2. **🧠 Contador de Palavras** - Conta palavras e caracteres em um texto
3. **🧮 Calculadora de Expressões** - Calcula expressões matemáticas (ex: 2+5*3)
4. **📆 Info de Data e Hora Atual** - Mostra data, hora e dia da semana
5. **⏱ Temporizador (Timer)** - Contagem regressiva em segundos
6. **🎲 Rolagem de Dado** - Simula a rolagem de um dado com N lados

## ⚙️ Requisitos

- Python 3.6+
- Biblioteca Rich (`pip install rich`)

## 🚀 Como Executar

1. Clone o repositório ou baixe o arquivo `app.py`
2. Instale as dependências:
   ```bash
   pip install rich
   ```
3. Execute o programa:
   ```bash
   python app.py
   ```

## 🖥️ Interface

O programa apresenta um menu interativo formatado com tabelas e painéis coloridos:

```
🧰 Canivete Suíço Python - Menu de Utilidades
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Opção  ┃ Utilidade                    ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1      │ 🔐 Gerador de Senha Segura   │
│ 2      │ 🧠 Contador de Palavras      │
│ 3      │ 🧮 Calculadora de Expressões │
│ 4      │ 📆 Info de Data e Hora Atual │
│ 5      │ ⏱ Temporizador (Timer)      │
│ 6      │ 🎲 Rolagem de Dado           │
│ 0      │ 🚪 Sair                      │
└────────┴──────────────────────────────┘
```

## 📝 Exemplos de Uso

### Gerador de Senha
```
🔐 Gerador de Senha
Qual o tamanho da senha? [12]: 16
Senha gerada: xK8@qL#2mZ9!pY4*
```

### Contador de Palavras
```
🧠 Contador de Palavras
Digite o texto para análise: Python é incrível!
Total de palavras: 3
Total de caracteres: 17
```

### Temporizador
```
⏱ Temporizador
Quantos segundos deseja contar? 5
⏳ Iniciando o temporizador...
5...4...3...2...1...
⏰ Tempo esgotado!
```

## 🛠️ Tecnologias Utilizadas

- Python 3
- Biblioteca Rich para interface no terminal
- Módulos padrão: random, string, datetime, time

## 📄 Licença

Este projeto está licenciado sob a licença MIT.
