from flask import Flask, render_template, request, redirect, url_for

# Dados simulados (substituir futuramente pela ligação à BD)
lista_utilizadores = [
    {"id": 1, "nome": "Ana Silva", "email": "ana@email.com", "password": "123"},
    {"id": 2, "nome": "João Santos", "email": "joao@email.com", "password": "456"}
]

app = Flask(__name__)

@app.get("/utilizadores")
def listar_utilizadores():
    # Devolve a lista sem expor as palavras-passe
    return [
        {"id": u["id"], "nome": u["nome"], "email": u["email"]}
        for u in lista_utilizadores
    ]

@app.get('/')
def pagina_inicial():
    return render_template('index.html', utilizadores=lista_utilizadores)

@app.post('/login')
def processar_login():
    email = request.form.get('email')
    password = request.form.get('password')

    utilizador = next(
        (u for u in lista_utilizadores if u["email"] == email and u["password"] == password),
        None
    )

    if utilizador:
        return redirect(url_for('pagina_inicial'))
    
    return "Credenciais inválidas.", 401


@app.post('/registo')
def processar_registo():
    nome = request.form.get('nome')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if password != confirm_password:
        return "As palavras-passe não coincidem.", 400

    # Verifica se o email já existe
    if any(u["email"] == email for u in lista_utilizadores):
        return "Este email já está registado.", 400

    # Adiciona à lista em memória (futuramente será um INSERT INTO na BD)
    novo_utilizador = {
        "id": len(lista_utilizadores) + 1,
        "nome": nome,
        "email": email,
        "password": password
    }
    lista_utilizadores.append(novo_utilizador)

    return redirect(url_for('pagina_inicial'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')