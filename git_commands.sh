#!/bin/bash

echo "Initializing a new repository on the command line..."
sleep 1

# Inicializa un repositorio Git
git init

# Agrega todos los archivos al repositorio
git add .

# Haz un commit con un mensaje adecuado
git commit -m "Initial commit"
sleep 0.8

# Elimina el remoto origin si ya existe
git remote remove origin

# Agrega el remoto origin con la URL correcta (SSH en lugar de HTTPS)
git remote add origin git@github.com:marianpg12/futbol-statistics.git
sleep 0.8

# Verificar si la clave SSH ya existe
KEY_PATH="$HOME/.ssh/key"
if [ -f "$KEY_PATH" ]; then
    echo "SSH key already exists. Skipping key generation."
else
    # Genera una clave SSH (si no tienes una)
    ssh-keygen -t ed25519 -C "marianogaleano@hotmail.com.ar" -f "$KEY_PATH"
fi

# Agrega tu clave SSH al agente SSH
eval "$(ssh-agent -s)"
ssh-add "$KEY_PATH"

# Mostrar la clave SSH al usuario
echo "Copy the following SSH key and add it to GitHub (Settings > SSH and GPG keys):"
cat "$KEY_PATH.pub"
sleep 0.8

echo "Once you've added the SSH key to GitHub, press Enter to continue..."
read -p ""

# Empuja tu código al repositorio remoto
#git push -u origin main

