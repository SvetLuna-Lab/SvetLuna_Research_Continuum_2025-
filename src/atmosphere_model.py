"""
Simple 1D atmospheric column model for the SvetLuna Hybrid
Atmospheric Installation.

Author: S. I. Romanova, 2025
"""

from dataclasses import dataclass
from typing import Tuple

import numpy as np


@dataclass
class AtmosphericProfile:
    """Container for a vertical atmospheric profile."""

    height: np.ndarray          # [m]
    temperature: np.ndarray     # [K]
    pressure: np.ndarray        # [Pa]
    energy: np.ndarray          # [arb. units]
    resonance_index: np.ndarray # [arb. units]


def standard_profile(
    z_max: float = 20_000.0,
    n_levels: int = 201,
    t_ground: float = 288.0,
    lapse_rate: float = -6.5e-3,
    p_ground: float = 101_325.0,
) -> AtmosphericProfile:
    """
    Build a very simple 'standard' atmosphere profile.

    Parameters
    ----------
    z_max : float
        Max height in meters.
    n_levels : int
        Number of vertical grid points.
    t_ground : float
        Ground temperature in Kelvin.
    lapse_rate : float
        Temperature gradient [K/m], usually negative.
    p_ground : float
        Surface pressure in Pa.

    Returns
    -------
    AtmosphericProfile
        Dataclass with arrays for height, temperature, pressure,
        conceptual energy and resonance index.
    """
    # 1) высота
    z = np.linspace(0.0, z_max, n_levels)  # [m]

    # 2) температура (очень грубый линейный профиль)
    T = t_ground + lapse_rate * z
    T[T < 180.0] = 180.0  # защита от нереалистично низких T

    # 3) давление (экспоненциальный спад, изотермическое приближение)
    g = 9.81   # [m/s^2]
    R = 287.0  # [J/(kg*K)]
    T_mean = (T + t_ground) / 2.0
    H = R * T_mean / g          # масштаб высоты
    P = p_ground * np.exp(-z / H)

    # 4) "энергия" как простая функция давления и температуры
    energy = P * T / 1e6        # произвольное масштабирование

    # 5) резонансный индекс = |вторая производная энергии по высоте|
    dz = z[1] - z[0]
    d2E_dz2 = np.zeros_like(energy)
    d2E_dz2[1:-1] = (energy[2:] - 2 * energy[1:-1] + energy[:-2]) / (dz ** 2)
    resonance_index = np.abs(d2E_dz2)

    return AtmosphericProfile(
        height=z,
        temperature=T,
        pressure=P,
        energy=energy,
        resonance_index=resonance_index,
    )
