# matcher.py

from collections import defaultdict

class Matcher:
    def __init__(self):
        self.waitlists = defaultdict(list)
        self.matches = []

    def add_user(self, user):
        product = user.product
        queue = self.waitlists[product]

        if queue:
            match_user = queue.pop(0)
            self.matches.append((match_user, user, product))
            return {
                "match_found": True,
                "user1": match_user.name,
                "user2": user.name,
                "product": product

            }
        else:
            queue.append(user)
            return {"match_found": False}
        
    def get_matches(self):
        return [
        {
            "user1": u1.name,
            "user2": u2.name,
            "product": product
        } for u1, u2, product in self.matches
    ]
