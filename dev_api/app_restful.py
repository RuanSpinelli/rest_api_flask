#importando coisas para fazer a api
from flask import Flask
from flask_restful import Resource, Api

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


class Desenvolvedor(Resource):
    #metodo get do "endpoint" desenvolvedor
    def get(self,id):
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
    
    def put(self):
        pass
    
    def delete(self):
        pass

#rota para acessar a classe "Desenvolvedor"
api.add_resource(Desenvolvedor, "/dev/<int:id>")


#pra rodar a aplicação
if __name__ == "__main__":
    app.run(debug=True)