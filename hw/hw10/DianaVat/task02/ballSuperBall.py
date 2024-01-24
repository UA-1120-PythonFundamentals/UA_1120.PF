class Ball(object):
    # your code goes here
    def init (self,typeBall="regular"):
        self.ball_type = typeBall
ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"