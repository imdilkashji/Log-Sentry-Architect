# Log-Sentry Architect: Algorithmic Log Analysis Engine

A lightweight, production-ready pipeline designed to ingest raw application server logs, isolate critical system anomalies, and calculate operational statistics using pure Python.

## Core Features
- **Dynamic Log Stream Simulation:** Automatically generates realistic server data using random seeds.
- **Anomalous Event Detection:** Implements precise conditional filtering to flag runtime errors (`CRITICAL`, `ERROR`).
- **Statistical Metric Synthesis:** Calculates error density distributions across standard timeframes.

## Code Directory Structure
- `sentry_engine.py`: Core processing algorithm and file I/O operations.
- `mock_generator.py`: Generates simulation traffic logs.

## Setup & Execution
Run the pipeline directly from your terminal:
```bash
python mock_generator.py
python sentry_engine.py