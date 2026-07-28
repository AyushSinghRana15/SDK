"""Module 1 agent loop demo.

The walkthrough text lives in docs/module1_agent_loop_explanation.md.
This script expects the committed data/ folder to already exist.
"""

import asyncio
import os

from claude_agent_sdk import AssistantMessage, ClaudeAgentOptions, ResultMessage, query
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel


TARGET_DIR = "data"
REPORT_PATH = "todo_fixme_report.md"
TASK = f"""
Scan the codebase located at '{TARGET_DIR}' and identify all TODO and FIXME comments.

For each match, detail:
- Relative file path
- Line number
- Comment text
- Brief summary of the task or issue described

Organize output into a clean markdown document grouped by file.
"""


async def execute_audit(task_prompt: str, agent_options: ClaudeAgentOptions, console: Console) -> str:
    final_output = ""
    console.print("[bold blue]Starting agent loop via query()...[/bold blue]")

    async for message in query(prompt=task_prompt, options=agent_options):
        if isinstance(message, AssistantMessage):
            tool_calls = [
                block.name
                for block in message.content
                if hasattr(block, "type") and block.type == "tool_use"
            ]
            if tool_calls:
                console.print(f"[dim]  → Tool calls requested: {', '.join(tool_calls)}[/dim]")

        if isinstance(message, ResultMessage):
            if message.subtype == "success":
                final_output = message.result or ""
                console.print("[bold green]✓ Execution completed successfully.[/bold green]")
            else:
                final_output = f"Execution stopped with status: {message.subtype}"
                console.print(f"[bold red]✗ Execution stopped: {message.subtype}[/bold red]")

    return final_output


async def run_production_local_explorer(target_path: str, report_filename: str) -> str:
    console = Console()
    console.print(
        Panel(
            "[bold white]Anthropic Agent SDK — Production Local Explorer[/bold white]",
            expand=False,
        )
    )

    load_dotenv()
    if not os.getenv("ANTHROPIC_API_KEY"):
        console.print("[bold red]Error: ANTHROPIC_API_KEY environment variable is not set.[/bold red]")
        return ""

    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Glob", "Grep"],
        model="claude-sonnet-4-5",
    )

    task_prompt = f"""
    Perform a complete codebase health audit on the directory '{target_path}'.
    Search for all TODO and FIXME comments.
    Format your response as a structured markdown report with file paths, line numbers, and issue summaries.
    """

    console.print(f"[cyan]Target Directory:[/cyan] {target_path}")
    console.print(f"[cyan]Allowed Tools Whitelist:[/cyan] {options.allowed_tools}")
    console.print("[bold yellow]Executing agent query loop...[/bold yellow]")

    final_report = await execute_audit(task_prompt, options, console)

    console.print(Panel(Markdown(final_report or "No report was generated."), title="[bold green]Audit Report Summary[/bold green]"))

    with open(report_filename, "w", encoding="utf-8") as report_file:
        report_file.write(final_report)

    console.print(f"[bold cyan]Report saved to disk: '{report_filename}'[/bold cyan]")
    return final_report


def main() -> None:
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

    try:
        response_text = asyncio.run(run_production_local_explorer(TARGET_DIR, REPORT_PATH))
    except Exception as exc:
        response_text = f"Execution failed: {exc}"
        Console().print(f"[bold red]✗ Execution failed: {exc}[/bold red]")

    console = Console()
    console.print("\n[bold cyan]--- Agent Response ---[/bold cyan]\n")
    console.print(Markdown(response_text or "No report was generated."))


if __name__ == "__main__":
    main()