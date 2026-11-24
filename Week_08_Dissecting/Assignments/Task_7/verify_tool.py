import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


SERVER_PATH = Path(__file__).with_name("server.py")
SAMPLE_TEXT = "MCP tools are ready"


async def main() -> None:
    server = StdioServerParameters(
        command=sys.executable,
        args=[str(SERVER_PATH)],
    )

    async with stdio_client(server) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            if not any(tool.name == "count_words" for tool in tools.tools):
                raise RuntimeError("The MCP server did not register count_words")

            result = await session.call_tool(
                "count_words",
                arguments={"text": SAMPLE_TEXT},
            )
            if result.isError:
                raise RuntimeError(f"MCP tool call failed: {result.content}")

            print(f"count_words({SAMPLE_TEXT!r}) -> {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
