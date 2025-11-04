"""
Run a demo simulation of the SvetLuna Hybrid Atmospheric Installation.

Usage:
    python -m src.run_simulation
"""

import os

import matplotlib.pyplot as plt

from .atmosphere_model import standard_profile


def main() -> None:
    profile = standard_profile()

    # переводим высоту в км для удобства графиков
    z_km = profile.height / 1000.0
    T = profile.temperature
    P_hpa = profile.pressure / 100.0  # Pa -> hPa
    E = profile.energy
    R = profile.resonance_index

    # создаём выходную папку
    out_dir = "output"
    os.makedirs(out_dir, exist_ok=True)

    fig, axes = plt.subplots(1, 4, figsize=(14, 5), sharey=True)

    axes[0].plot(T, z_km)
    axes[0].set_xlabel("Temperature [K]")
    axes[0].set_ylabel("Height [km]")
    axes[0].set_title("Temperature profile")

    axes[1].plot(P_hpa, z_km)
    axes[1].set_xlabel("Pressure [hPa]")
    axes[1].set_title("Pressure profile")

    axes[2].plot(E, z_km)
    axes[2].set_xlabel("Energy [arb. units]")
    axes[2].set_title("Energy potential")

    axes[3].plot(R, z_km)
    axes[3].set_xlabel("Resonance index [arb. units]")
    axes[3].set_title("Resonance zones")

    for ax in axes:
        ax.grid(True, linestyle="--", alpha=0.5)

    fig.suptitle("SvetLuna Hybrid Atmospheric Installation — 1D Column Demo",
                 fontsize=12)

    fig.tight_layout(rect=[0, 0.03, 1, 0.95])

    out_path = os.path.join(out_dir, "atmospheric_profile.png")
    fig.savefig(out_path, dpi=200)

    print(f"Saved plot to: {out_path}")


if __name__ == "__main__":
    main()
