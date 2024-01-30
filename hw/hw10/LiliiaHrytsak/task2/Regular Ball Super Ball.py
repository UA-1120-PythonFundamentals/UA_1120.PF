class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


a = Ball()
print(a.ball_type)
b = Ball('super')
print(b.ball_type)
