#!/bin/bash

# activar entorno
echo "Creando el entorno..."
sleep 1
python3 -m venv myenv
echo "Activando..."
sleep 1
source myenv/bin/activate

# luego correr la app
echo "Ejecutando la App"
sleep 1
streamlit run new_app.py


