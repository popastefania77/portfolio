#!/bin/sh
echo "Activare venv:"
#source .vanv/bin/activate
. .venv/bin/activate
echo "Configurare variabila mediu FLASK_APP"
export FLASK_APP=aplicatie_flask
echo "Start server:"
exec flask run -h 0.0.0.0 -p 5011 --reload
