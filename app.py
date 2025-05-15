import random, string
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from datetime import datetime
import time

console = Console()

def menu():
    table = Table(title="🧰 Canivete Suíço Python - Menu de Utilidades")
    table.add_column("Opção", justify="center", style="cyan")
    table.add_column("Utilidade", style="magenta")
    table.add_row("1", "🔐 Gerador de Senha Segura")
    table.add_row("2", "🧠 Contador de Palavras")
    table.add_row("3", "🧮 Calculadora de Expressões")
    table.add_row("4", "📆 Info de Data e Hora Atual")
    table.add_row("5", "⏱ Temporizador (Timer)")
    table.add_row("6", "🎲 Rolagem de Dado")
    table.add_row("0", "🚪 Sair")
    console.print(table)

def gerar_senha():
    console.print(Panel("🔐 [bold]Gerador de Senha[/bold]"))
    tamanho = IntPrompt.ask("Qual o tamanho da senha?", default=12)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choices(caracteres, k=tamanho))
    console.print(f"[green]Senha gerada:[/green] [bold yellow]{senha}[/bold yellow]")

def contar_palavras():
    console.print(Panel("🧠 [bold]Contador de Palavras[/bold]"))
    texto = Prompt.ask("Digite o texto para análise")
    palavras = texto.split()
    caracteres = len(texto)
    console.print(f"Total de palavras: [bold cyan]{len(palavras)}[/bold cyan]")
    console.print(f"Total de caracteres: [bold cyan]{caracteres}[/bold cyan]")

def calculadora():
    console.print(Panel("🧮 [bold]Calculadora[/bold]"))
    expressao = Prompt.ask("Digite a expressão (ex: 2+5*3)")
    try:
        resultado = eval(expressao)
        console.print(f"Resultado: [bold green]{resultado}[/bold green]")
    except Exception as e:
        console.print(f"[red]Erro na expressão: {e}[/red]")

def info_data():
    console.print(Panel("📆 [bold]Data e Hora Atual[/bold]"))
    agora = datetime.now()
    console.print(f"📅 Data: [cyan]{agora.strftime('%d/%m/%Y')}[/cyan]")
    console.print(f"🕒 Hora: [cyan]{agora.strftime('%H:%M:%S')}[/cyan]")
    console.print(f"📌 Dia da semana: [cyan]{agora.strftime('%A')}[/cyan]")

def temporizador():
    console.print(Panel("⏱ [bold]Temporizador[/bold]"))
    segundos = IntPrompt.ask("Quantos segundos deseja contar?")
    console.print("⏳ Iniciando o temporizador...")
    for i in range(segundos, 0, -1):
        console.print(f"[yellow]{i}...[/yellow]", end='\r')
        time.sleep(1)
    console.print("[bold green]⏰ Tempo esgotado![/bold green]")

def rolar_dado():
    console.print(Panel("🎲 [bold]Rolagem de Dado[/bold]"))
    lados = IntPrompt.ask("Quantos lados tem o dado?", default=6)
    resultado = random.randint(1, lados)
    console.print(f"Você rolou: [bold magenta]{resultado}[/bold magenta]")

def main():
    while True:
        menu()
        escolha = Prompt.ask("\nEscolha uma opção", choices=["0", "1", "2", "3", "4", "5", "6"])
        if escolha == "1":
            gerar_senha()
        elif escolha == "2":
            contar_palavras()
        elif escolha == "3":
            calculadora()
        elif escolha == "4":
            info_data()
        elif escolha == "5":
            temporizador()
        elif escolha == "6":
            rolar_dado()
        elif escolha == "0":
            console.print("\n👋 Até a próxima!", style="bold green")
            break

if __name__ == "__main__":
    main()