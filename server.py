import asyncio
import logging
import os

from fastmcp import FastMCP

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

mcp = FastMCP("Math MCP Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Use this to add two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of the two numbers.
    """
    logger.info(f">>> Tool: 'add' called with numbers '{a}' and '{b}'")
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Use this to subtract two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The difference of the two numbers.
    """
    logger.info(f">>> Tool: 'subtract' called with numbers '{a}' and '{b}'")
    return a - b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Use this to multiply two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The multiplication of the two numbers.
    """
    logger.info(f">>> Tool: 'multiply' called with numbers '{a}' and '{b}'")
    return a * b


@mcp.tool()
def divide(a: int, b: int) -> int:
    """Use this to divide two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The division of the two numbers.
    """
    logger.info(f">>> Tool: 'divide' called with numbers '{a}' and '{b}'")
    return a / b


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
