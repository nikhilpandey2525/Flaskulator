from flask import Flask, render_template, request ,jsonify
from Maths.mathematics import add, sub, mul, div, power, sqrt, cos, sin, tan, log, pi, e
app = Flask("Mathematics Problem Solver")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/sum")
def addition():
    """
    This endpoint will return the sum of two numbers given as query parameters.
    
    Example: /sum?num1=1&num2=2
    """
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    result = add(num1, num2)
    return str(result)

@app.route("/sub")
def subtraction():
    """
    This endpoint will return the difference of two numbers given as query parameters.
    
    Example: /sub?num1=5&num2=3
    """

    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    result = sub(num1, num2)
    return str(result)

@app.route("/mul")
def multiplication():
    """
    This endpoint will return the product of two numbers given as query parameters.
    
    Example: /mul?num1=2&num2=3
    """
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    result = mul(num1, num2)
    return str(result)

@app.route("/div")
def division():
    """
    This endpoint will return the result of dividing two numbers given as query parameters.
    
    Example: /div?num1=4&num2=2
    """
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    result =div(num1, num2)
    return str(result)

@app.route("/power")
def exponent():
    """
    This endpoint will return the result of raising a base to an exponent given as query parameters.
    
    Example: /power?base=2&exp=3
    """
    base = float(request.args.get("base"))
    exp = float(request.args.get("exp"))
    result = power(base, exp)
    return str(result)

@app.route("/sqrt")
def square_root():
    """
    This endpoint will return the square root of a given number given as a query parameter.
    
    Example: /sqrt?num=4
    """
    num = float(request.args.get("num"))
    result =sqrt(num)
    return str(result)

@app.route("/sin")
def sine():
    """
    This endpoint will return the sine of a given angle given as a query parameter.
    
    Example: /sin?angle=45
    """
    angle = float(request.args.get("angle"))
    result = sin(angle)
    return str(result)

@app.route("/cos")
def cosine():
    """
    This endpoint will return the cosine of a given angle provided as a query parameter.

    Example: /cos?angle=45
    """

    angle = float(request.args.get("angle"))
    result = cos(angle)
    return str(result)

@app.route("/tan")
def tangent():
    """
    This endpoint will return the tangent of a given angle provided as a query parameter.

    Example: /tan?angle=45
    """

    angle = float(request.args.get("angle"))
    result = tan(angle)
    return str(result)

@app.route("/log")
def logarithm():
    """
    This endpoint will return the natural logarithm of a given number provided as a query parameter.

    Example: /log?num=5
    """
    num = float(request.args.get("num"))
    result = log(num)
    return str(result)

@app.route("/pi")
def get_pi():
    return str(pi())

@app.route("/e")
def get_e():
    """
    This endpoint will return the value of the mathematical constant e.

    Example: /e
    """

    return str(e())

if __name__ == "__main__":
    app.run(debug=True)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
