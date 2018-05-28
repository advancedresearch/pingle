

class GameResults:
    def __init__(self, *,
                 cumulative_reward,
                 cumulative_safety_reward,
                 ):
        self.cumulative_reward = cumulative_reward
        self.cumulative_safety_reward = cumulative_safety_reward
                 
    def __repr__(self):
        return '<rew=%.2f safe=%.2f>' % (
            self.cumulative_reward,
            self.cumulative_safety_reward)
    
