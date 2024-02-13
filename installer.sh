#! /bin/bash

# Install ollama.
cd /tmp/
curl -fsSL https://ollama.com/install.sh | sh

# Serve the ollama app.
sudo systemctl enable ollama
sudo systemctl start ollama
 
# Download the LLaMa2 model.
ollama pull llama2:latest

# Download the CodeLLaMa model.
ollama pull codellama:latest

# Re-start the service. 
sudo systemctl restart ollama

# I'm not sure if this script works. :)