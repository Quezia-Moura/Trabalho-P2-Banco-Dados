from flask import Flask, render_template, url_for, request, redirect
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="aula_13_10"
)


db_cursor = connection.cursor()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/setor', methods=['POST'])
def adicionar_setor():
    if request.method == 'POST':
        setor_nome = request.form['setor_nome']
        query = 'INSERT INTO setor (nome) VALUES (%s)'
        db_cursor.execute(query, (setor_nome,))
        connection.commit()
    return redirect(url_for('home'))


@app.route('/funcionarios', methods=['POST'])
def adicionar_funcionarios():
    primeiro_nome = request.form['primeiro_nome']
    sobrenome = request.form['sobrenome']
    data_admissao = request.form['data_admissao']
    status_funcionario = request.form['status_funcionario']
    id_setor = request.form['id_setor']


    db_cursor.execute(
        'INSERT INTO funcionarios (primeiro_nome, sobrenome, data_admissao, status_funcionario, id_setor) VALUES (%s, %s, %s, %s, %s)',
        (primeiro_nome, sobrenome, data_admissao, status_funcionario, id_setor)
    )
    connection.commit()

    return f'Funcionário adicionado: {primeiro_nome} {sobrenome}, Data de Admissão: {data_admissao}, Status: {status_funcionario}, Setor: {id_setor}'


@app.route('/cargo', methods=['POST'])
def adicionar_cargo():
    if request.method == 'POST':
        nome_cargo = request.form['nome_cargo']
        query = 'INSERT INTO cargos (nome) VALUES (%s)'
        db_cursor.execute(query, (nome_cargo,))
        connection.commit()
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)
