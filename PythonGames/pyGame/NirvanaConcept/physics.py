import pygame

class PhysicsEngine:
    @staticmethod
    def apply_gravity(velocity_y: float, gravity: float, dt: float) -> float:
        """Applies downward acceleration scaled by delta-time."""
        return velocity_y + (gravity * dt)

    @staticmethod
    def move_and_collide(rect: pygame.Rect, velocity: list[float], platforms: list[pygame.Rect], dt: float) -> dict:
        """
        Updates position using delta-time and resolves AABB collisions.
        Returns ground state flags.
        """
        on_ground = False

        # --- Horizontal Movement ---
        rect.x += int(velocity[0] * dt)
        for platform in platforms:
            if rect.colliderect(platform):
                if velocity[0] > 0:  # Moving right
                    rect.right = platform.left
                elif velocity[0] < 0:  # Moving left
                    rect.left = platform.right

        # --- Vertical Movement ---
        rect.y += int(velocity[1] * dt)
        for platform in platforms:
            if rect.colliderect(platform):
                if velocity[1] > 0:  # Falling down
                    rect.bottom = platform.top
                    velocity[1] = 0
                    on_ground = True
                elif velocity[1] < 0:  # Jumping up
                    rect.top = platform.bottom
                    velocity[1] = 0

        # --- Continuous Ground Check (The Fix) ---
        # Even if velocity is 0, check if we are resting right on top of any platform
        if not on_ground:
            # Shift the rect down by 1 pixel temporarily to check for ground contact
            rect.y += 1
            for platform in platforms:
                if rect.colliderect(platform) and velocity[1] >= 0:
                    on_ground = True
                    break
            rect.y -= 1  # Revert the temporary shift

        return {"on_ground": on_ground}