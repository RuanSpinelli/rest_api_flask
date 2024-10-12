from flask import Flask, jsonify, request
import json

app = Flask(__name__)

#listinha com os desenvolvedores
desenvolvedores = [
    {
        "id": 0,
        "nome": "Rafael",
        "habilidades": ["python", "flask"]
     },
     {
        'id': 1,
        "nome": "Daniel",
        "habilidades": ["C#", "SQLSERVER"]
     }

]

#Devolve, altera e remove um desenvolvedor pelo ID
@app.route('/dev/<int:id>/', methods=["GET","PUT","DELETE"])
def desenvolvedor(id):

    if request.method == "GET":
        try:
            response = desenvolvedores[id]
        
        except IndexError:
            mensagem = f"Desenvolvedor de ID: {id} não encontrado"        
            response = {"Status": "FALHA", "Mensagem": mensagem}

        except Exception:
            mensagem = "Erro desconhecido. Procure o administrador da API."
            response = {"Status": "FALHA", "Mensagem": mensagem}
        
        return jsonify(response)    
    
    
    elif request.method == "PUT":
        
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    

    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({'status': "sucesso", "mensagem": "registro excluído"})

#lista todos os desenvolvedores e inclui um novo desenvolvedor
@app.route("/dev/", methods=["POST", "GET"])
def lista_desenvolvedores():
    if request.method =="POST":
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        desenvolvedores.append(dados)
        dados['id'] = posicao

        mensagem = "Desenvolvedor postado com sucesso!"  
        return jsonify(desenvolvedores[posicao])
    
    elif request.method == "GET":
        return jsonify(desenvolvedores)






if __name__ == "__main__":
    app.run(debug=True)