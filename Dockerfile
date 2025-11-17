FROM ghcr.io/astral-sh/uv:python3.13-alpine

#LABEL org.opencontainers.image.source="https://github.com/cssnr/create-files-action"
#LABEL org.opencontainers.image.description="Create Files Action"
#LABEL org.opencontainers.image.authors="smashedr"

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy
# Ensure installed tools can be executed out of the box
ENV UV_TOOL_BIN_DIR=/usr/local/bin
# Add .venv to the front of the PATH
ENV PATH="/.venv/bin:$PATH"

COPY pyproject.toml uv.lock /
RUN uv sync --locked --no-dev

COPY src /src
ENTRYPOINT ["python", "/src/main.py"]
