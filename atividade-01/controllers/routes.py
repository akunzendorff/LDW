from flask import render_template, request, redirect, url_for

def init_app(app):
    pokemon_favorites = ['Pikachu', 'Charizard', 'Blastoise', 'Venusaur']
    
    pokemon_database = [
        {'nome': 'Pikachu', 'tipo': 'Elétrico', 'nivel': 25, 'hp': 100, 'regiao': 'Kanto'},
        {'nome': 'Charizard', 'tipo': 'Fogo/Voador', 'nivel': 36, 'hp': 150, 'regiao': 'Kanto'},
        {'nome': 'Blastoise', 'tipo': 'Água', 'nivel': 36, 'hp': 140, 'regiao': 'Kanto'}
    ]
    
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/favoritos', methods=['GET', 'POST'])
    def favoritos():
        if request.method == 'POST':
            if request.form.get('pokemon_name'):
                new_pokemon = request.form.get('pokemon_name')
                if new_pokemon not in pokemon_favorites:
                    pokemon_favorites.append(new_pokemon)
                return redirect(url_for('favoritos'))

        return render_template('favoritos.html', pokemon_favorites=pokemon_favorites)

    @app.route('/pokedex', methods=['GET', 'POST'])
    def pokedex():
        if request.method == 'POST':
            if (request.form.get('nome') and 
                request.form.get('tipo') and 
                request.form.get('nivel') and 
                request.form.get('hp') and 
                request.form.get('regiao')):
                
                new_pokemon = {
                    'nome': request.form.get('nome'),
                    'tipo': request.form.get('tipo'),
                    'nivel': int(request.form.get('nivel')),
                    'hp': int(request.form.get('hp')),
                    'regiao': request.form.get('regiao')
                }
                pokemon_database.append(new_pokemon)
                return redirect(url_for('pokedex'))

        return render_template('pokedex.html', pokemon_database=pokemon_database)

    @app.route('/remover_favorito/<pokemon_name>')
    def remover_favorito(pokemon_name):
        if pokemon_name in pokemon_favorites:
            pokemon_favorites.remove(pokemon_name)
        return redirect(url_for('favoritos'))

    @app.route('/remover_pokemon/<int:index>')
    def remover_pokemon(index):
        if 0 <= index < len(pokemon_database):
            pokemon_database.pop(index)
        return redirect(url_for('pokedex'))