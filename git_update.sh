#!/bin/bash

# Asegúrate de estar en la rama principal
git checkout main

# Actualiza el repositorio local con los cambios del repositorio remoto
git pull origin main

# Verifica el estado de tus cambios
git status

# Agrega todos los archivos modificados al área de preparación
git add .

# Realiza un commit con un mensaje descriptivo
git commit -m "Actualizar aplicación con nuevas modificaciones"

# Empuja tus cambios al repositorio remoto en GitHub
git push origin main

# Mensaje de confirmación
echo "¡Actualización exitosa! Los cambios han sido subidos a GitHub."

