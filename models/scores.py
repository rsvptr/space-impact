# Filename: scores.py

# Function: Model file that contains functions used by the scoreboard.

# This include getting top 5 high scores (which are stored in an array), displaying the list and even appending the values for a particular gameplay.

class Scores:

    # Initializes empty matrix to store score list.
    
    def __init__(self):
        self.score_list = []

    # Used to get top 5 high scores.

    def get_top_5(self):
        return sorted(self.score_list, key=lambda item: item['score'], reverse=True)

    # Used to get complete list of high scores.

    def get_scores(self):
        return self.score_list

    # Appends values of level completed, kills made, score achieved for a particular gameplay into matrix.

    def append(self, status, level, score, kills):
        self.score_list.append({
            "status": status,
            "level": level,
            "score": score,
            "kills": kills,
        })


scores = Scores()
