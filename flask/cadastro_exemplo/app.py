from flask import Flask, render_template, redirect, request, json, flash, url_for
import pyodbc
from flask_login import LoginManager, UserMixin, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

app = Flask(__name__)
app.secret_key = 'senha_secreta'



app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?odbc_connect=' + \
    'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' + \
    f'DBQ=db.accdb;'

login_manager = LoginManager()
login_manager.init_app(app=app)
db = SQLAlchemy(app=app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    racf = Column(String(100), nullable=False)
    senha = Column(String(100), nullable=False)

def tabela_existe(connection, tabela):
    cursor = connection.cursor()

    # Monta a consulta SQL para verificar a existência da tabela
    query = f"SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{tabela}'"

    # Executa a consulta SQL
    cursor.execute(query)

    # Verifica se a tabela existe
    if cursor.fetchone():
        return True
    else:
        return False

def get_conexao():
    try:
        conn_str = (
            'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            f'DBQ=db.accdb;'
        )

        # Passo 2: Estabeleça a conexão com o banco de dados
        connection = pyodbc.connect(conn_str)
        
    except Exception as e:
        raise ConnectionError('Erro ao tentar conectar ao banco de dados')
    return connection


@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect(url_for('login'))


@app.route('/')
@login_required
def home():
    return render_template('home.html')


@app.route('/cadastrar', methods=['POST', 'GET'])
def enviar():
    
    """ 
    Pegando os dados enviados via post
    """
    
    emissor = request.form.get('emissor')
    ticker = request.form.get('ticker')
    cnpj = request.form.get('cnpj')
    tipo_ativo = request.form.get('tipo_ativo')
    limites = request.form.get('lista_limites')
    lista_limites: list = json.loads(limites)
    
    data = [{
        "emissor": emissor,
        "ticker": ticker,
        "cnpj": cnpj,
        "tipo_ativo": tipo_ativo,
        }]
    
    # if not pessoas_dict:
    #     flash(message='Ocorreu um erro ao realizar o processamento!')
    #     return redirect(url_for('home'))
    # else: 
    #     flash(message='operaçao realizada com sucesso')
    #     return redirect(url_for('home'))
    

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logar', methods=['POST'])
def logar():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    
    
    
