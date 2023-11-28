# -*- coding: utf-8 -*-
import os
import dotenv
from flask import Flask, render_template, url_for

from dotenv import load_dotenv
app = Flask(__name__)

env_path = "ma.env"

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path=env_path)

# Agora você pode acessar as variáveis de ambiente usando o módulo os
api_key = os.getenv('API_KEY')
apizuser = os.getenv('API_USER')
Vuser = os.getenv('USUARIO')
VSenha = os.getenv('SENHA')

@app.route('/')
def index():

    return render_template('LOGINFUNCIONARIO.html', api_key=api_key, apizuser=apizuser,logo_url=url_for('static', filename='Logos.png'))
@app.route('/Untitled-1.html', methods=['GET'])
def inicio():
    return render_template('Untitled-1.html', api_key=api_key, apizuser=apizuser, logo_url=url_for('static', filename='Logos.png'))
@app.route('/DadosValidade.html', methods=['GET'])
def Dados():
    return render_template('DadosValidade.html', api_key=api_key, apizuser=apizuser, logo_url=url_for('static', filename='Logos.png'))

@app.route('/CADASTROFUNCIONARIO.html', methods=['GET'])
def Cadastro():
    return render_template('CADASTROFUNCIONARIO.html', api_key=api_key, apizuser=apizuser, logo_url=url_for('static', filename='Logos.png'))
@app.route('/ADMINISTRAR.html', methods=['GET'])
def Adm():
    return render_template('ADMINISTRAR.html', api_key=api_key, apizuser=apizuser,Vuser=Vuser,VSenha=VSenha)

@app.route('/Qrcodegenerate.html', methods=['GET'])
def Adf():
    return render_template('Qrcodegenerate.html', api_key=api_key, apizuser=apizuser)


if __name__ == '__main__':
    # Executar o aplicativo em modo de depuração
    app.run(debug=True)

