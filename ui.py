from ursina import *
def update(score, score_text=None):
    if not score_text
return Text(text=f"score: {score}", position=(-0.7, 0.45))
else:
    score_text.text = f"score: {score}"