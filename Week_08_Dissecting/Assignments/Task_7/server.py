from mcp.server.fastmcp import FastMCP


mcp = FastMCP("task7-local-tool")


@mcp.tool()
def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in text."""
    return len(text.split())


if __name__ == "__main__":
    mcp.run(transport="stdio")
