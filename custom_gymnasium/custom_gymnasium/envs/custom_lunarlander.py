import numpy as np
import gymnasium as gym
from typing import TYPE_CHECKING, Optional
from custom_gymnasium.utils.base_lander import BASE_LANDER

class CustomLunarLander_v1(BASE_LANDER):
    def __init__(
        self,
        render_mode: Optional[str] = None,
        continuous: bool = False,
        gravity: float = -10.0,
        enable_wind: bool = False,
        wind_power: float = 15.0,
        turbulence_power: float = 1.5,
        fuel: float = 100,):
        """
        task: Use super() function to excute 
        """
        # =====================type your code here=====================
        super().__init__(
            render_mode=render_mode,
            continuous=continuous,
            gravity=gravity,
            enable_wind=enable_wind,
            wind_power=wind_power,
            turbulence_power=turbulence_power,
            fuel=fuel,
        )
        self.__total_fuel = fuel
        # =============================================================

    def reset(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[dict] = None,):

        # =====================type your code here=====================
        self.__fuel = self.__total_fuel
        return super().reset(
                        seed=seed,
                        options=options)
        # =============================================================
        
    def step(self, action):

        # =====================type your code here=====================
        if self.__fuel <= 0:
            action = 0
        else:
            if action > 0:
                self.__fuel -= 1
        obs, reward, terminated, truncation, info = super().step(action=action)
        return obs, reward, terminated, truncation, info
        # =============================================================
