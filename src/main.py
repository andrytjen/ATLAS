from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

from scanner import scan_folder

console = Console()

console.print(
    Panel.fit(
        "[bold cyan]Atlas[/bold cyan]\nDuplicate Finder v0.1",
        title="Atlas",
    )
)

folder = Prompt.ask("Folder to scan")

#files, size = scan_folder(folder)

#console.print()
#console.print(f"[green]Files:[/green] {files}")
#console.print(f"[green]Size:[/green] {size / (1024*1024):.2f} MB")
hashes = scan_folder(folder)

duplicates = 0

for file_hash, files in hashes.items():
    if len(files) > 1:
        duplicates += 1

        console.print(f"\n[red]Duplicate Group[/red]")
        console.print(f"Hash: {file_hash[:16]}...")

        for file in files:
            console.print(f"  • {file}")

console.print()
console.print(f"[bold green]Duplicate groups found:[/bold green] {duplicates}")
