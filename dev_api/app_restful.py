#importando coisas para fazer a api
from flask import Flask, request
from flask_restful import Resource, Api
import json



#criando uma instancia para o app
app = Flask(__name__)
api = Api(app)


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
class Desenvolvedor(Resource):
    #metodo get do "endpoint" desenvolvedor
    def get(self, id):
        try:
            #tenta pegar um desenvolvedor com base no id dele no sistema
            response = desenvolvedores[id]
        
        #caso não encontre-o
        except IndexError:
            mensagem = f"Desenvolvedor de ID: {id} não encontrado"        
            response = {"Status": "FALHA", "Mensagem": mensagem}

        #caso ocorra algum problema inesperado 
        except Exception:
            mensagem = "Erro desconhecido. Procure o administrador da API."
            response = {"Status": "FALHA", "Mensagem": mensagem}
        
        #retornar a resposta final
        return response 
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': "sucesso", "mensagem": "registro excluído"}
        
#rota para acessar a classe "Desenvolvedor"
api.add_resource(Desenvolvedor, "/dev/<int:id>")

    
#lista todos os desenvolvedores e inclui um novo desenvolvedor
class ListarDesenvolvedores(Resource):
    
    #coloca um desenvolvedor novo na lista
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        desenvolvedores.append(dados)
        dados['id'] = posicao

        return desenvolvedores[posicao]
    
    #mostra uma lista de desenvolvedores na tela
    def get(self):
        
        return desenvolvedores


#rota para acessar a classe "ListarDesenvolvedores"
api.add_resource(ListarDesenvolvedores, "/dev/")



#pra rodar a aplicação
if __name__ == "__main__":
    app.run(debug=True)