from flask import Flask, jsonify, request
import json

app = Flask(__name__)

#listinha com os desenvolvedores
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


def lista_desenvolvedores():

if __name__ == "__main__":
    app.run(debug=True)