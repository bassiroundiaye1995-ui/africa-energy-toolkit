# Africa Energy Toolkit (AET)

An open-source Python toolkit for practical renewable-energy and energy-efficiency calculations, designed with African use cases in mind.

## Why this project?

Energy engineers, students, analysts, developers, and project teams often rebuild the same calculations in spreadsheets. AET aims to provide transparent, testable, reusable building blocks for:

- Solar PV sizing
- Battery sizing
- Energy and carbon calculations
- Electricity-cost analysis
- Project KPIs
- Scenario analysis

The project is intentionally modular so contributors can add country-specific datasets, tariffs, climate assumptions, and new calculation modules without changing the core engine.

## Current status

**Early-stage / community project.**

The first release focuses on transparent calculation primitives. It is not a replacement for detailed engineering software or a professional feasibility study.

## Quick start

```bash
pip install -e .
```

Then:

```python
from aet import solar_pv

result = solar_pv.size_system(
    daily_energy_kwh=12,
    peak_sun_hours=5.5,
    system_efficiency=0.80,
)

print(result)
```

## CLI

```bash
aet solar-pv --daily-energy 12 --sun-hours 5.5 --efficiency 0.80
```

## Development

```bash
git clone https://github.com/YOUR_USERNAME/africa-energy-toolkit.git
cd africa-energy-toolkit

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -e ".[dev]"
pytest
```

## Roadmap

- [x] Initial solar PV sizing engine
- [x] Battery sizing engine
- [x] Energy-cost calculations
- [x] Carbon-emissions calculations
- [x] CLI
- [x] Automated tests
- [ ] Country tariff datasets
- [ ] African solar-resource datasets
- [ ] Financial model for PV + battery projects
- [ ] Interactive web dashboard
- [ ] French documentation
- [ ] English documentation expansion
- [ ] Country modules contributed by the community

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

Useful contributions include:

- New calculation modules
- Tests and bug fixes
- Documentation
- Country-specific datasets
- Examples
- Translations
- Performance improvements

## License

MIT. See [LICENSE](LICENSE).

## Disclaimer

This toolkit provides educational and analytical calculations. Results should be reviewed by a qualified professional before being used for engineering, financial, safety, or regulatory decisions.
