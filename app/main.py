import bottle
import os
import random


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
        'taunt': '--- Tibor > Thor ---',
        'head_url': 'https://media.licdn.com/mpr/mpr/shrinknp_200_200/AAEAAQAAAAAAAAdMAAAAJDBlMDJjMjI2LTgyMWItNDc5My1iM2Q4LWQ1NDg2MWQ5YTIwNg.jpg',
        'name': 'TiborManRooij'
    }


@bottle.post('/move')
def move():
  
    data = bottle.request.json
    health = data['you']['health']
    
    # TODO: Do things with data
    
    directions = ['up', 'down', 'left', 'right']
    
#    # if (health > 30)
#     #    if (count == 0):
#             direction = 'up'
#             count = 1
#         elif (count == 1):
#             direction = 'right'
#             count = 2
#         elif (count == 2):
#             direction = 'down'
#             count = 3
#         elif (count == 3):
#             direction = 'left'
#             count = 0 
            
    closestx=0
    closesty=0
    headx = data['you']['body']['data'][0]['x']
    heady = data['you']['body']['data'][0]['y']
    body1x = data['you']['body']['data'][1]['x']
    body1y = data['you']['body']['data'][1]['y']
    direction = random.choice(directions)
#     for i in data['food']['data']:
        
#         closestDistance = (((closestx-headx)**2)+((closesty-heady)**2))**0.5
#         foodx= i['x']
#         foody= i['y']
#         distance=(((foodx-headx)**2)+((foody-heady)**2))**0.5
#         if distance<closestDistance:
#             closestx = foodx
#             closesty = foody        
#     if headx!=foodx:       
#         if closestx<headx:
#             direction = 'left'
#         elif closestx>headx:
#             direction = 'right'
#     else:
#         if closesty<heady:
#             direction = 'down'
#         elif closesty>heady:
#             direction = 'up'
    if (headx-body1x) == 0:
        if (heady-body1y)>0:
            if direction == 'up':
                direction = 'right'
        else:
            if direction == 'down':
                direction = 'right'
    if (heady-body1y) == 0:
        if (headx-body1x)>0:
            if direction == 'left':
                direction = 'up'
        else:
            if direction == 'right':
                direction = 'up'
                
    if (headx==0) or (headx == (data['width']-1)):
        direction = 'down'
    if (heady==0) or (heady == (data['height']-1)):
        direction = 'left'
    if (headx==0) and (heady==0):
        if (headx-body1x)==0:
            direction = 'right'
        else:
            direction = 'down'
    if (headx==0) and (heady==data['height']-1):
        if (headx-body1x)==0:
            direction = 'right'
        else:
            direction = 'up'
    if (headx==data['width']-1) and (heady==data['height']-1):
        if (headx-body1x)==0:
            direction = 'left'
        else:
            direction = 'up'
    if (headx==data['width']-1) and (heady==0):
        if (headx-body1x)==0:
            direction = 'left'
        else:
            direction = 'down'
    
    if (headx-body1x) == 0:
        if (heady-body1y)>0:
            if direction == 'up':
                direction = 'right'
        else:
            if direction == 'down':
                direction = 'right'
    if (heady-body1y) == 0:
        if (headx-body1x)>0:
            if direction == 'left':
                direction = 'up'
        else:
            if direction == 'right':
                direction = 'up'
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
