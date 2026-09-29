from pathlib import Path
import importlib

from telegram.ext import Application


def register_commands(app: Application):
    commands_dir = Path(__file__).parent.parent / "commands"

    for file in commands_dir.glob("*.py"):
        if file.name == "__init__.py":
            continue

        module = importlib.import_module(f"commands.{file.stem}")

        if hasattr(module, "register"):
            module.register(app)