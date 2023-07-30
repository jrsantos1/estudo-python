import pandas as pd
from flask import Flask, render_template, redirect, request, json, flash, url_for
import pyodbc
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, create_engine
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'senha_secreta'

caminho_projeto = os.path.abspath(os.curdir)
caminho_db = os.path.join(caminho_projeto, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{caminho_db}'

login_manager = LoginManager()
login_manager.init_app(app=app)
db = SQLAlchemy(app=app)

def get_conexao():
    connection = sqlite3.connect(caminho_db)
    return connection
    #connection_string = f'DRIVER={{SQLite3 ODBC Driver}};DATABASE={caminho_db};'

    return pyodbc.connect(connection_string)
@login_manager.user_loader
def load_user(user_id):
    user = User(id=1, senha='123', racf='ribejho')
    return user

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    racf = Column(String(100), nullable=False)
    senha = Column(String(100), nullable=False)

    def __init__(self, id, racf, senha):
        self.id = id
        self.senha = senha
        self.racf = racf



@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect(url_for('login'))


@app.route('/')
@login_required
def home():
    return render_template('home.html', current_user=current_user)


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
    df_limites = pd.DataFrame(data=lista_limites)

    data = [{
        "emissor": emissor,
        "ticker": ticker,
        "cnpj": cnpj,
        "tipo_ativo": tipo_ativo,
       "valor_limite": r['valor_limite'],
       "prazo_limite": r['prazo_limite'],
       "tipo_limite": r['tipo_limite']
     }  for _, r in df_limites.iterrows()]

    df_cadastro = pd.DataFrame(data=data)

    try:
        with get_conexao() as con:
            df = pd.read_sql(sql='select * from tgemissores', con=con)
            state = 'insert into tgemissores (emissor, ticker, cnpj, tipo_ativo, valor_limite, prazo_limite, tipo_limite) values (?,?,?,?,?,?,?)'
            for _, r in df_cadastro.iterrows():
                parametros = [r['emissor'], r['ticker'], r['cnpj'], r['tipo_ativo'],
                              r['valor_limite'], r['prazo_limite'], r['tipo_limite'],]
            df_cadastro.to_sql('tgemissores', con=con, if_exists='append', index=False) #todo verificar depois, pois é mais eficiente
            df = pd.read_sql(sql='select * from tgemissores', con=con)
    except Exception as e:
        print(e)

    return redirect(url_for('home'))

@app.route('/cadastros')
def cadastros():
    with get_conexao() as con:
        df_cadastros = pd.read_sql(sql='select * from tgemissores', con=con)
    return render_template('cadastros.html', cadastros=df_cadastros.to_dict('records'))

@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logar', methods=['POST'])
def logar():

    racf = request.form.get('racf')
    senha = request.form.get('senha')

    if racf and senha:
        user = User.query.filter_by(racf=racf).first()
        login_user(user=user)
    else:
        return redirect(url_for('login'))
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    
    
    
