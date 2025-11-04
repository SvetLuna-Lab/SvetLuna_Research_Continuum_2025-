# ⚙️ SvetLuna Hybrid Atmospheric Installation

_Core research project — 2025_

---

## 🌩️ Overview

The Hybrid Atmospheric Installation is an experimental system designed to capture and
store atmospheric electric energy via controlled corona discharge and resonant
accumulation. The project combines principles of electrical engineering, atmospheric
physics, and resonance-based energy modeling.

---

## 🧭 System Schematic

![Hybrid Atmospheric Installation schematic](78cd4ddd-4886-4c52-9949-6272c710aa7a.png)

Hybrid atmospheric resonance + accumulator system (schematic).  
*(Diagram text intentionally kept in Russian to preserve original engineering notation.)*

---

## 🧩 System Architecture

- **Corona wire** — high-voltage emitter for atmospheric ionization  
- **Atmospheric electrodes** — field collectors and charge transfer nodes  
- **Mast insulation** — multi-layer dielectric isolation  
- **Current-limited rectifiers** — safe conversion of atmospheric current  
- **Measuring shunt & damper** — current sensing and protection  
- **Resonance circuit** — frequency-matched phase loop  
- **Charge controller** — regulated energy flow  
- **Supercapacitor block** — fast-response accumulator  
- **LiFePO₄ battery** — long-term storage  
- **DC outputs 12 V / 24 V** — power delivery for loads  

---

## 🐍 Python model

The repository also contains a small Python model of the hybrid atmospheric installation:

- `src/atmosphere_model.py` – 1D atmospheric column model  
  (height, temperature, pressure, conceptual energy, resonance index).
- `src/run_simulation.py` – script that runs a demo and saves plots to `output/`.

Run the demo locally:

```bash
python -m src.run_simulation
The script will generate output/atmospheric_profile.png with four panels
(temperature, pressure, energy potential, and resonance index vs height).

📁 Repository layout
README.md — project overview

78cd4ddd-4886-4c52-9949-6272c710aa7a.png — installation schematic (used above)

src/ — Python package for the atmospheric model

output/ — generated plots (created on first run)

report_text_2.pdf — technical report with current-flow modeling

report_content_text5.pdf — extended data, parameters, and logs

Final_Tech.pdf — core technical summary and final conclusions

© 2025 Svetlana Romanova (SvetLuna)
Independent researcher — hybrid atmospheric energy systems.

