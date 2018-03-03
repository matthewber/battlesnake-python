import bottle
import os
import random

count = 0

@bottle.route('/')
def static():
    return "the server is running"


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data.get('game_id')
    board_width = data.get('width')
    board_height = data.get('height')

    # TODO: Do things with data

    return {
        'color': '#00FF00',
        'taunt': ' Tibor > Thor',
        'head_url': 'https://media.licdn.com/mpr/mpr/shrinknp_200_200/AAEAAQAAAAAAAAdMAAAAJDBlMDJjMjI2LTgyMWItNDc5My1iM2Q4LWQ1NDg2MWQ5YTIwNg.jpg',
        'name': 'TiborManRooij'
    }


@bottle.post('/move')
def move():
    
    data = bottle.request.json
    
    if count == 0:
        direction = 'up'
        count = count+1
    elif count == 1:
        direction = 'right'
        count = count+1
    elif count == 2:
        direction = 'down'
        count = count+1
    elif count == 3:
        direction = 'left'
        count = 0 
    # TODO: Do things with data
    
    directions = ['up', 'down', 'left', 'right']

    print direction
    return {
        'move': direction,
        'taunt': 'Tibors on the dance floor'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug = True)
