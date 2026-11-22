from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route('/')
def inicio():
    return render_template('index.html')


# Ejercicio 1: Formulario de notas
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None

    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        if (10 <= nota1 <= 70 and
            10 <= nota2 <= 70 and
            10 <= nota3 <= 70 and
            0 <= asistencia <= 100):

            promedio = (nota1 + nota2 + nota3) / 3

            if promedio >= 40 and asistencia >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"

        else:
            estado = "ERROR: Las notas o la asistencia están fuera del rango permitido."
    return render_template(
        'ejercicio1.html',
        promedio=promedio,
        estado=estado
    )


# Ejercicio 2: Formulario de nombres
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_largo = None
    cantidad = None
    error = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()

        nombres = [nombre1, nombre2, nombre3]

        if not all(nombres):
            error = "Debes ingresar los tres nombres."
        elif len(set(nombre.lower() for nombre in nombres)) != 3:
            error = "Los nombres deben ser diferentes."
        else:
            nombre_largo = max(nombres, key=len)
            cantidad = len(nombre_largo)

    return render_template(
        'ejercicio2.html',
        nombre_largo=nombre_largo,
        cantidad=cantidad,
        error=error
    )


# Ejecutar aplicación
if __name__ == '__main__':
    app.run(debug=True)