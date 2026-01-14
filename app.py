from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

#1_Suma de digítos
def digitsSum(inputInt: int) -> int:
    suma = 0
    for num in str(abs(inputInt)):
        suma += int(num)
    return suma
    
#2_Palíndromo
def isPanlindrome(inputStr: str) -> bool:
    return inputStr == inputStr[::-1]

#3_Ordenamiento
def integerSort(inputArray):
    arr = inputArray.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# ----- RUTAS -------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/suma", methods=["GET", "POST"])
def suma():
    cantidad = None
    result = None
    proceso = None

    if request.method == "POST":
        cantidad = int(request.form["inputInt"])

        digitos = [int(d) for d in str(abs(cantidad))]

        proceso = " + ".join(map(str, digitos))

        result = sum(digitos)

    return render_template(
        "suma.html",
        cantidad=cantidad,
        proceso=proceso,
        result=result
    )

@app.route("/palindromo", methods=["GET", "POST"])
def palindromo():
    palabra = None
    result = None

    if request.method == "POST":
        palabra = request.form["inputStr"]
        result = isPanlindrome(palabra)

    return render_template(
        "palindromo.html",
        palabra=palabra,
        result=result
    )

@app.route("/ordenamiento", methods=["GET", "POST"])
def ordenamiento():
    original = None
    result = None

    if request.method == "POST":
        texto = request.form["inputArray"]
        original = list(map(int, texto.split(",")))
        result = integerSort(original)

    return render_template(
        "ordenamiento.html",
        original=original,
        result=result
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/descargar")
def descargar_zip():
    return send_from_directory(
        directory="static",
        path="Ejercicios_py.zip",
        as_attachment=True
    )

@app.route("/descargar-digits-sum")
def descargar_digits_sum():
    return send_from_directory(
        directory="Ejercicios_py",
        path="1_digits_sum.py",
        as_attachment=True
    )

@app.route("/descargar-palindromo")
def descargar_palindromo():
    return send_from_directory(
        directory="Ejercicios_py",
        path="2_palindromos.py",
        as_attachment=True
    )

@app.route("/descargar-ordenamiento")
def descargar_ordenamiento():
    return send_from_directory(
        directory="Ejercicios_py",
        path="3_ordenamiento.py",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)