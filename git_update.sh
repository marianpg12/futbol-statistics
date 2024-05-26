#!/bin/bash

git pull origin main --no-rebase
git status
git add .
git commit -m "Actualizando..."
git push origin main

# Mensaje de confirmación
echo "¡Actualización exitosa! Los cambios han sido subidos a GitHub."

