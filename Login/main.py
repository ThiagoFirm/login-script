from flask import Flask, render_template, request, redirect, flash
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key' 

logado = False

@app.route('/')
def home():
    global logado
    logado = False 
    return render_template('login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    
    global logado
    if logado == True:
        return render_template('usuario.html')
    if logado == False:
        redirect('/')
    
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    
    with open ('usuarios.json') as UsuariosTemp:
        usuarios = json.load(UsuariosTemp)
        cont = 0    
        for usuario in usuarios:
            cont += 1
            if usuario['nome'] == nome and usuario['senha'] == senha:
                return render_template('usuario.html')

            if cont >= len(usuarios):
                flash('USUÁRIO INVÁLIDO')
                return redirect('/')

@app.route('/register', methods = ['POST', 'GET'])
def register():
    global logado
    if logado == True:
        return render_template('usuario.html')
    if logado == False:
        redirect('/')
    user = []
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    user = [
        {
            "nome": nome,
            "senha": senha
        }
    ]
    
    with open ('usuarios.json') as UsuariosTemp:
        usuarios = json.load(UsuariosTemp)

        
        
        usuarioNovo = usuarios + user
    
    with open ('usuarios.json', 'w') as gravarTemp:
        json.dump(usuarioNovo, gravarTemp, indent = 4)
        
        return render_template('register.html') 





if __name__  == "__main__":
    app.run(debug = True)