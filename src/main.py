import os
from pathlib import Path

from actions import core
from jinja2 import Environment, FileSystemLoader, select_autoescape

from functions import write_file


version: str = core.get_version()
core.info(f"🏳️ Starting Create Files Action - \033[36;1m{version}")


# Inputs
core.start_group("Inputs")
input_type = core.get_input("type").lower()
core.info(f"input_type: \033[36;1m{repr(input_type)}")
input_file = core.get_input("file")
core.info(f"input_file: \033[36;1m{repr(input_file)}")
data = core.get_data("data")
core.info(f"data: {data}")
core.end_group()  # Inputs


# Setup
core.start_group("Setup")
core.info(f"getcwd: {os.getcwd()}")
src_path = Path(__file__).resolve().parent
core.info(f"src_path: {src_path}")
templates = src_path / "templates"
core.info(f"templates: {templates}")
core.end_group()  # Setup

# Action
core.info(f"⌛ Processing type: \033[35m{input_type}")

env = Environment(loader=FileSystemLoader(templates), autoescape=select_autoescape())

result = None

if input_type == "redirect":
    if "url" not in data:
        core.set_failed("Missing required data: url")
    ctx = {"title": "Redirecting", "timer": 5}
    ctx.update(data)
    if "text" not in ctx:
        ctx["text"] = data["url"]
    template = env.get_template("redirect.jinja")
    result = template.render(ctx)
    write_file(input_file, result, True)
elif input_type == "robots":
    result = "User-agent: *\nDisallow: /\n"
    write_file(input_file, result, True)
else:
    core.set_failed(f"Unknown type: {input_type}")

if not result:
    core.set_failed("No results, this is probably a bug?")


# Output
core.set_output("content", result)

core.info("✅ \033[32;1mFinished Success")
