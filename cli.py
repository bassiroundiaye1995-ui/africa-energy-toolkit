import argparse
from .solar_pv import size_system

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="aet",
        description="Africa Energy Toolkit",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    pv = subparsers.add_parser("solar-pv", help="Estimate PV capacity")
    pv.add_argument("--daily-energy", type=float, required=True)
    pv.add_argument("--sun-hours", type=float, required=True)
    pv.add_argument("--efficiency", type=float, default=0.80)

    args = parser.parse_args()

    if args.command == "solar-pv":
        result = size_system(
            args.daily_energy,
            args.sun_hours,
            args.efficiency,
        )
        print(f"Required PV capacity: {result.required_kwp:.2f} kWp")

if __name__ == "__main__":
    main()
