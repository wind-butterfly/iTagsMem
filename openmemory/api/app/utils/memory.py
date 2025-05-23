import os

from mem0 import Memory


memory_client = None


def get_memory_client(custom_instructions: str = None):
    """
    Get or initialize the Mem0 client.

    Args:
        custom_instructions: Optional instructions for the memory project.

    Returns:
        Initialized Mem0 client instance.

    Raises:
        Exception: If required configuration is not set.
    """
    global memory_client

    if memory_client is not None:
        return memory_client

    try:
        config = {
            "vector_store": {
                "provider": "qdrant",
                "config": {
                    "collection_name": "openmemory",
                    "host": "mem0_store",
                    "port": 6333,
                    "embedding_model_dims": int(os.getenv("EMBEDDING_DIMS", "768"))
                }
            },
            "llm": {
                "provider": "ollama",
                "config": {
                    "model": "llama2",
                    "ollama_base_url": os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434"),
                    "temperature": 0.7,
                    "max_tokens": 2000
                }
            },
            "embedder": {
                "provider": "ollama",
                "config": {
                    "model": os.getenv("EMBEDDING_MODEL", "mxbai-embed-large"),
                    "ollama_base_url": os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434"),
                    "embedding_dims": int(os.getenv("EMBEDDING_DIMS", "768"))
                }
            }
        }

        memory_client = Memory.from_config(config_dict=config)
    except Exception as e:
        raise Exception(f"Exception occurred while initializing memory client: {str(e)}")

    # Update project with custom instructions if provided
    if custom_instructions:
        memory_client.update_project(custom_instructions=custom_instructions)

    return memory_client


def get_default_user_id():
    return "default_user"
