from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/notasyasistencia', methods=['GET', 'POST'])
def notasYAsistencia():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        promedio = round((nota1 + nota2 + nota3)/3, 1)
        status = ""
        if promedio >= 40.0 and asistencia >= 75:
            status = "APROBADO"
        else:
            status = "REPROBADO"
        return render_template('notasyasistencia.html', promedio=promedio, status=status)
    return render_template('notasyasistencia.html')


@app.route('/mayornombre', methods=['GET', 'POST'])
def mayorNombre():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        mayor = ""
        if len(nombre1) >= len(nombre2) and len(nombre1) >= len(nombre3):
            mayor = nombre1
        elif len(nombre2) >= len(nombre3):
            mayor = nombre2
        else:
            mayor = nombre3

        return render_template('mayornombre.html', mayorNombre=mayor, cantLetras=len(mayor))
    return render_template('mayornombre.html')


if __name__ == '__main__':
    app.run(debug=True)