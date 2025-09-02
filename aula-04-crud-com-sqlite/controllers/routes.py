from flask import render_template, request, redirect, url_for
import urllib #envia requisições a uma URL
import json #faz a conversão de json > dicionário


def init_app(app):
    # Lista em Python (array)
    players = ['Leminhos', 'Yasmine', 'Ana', 'Gustavo']
    
    gamelist = [{'Título': 'CS 1.6', 'Ano': 1996, 'Categoria': 'FPS Online'}]
    
    # Definindo a rota principal da aplicação '/'
    @app.route('/')
    def home():  # Função que será executada ao acessar a rota
        return render_template('index.html')

    @app.route('/games')
    def games():
        title = 'Tarisland'
        year = 2022
        category = 'MMORPG'
        # Dicionário em Python (objeto)
        console = {'nome': 'Playstation5', 'fabricante': 'Sony', 'ano': 2024}

        # Tratando uma requisição POST com request
        if request.method == 'POST':
            # Coletando o texto da input
            if request.form.get('player'):
                players.append(request.form.get('player'))
                return redirect(url_for('games'))

        return render_template('games.html',
                               title=title,
                               year=year,
                               category=category,
                               players=players,
                               console=console)

    @app.route('/newgame', methods=['GET', 'POST'])
    def newgame():

        # Tratando a requisição POST
        if request.method == 'POST':

            if request.form.get('title') and request.form.get('year') and request.form.get('category'):

                gamelist.append(
                    {'Título': request.form.get('title'),
                     'Ano': request.form.get('year'),
                     'Categoria': request.form.get('category')}
                )
                return redirect(url_for('newgame'))

        return render_template('newGame.html', gamelist=gamelist)
    
    
    @app.route('/apigames', methods=['GET', 'POST'])
    # Criando parâmetros para a rota
    @app.route('/apigames/<int:id>', methods=['GET', 'POST'])
    def apigames(id=None): # Parâmetro opicional
        url = 'https://www.freetogame.com/api/games'
        response = urllib.request.urlopen(url)
        data = response.read()
        # Pega informação, grava num dicionário que é a variável abaixo
        gamesList = json.loads(data)
        # Verificando se o parâmetro foi enviado
        if id:
            gameInfo = []
            for game in gamesList:
                if game['id'] == id:
                    gameInfo = game
                    break
            if gameInfo:
                return render_template('gameInfo.html', gameInfo=gameInfo)
            else:
                return f'Game com a ID {id} não foi encontrado.'
        else:            
            return render_template('apigames.html', gamesList=gamesList)
        
