"""
CLI entry-point for GitHub Achievement Lab.

Provides a command-line interface with subcommands for calculation,
workflow guidance, achievement tracking, and project status reporting.
"""

from __future__ import annotations

import argparse
import sys
from typing import Optional

from achievement_lab import __version__
from achievement_lab.calculator import Calculator, ValidationError
from achievement_lab.workflows import AchievementStatus, WorkflowGuide

# ─── ANSI colour helpers ────────────────────────────────────────────────────

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
DIM = "\033[2m"


def _c(colour: str, text: str) -> str:
    """Wrap text in an ANSI colour code."""
    return f"{colour}{text}{RESET}"


# ─── Banner ─────────────────────────────────────────────────────────────────

BANNER = f"""
{CYAN}{BOLD}╔══════════════════════════════════════════════════╗
║        GitHub Achievement Lab  v{__version__}          ║
║   Learn professional GitHub workflows hands-on  ║
╚══════════════════════════════════════════════════╝{RESET}
"""


# ─── Sub-command handlers ────────────────────────────────────────────────────

def cmd_calculate(args: argparse.Namespace) -> int:
    """Handle the `calculate` sub-command."""
    calc = Calculator()
    try:
        # Parse and validate operands independently for precise error messages
        def _parse_operand(raw: str, label: str) -> float:
            try:
                return float(raw)
            except ValueError:
                print(
                    _c(RED, f"✗ Error: {label} argument {raw!r} is not a valid number."),
                    file=sys.stderr,
                )
                print(
                    _c(DIM, f"  Usage: achievement-lab calculate <number> <number> [--operation OP]"),
                    file=sys.stderr,
                )
                raise

        try:
            a = _parse_operand(args.a, "first")
            b = _parse_operand(args.b, "second")
        except ValueError:
            return 2

        op = args.operation.lower()
        op_map = {
            "add": (calc.add, "+"),
            "subtract": (calc.subtract, "−"),
            "multiply": (calc.multiply, "×"),
            "divide": (calc.divide, "÷"),
            "power": (calc.power, "^"),
        }

        if op not in op_map:
            print(
                _c(RED, f"✗ Unknown operation '{op}'. Choose: {', '.join(op_map)}."),
                file=sys.stderr,
            )
            return 2

        fn, symbol = op_map[op]
        result = fn(a, b)
        print(f"\n  {_c(CYAN, f'{a} {symbol} {b}')} = {_c(GREEN, str(result))}\n")
        return 0

    except ValidationError as exc:
        print(_c(RED, f"✗ Validation error: {exc}"), file=sys.stderr)
        return 2
    except ZeroDivisionError as exc:
        print(_c(RED, f"✗ Math error: {exc}"), file=sys.stderr)
        return 1


def cmd_status(args: argparse.Namespace) -> int:
    """Handle the `status` sub-command — project status report."""
    print(BANNER)
    status = WorkflowGuide.get_project_status()

    print(_c(BOLD, "  📊 Project Status\n"))
    print(f"  {'Project':<28} {status['project']}")
    print(f"  {'Version':<28} {status['version']}")
    print(f"  {'Total achievements tracked':<28} {status['total_achievements']}")
    print(f"  {'Currently earnable':<28} {status['available_achievements']}")
    print(f"  {'Historical (no longer earnable)':<28} {status['historical_achievements']}")
    print(f"  {'Workflow steps documented':<28} {status['workflow_steps']}")
    print()

    if getattr(args, "verbose", False):
        # Print a detailed achievement progress table
        print(_c(BOLD, "  🏆 Achievement Progress Table\n"))
        col_name = 22
        col_status = 16
        col_tier = 24
        header = (
            f"  {'Achievement':<{col_name}} {'Status':<{col_status}} "
            f"{'Tier Progression':<{col_tier}} Requirement"
        )
        print(_c(CYAN, header))
        print(_c(DIM, "  " + "─" * 90))

        for item in WorkflowGuide.get_achievement_progress():
            name = str(item["name"])[:col_name]
            s = str(item["status"])
            # Strip emoji for width calculation
            status_clean = s[:col_status]
            tier = str(item["tier"])[:col_tier]
            req = str(item["requirement"])[:50]
            print(f"  {name:<{col_name}} {status_clean:<{col_status}} {tier:<{col_tier}} {req}")
        print()
    else:
        print(_c(BOLD, "  🏆 Earnable Achievements:"))
        for name in status["achievement_names"]:
            print(f"    • {name}")
        print()
        print(_c(DIM, "  Tip: Run `achievement-lab status --verbose` for a detailed progress table."))
        print()

    return 0


def cmd_workflow(args: argparse.Namespace) -> int:
    """Handle the `workflow` sub-command — show the PR workflow."""
    print(BANNER)
    print(_c(BOLD, "  🔄 Standard GitHub PR Workflow\n"))
    for step in WorkflowGuide.get_workflow_steps():
        print(_c(CYAN, f"  ─── Step {step.number}: {step.title}"))
        print(f"    $ {_c(YELLOW, step.command)}")
        print(f"    → {step.description}\n")
    return 0


def cmd_achievements(args: argparse.Namespace) -> int:
    """Handle the `achievements` sub-command — show achievement guide."""
    print(BANNER)
    print(_c(BOLD, "  🏆 GitHub Achievement Guide\n"))

    all_achievements = WorkflowGuide.get_achievements()
    grouped: dict[str, list] = {}
    for a in all_achievements:
        key = a.status.value
        grouped.setdefault(key, []).append(a)

    for status_label, items in grouped.items():
        print(_c(BOLD, f"\n  {status_label}\n  {'─' * 48}"))
        for achievement in items:
            print(achievement.display())
            print()
    return 0


def cmd_about(args: argparse.Namespace) -> int:
    """Handle the `about` sub-command."""
    print(BANNER)
    print(
        "  GitHub Achievement Lab is an open-source project for learning\n"
        "  professional Git/GitHub workflows through a real, working codebase.\n\n"
        "  It demonstrates:\n"
        "    • Branching and feature development\n"
        "    • Pull requests and code review\n"
        "    • GitHub Actions / CI\n"
        "    • Issue tracking and releases\n"
        "    • Co-authored contributions\n"
        "    • Open-source documentation practices\n\n"
        f"  Repository: https://github.com/thrilokm/github-achievement-lab\n"
        f"  Version   : {__version__}\n"
        f"  License   : MIT\n"
    )
    return 0


# ─── Argument parser ─────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    """Construct and return the top-level argument parser."""
    parser = argparse.ArgumentParser(
        prog="achievement-lab",
        description="GitHub Achievement Lab — learn professional GitHub workflows",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  achievement-lab calculate 10 20\n"
            "  achievement-lab calculate 10 4 --operation divide\n"
            "  achievement-lab calculate 2 8 --operation power\n"
            "  achievement-lab status\n"
            "  achievement-lab workflow\n"
            "  achievement-lab achievements\n"
            "  achievement-lab about\n"
        ),
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    sub = parser.add_subparsers(dest="command", metavar="<command>")
    sub.required = True

    # ── calculate ──────────────────────────────────────────────────────────
    calc_parser = sub.add_parser(
        "calculate",
        aliases=["calc"],
        help="Perform arithmetic: add, subtract, multiply, divide, power",
    )
    calc_parser.add_argument("a", help="First operand (numeric)")
    calc_parser.add_argument("b", help="Second operand (numeric)")
    calc_parser.add_argument(
        "-o", "--operation",
        default="add",
        metavar="OP",
        help="Operation: add | subtract | multiply | divide | power (default: add)",
    )
    calc_parser.set_defaults(func=cmd_calculate)

    # ── status ──────────────────────────────────────────────────────────────
    status_parser = sub.add_parser("status", help="Show project status report")
    status_parser.add_argument(
        "-V", "--verbose",
        action="store_true",
        help="Show full achievement progress table",
    )
    status_parser.set_defaults(func=cmd_status)

    # ── workflow ─────────────────────────────────────────────────────────────
    workflow_parser = sub.add_parser("workflow", help="Show the standard GitHub PR workflow")
    workflow_parser.set_defaults(func=cmd_workflow)

    # ── achievements ──────────────────────────────────────────────────────────
    ach_parser = sub.add_parser(
        "achievements",
        aliases=["ach"],
        help="Show GitHub achievement guide and requirements",
    )
    ach_parser.set_defaults(func=cmd_achievements)

    # ── about ─────────────────────────────────────────────────────────────────
    about_parser = sub.add_parser("about", help="About this project")
    about_parser.set_defaults(func=cmd_about)

    return parser


# ─── Entry-point ─────────────────────────────────────────────────────────────

def main(argv: Optional[list[str]] = None) -> int:
    """
    Main entry-point for the CLI.

    Args:
        argv: Argument list (defaults to sys.argv[1:]).

    Returns:
        Exit code (0 = success, 1 = runtime error, 2 = usage error).
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
