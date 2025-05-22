# OpenMemory

This project is containerized using Docker and Docker Compose. All services run in containers for consistency and ease of deployment.

## Prerequisites

- Docker
- Docker Compose
- Ollama (for local embeddings)

## Building and Running

1. **Build the containers:**

   ```sh
   docker-compose build --parallel
   ```

2. **Pull the Ollama model:**

   ```sh
   ollama pull mxbai-embed-large
   ```

3. **Run the services:**

   ```sh
   docker-compose up
   ```

   This will start the following services:
   - `mem0_store`: Qdrant vector store
   - `openmemory-mcp`: MCP server (using Ollama for embeddings)
   - `openmemory-ui`: Next.js UI

4. **Access the UI:**

   Open your browser and navigate to `http://localhost:3000`.

## Configuration

- **Environment Variables:**

   - `NEXT_PUBLIC_API_URL`: URL for the MCP server (default: `http://localhost:8765`).
   - `USER`: User ID for the MCP client.
   - `OLLAMA_BASE_URL`: URL for the Ollama server (default: `http://host.docker.internal:11434`).
   - `EMBEDDING_MODEL`: Ollama embedding model (default: `mxbai-embed-large`).
   - `EMBEDDING_DIMS`: Embedding dimensions (default: `768`).

   These can be set in a `.env` file or passed directly to Docker Compose.

## Development

- **API:**

   The API is built using FastAPI and runs in a container. The source code is mounted as a volume for live reloading.

- **UI:**

   The UI is built using Next.js and runs in a container. The source code is mounted as a volume for live reloading.

## Troubleshooting

- If you encounter issues with the `install-mcp` package, ensure you are using the correct Node.js image and that the package is properly installed.
- Check the Docker logs for any errors or warnings.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
