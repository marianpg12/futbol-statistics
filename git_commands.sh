#!/bin/bash

echo "create a new repository on the command line"
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
# Genera una clave SSH (si no tienes una)
ssh-keygen -t ed25519 -C "marianogaleano@hotmail.com.ar"

# Agrega tu clave SSH al agente SSH
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Agrega tu clave SSH a GitHub
# Copia tu clave SSH al portapapeles
cat ~/.ssh/id_ed25519.pub
sleep 0.8
# Ve a GitHub y agrega la clave SSH en Settings > SSH and GPG keys

# Empuja tu código al repositorio remoto
#git push -u origin main


