import os
import asyncio
import platform
import anyio
from dotenv import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    _original_open_process = anyio.open_process
    async def _patched_open_process(*args, **kwargs):
        kwargs.pop("user", None)
        return await _original_open_process(*args, **kwargs)
    anyio.open_process = _patched_open_process

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

TARGET_DIR = "/path/to/your/project"

TASK = f"""
Analyze the project at {TARGET_DIR} and update any outdated dependencies.

Steps:
1. Read the requirements.txt (or package.json) to see current versions
2. Check for newer versions of each dependency
3. Update the dependency file with compatible versions
4. Install the updated dependencies
5. Run the test suite to verify nothing broke

If you encounter any breaking changes or are unsure about a dependency update,
use AskUserQuestion to clarify with the human before proceeding.
"""

options = ClaudeAgentOptions(
    allowed_tools=["Bash", "Edit", "Write", "AskUserQuestion"],
    permission_mode="bypassPermissions",
    model="claude-haiku-4-5-20251001",
)

async def run_agent():
    result = ""
    async for message in query(prompt=TASK, options=options):
        if hasattr(message, 'content'):
            result = message.content
    return result

def main():
    response = asyncio.run(run_agent())
    print("\n--- Agent Response ---\n")
    print(response)

if __name__ == "__main__":
    main()
