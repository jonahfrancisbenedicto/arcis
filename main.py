class Projectile:

    # Constructor Method
    def __init__(
        self, 
        position: tuple[float, float, float], 
        velocity: tuple[float, float, float], 
        acceleration: tuple[float, float, float],
        mass: float
    ) -> None:
        self.set_position(position)
        self.set_velocity(velocity)
        self.set_acceleration(acceleration)
        self.set_mass(mass)
    
    # Methods
    def step(self, delta_time: float) -> None:
        pass

    # Setter and Getter Methods
    def get_position(self) -> tuple[float, float, float]:
        return self._position

    def set_position(self, position: tuple[float, float, float]) -> None:
        self._position = position
    
    def get_velocity(self) -> tuple[float, float, float]:
        return self._velocity

    def set_velocity(self, velocity: tuple[float, float, float]) -> None:
        self._velocity = velocity

    def get_acceleration(self) -> tuple[float, float, float]:
        return self._acceleration

    def set_acceleration(self, acceleration: tuple[float, float, float]) -> None:
        self._acceleration = acceleration

    def get_mass(self) -> float:
        return self._mass

    def set_mass(self, mass: float) -> None:
        self._mass = mass
