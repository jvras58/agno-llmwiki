"""
Main entry point for the modular Agno LLM Wiki system.
This orchestrates the microservices-like architecture.
"""

from chat import start_chat

if __name__ == "__main__":
    start_chat()