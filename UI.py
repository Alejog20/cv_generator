import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.layout import Layout
from rich.traceback import install

install()

from main import generate_cv_pdf

console = Console()

def display_header():
    """Displays a professional application header."""
    console.clear()
    header_text = Text("🚀 Enterprise CV Generator System", style="bold white on blue", justify="center")
    header_panel = Panel(header_text, border_style="blue", padding=(1, 2))
    console.print(header_panel)
    console.print("[dim]Version 2.0 | ScotiaGBS Application Target[/dim]\n", justify="center")

def main():
    display_header()
    
    # Simple interactive menu
    console.print("[bold cyan]System Initialization Sequence[/bold cyan]")
    console.print("1. Target Role: [green]Associate Automation Developer[/green]")
    console.print("2. Target Company: [green]ScotiaGBS[/green]\n")
    
    # Prompt the user for a custom filename
    default_filename = "Alejandro_Garcia_Automation_CV.pdf"
    user_filename = Prompt.ask(
        "[bold yellow]Enter output filename[/bold yellow]", 
        default=default_filename
    )
    
    # Add .pdf extension if the user forgot it
    if not user_filename.endswith(".pdf"):
        user_filename += ".pdf"
    
    console.print("\n")

    # Use rich's status spinner for a professional loading effect
    with console.status(f"[bold green]Compiling ATS-optimized CV: {user_filename}...", spinner="dots"):
        # Artificial delay to show off the cool spinner (remove in production if desired)
        time.sleep(1.5) 
        
        # Call the backend engine
        success, message = generate_cv_pdf(output_filename=user_filename)

    # Handle the results gracefully
    if success:
        success_panel = Panel(
            Text(f" PROCESS COMPLETE\n\n{message}", justify="center", style="bold green"),
            border_style="green"
        )
        console.print(success_panel)
        console.print("\n[bold]Next Step:[/bold] Review the PDF and prepare your ScotiaGBS application.")
    else:
        error_panel = Panel(
            Text(f" GENERATION FAILED\n\n{message}", justify="left", style="bold red"),
            border_style="red",
            title="System Error"
        )
        console.print(error_panel)
        console.print("\n[bold yellow]Troubleshooting Tip:[/bold yellow] If you see an OS/Dependency error on Windows, you likely need to install GTK3. Search 'WeasyPrint Windows Installation' for the official guide.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Process aborted by user.[/bold red]")
        sys.exit(0)