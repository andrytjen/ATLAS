from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

from file_index import group_by_size
from duplicate_finder import find_duplicates

#from scanner import scan_folder

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
#hashes = scan_folder(folder)

size_map = group_by_size(folder)
duplicates = find_duplicates(size_map)

duplicate_groups = len(duplicates)

for file_hash, files in duplicates.items():
    console.print(f"\n[red]Duplicate Group[/red]")
    console.print(f"Hash: {file_hash[:16]}...")

    for file in files:
        console.print(f"  • {file}")

console.print()
console.print(
    f"[bold green]Duplicate groups found:[/bold green] {duplicate_groups}"
)
