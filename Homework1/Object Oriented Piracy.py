PERSON_DRAFT = 1.5
SHIP_DRAFT = 20


class Ship:
    """
    Link to task: https://www.codewars.com/kata/54fe05c4762e2e3047000add
    """
    def __init__(self, draft: int, crew: int):
        self.draft = draft
        self.crew = crew
        
    def is_worth_it(self):
        min_ship_draft = SHIP_DRAFT + self.crew * PERSON_DRAFT
        if self.draft > min_ship_draft:
            return True

        return False 
        
