from flask import Flask, render_template

lista_catalogo = [{"marca": "Nike", "modelo": "xpto", "tamanho": 42, "preco": 120, "quantidade": 5},
            {"marca": "Adidas", "modelo": "ABC", "tamanho": 41, "preco": 100, "quantidade": 4},
            {"marca": "Puma", "modelo": "XYZ", "tamanho": 43, "preco": 90, "quantidade": 3}]

app = Flask(__name__)

@app.get("/catalogo")
def listar_produtos():
    return lista_catalogo

@app.get('/')
def pagina_inicial():
    return render_template('index.html', catalogo=lista_catalogo)

if __name__ == '__main__':
    app.run(host='0.0.0.0')