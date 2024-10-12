from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        "nome": "Rafael",
        "habilidades": ["python", "flask"]
     },
     {
        "nome": "Daniel",
        "habilidades": ["C#", "SQLSERVER"]
     }

]


@app.route('/dev/<int:id>/', methods=["GET","PUT"])
def desenvolvedor(id):

    if request.method == "GET":
        desenvolvedor = desenvolvedores[id]
        return jsonify(desenvolvedor)
    elif request.method == "PUT":
        
        dados = json.loads(request.data)
        desenvolvedores[id] = dados


if __name__ == "__main__":
    app.run(debug=True)