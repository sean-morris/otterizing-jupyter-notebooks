# Use Ubuntu latest as the base image
FROM ubuntu:latest

# Set non-interactive mode for apt to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

# Set bash as the default shell for all commands
SHELL ["/bin/bash", "-c"]

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    wget \
    gnupg \
    ca-certificates \
    unzip \
    fonts-liberation \
    libatk-bridge2.0-0 \
    libxcomposite1 \
    libxrandr2 \
    libxdamage1 \
    libxkbcommon-x11-0 \
    libgtk-3-0 \
    libgbm-dev \
    libnss3 \
    libnspr4 \
    python3.12-venv \
    xdg-utils \
    zstd \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p ~/.cache/pip && chmod -R 777 ~/.cache/pip

# Install Node.js (required for Playwright)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# Install Playwright and browsers
RUN npm install -g playwright \
    && npx playwright install chromium --with-deps

# Set the working directory to /app
WORKDIR /


