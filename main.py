from ursina import *
from fish import fish
from rod import rod
from ui import update_score

app= Ursina()

rod = Rod(positition(0, -2, 0))
fish = Fish(position=(random.uniform(-3, 3), -2, 0))
score=0
score_text = update_score(score)

def update():
    global score

rod.move()

if rod.entity.intersects(fish.entity).hit:
    fish.respawn()
    score += 10
    update_score(sore, score_text)

    app.run
    