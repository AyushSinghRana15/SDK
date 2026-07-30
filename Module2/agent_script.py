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

TARGET_DIR = "data"

TASK = f"""
Analyze the project at {TARGET_DIR} and update only PATCH and MINOR versions.
Do not upgrade major versions (e.g., numpy 1.x stays 1.x, pandas 1.x stays 1.x).

Steps:
1. Read the requirements.txt to see current versions
2. Update only to latest patch/minor within current major version
3. Install the updated dependencies
4. Run the test suite to verify nothing broke

If you encounter any issues, stop and report what happened.
"""

async def can_use_tool(tool_name: str, input_data: dict, context):
    if tool_name in ("Bash", "Edit", "Write"):
        print(f"[AUTHORIZATION REQUIRED] Allow {tool_name}?")
        response = input(f"Allow {tool_name}? (y/n): ")
        if response.lower() == 'y':
            return {"behavior": "allow", "updatedInput": input_data}
        return {"behavior": "deny"}
    return {"behavior": "allow", "updatedInput": input_data}

options = ClaudeAgentOptions(
    allowed_tools=["Bash", "Edit", "Write"],
    permission_mode="default",
    can_use_tool=can_use_tool,
    model="claude-haiku-4-5-20251001",
)

async def prompt_stream():
    yield {
        "type": "user",
        "message": {"role": "user", "content": TASK},
        "parent_tool_use_id": None,
        "session_id": "",
    }

async def run_agent():
    response = ""
    async for message in query(prompt=prompt_stream(), options=options):
        if hasattr(message, 'content'):
            content = message.content
            if isinstance(content, list):
                texts = [getattr(b, 'text', str(b)) for b in content]
                response = "\n".join(texts)
            else:
                response = content
        if hasattr(message, "result") and message.result:
            response = message.result
    return response

def main():
    response = asyncio.run(run_agent())
    print("\n--- Agent Response ---\n")
    print(response)

if __name__ == "__main__":
    main()
