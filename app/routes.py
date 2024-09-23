from flask import Blueprint, render_template
from .utils import obtener_datos, crear_graficos

main = Blueprint('main', __name__)

@main.route('/')
def index():
    df = obtener_datos()
    crear_graficos(df)
    tabla_html = df.to_html(classes='table table-bordered table-striped table-hover', index=False)
    return render_template('index.html', tabla=tabla_html)
