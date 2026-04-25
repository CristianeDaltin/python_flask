# Arquivo principal da aplicação Flask

# Importa a classe Flask do pacote Flask
from flask import Flask

# Criar a instância da aplicação
# __name__ diz ao Flask onde esta a raiz do projeto
app = Flask(__name__)

# Chave secreta - usada para proteger sessões
# e  formulários CSRF
app.config['SECRET_KEY'] = 'trocar_senha'

# Rota principal 
# http://localhost/:5000 , retorna Olá
@app.route('/')
def index(): 
    return 'Olá, Flask funcionangido'
    
# Debug
if __name__ =='__main__':
    app.run(debug=True)



