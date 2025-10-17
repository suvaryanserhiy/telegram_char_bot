XP_BASE = 10  # Base XP multiplier

class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.exp = 0
        self.level = 1

    def exp_handler(self, amount: int):
        """Add (or subtract) XP and update level accordingly."""
        self.exp += amount

        # Handle XP loss and possible level down
        while self.exp < 0 and self.level > 1:
            # Drop one level
            self.level -= 1
            # Add XP equivalent to how much it took to reach the next level
            self.exp += self.level * XP_BASE
            return "level_down"

        # Clamp XP to 0 if below level 1
        if self.level == 1 and self.exp < 0:
            self.exp = 0
            return "none"

        # Handle XP gain and possible level up
        leveled_up = False
        while self.exp >= self.level * XP_BASE:
            self.exp -= self.level * XP_BASEc
            self.level += 1
            leveled_up = True

        return "level_up" if leveled_up else "none"
