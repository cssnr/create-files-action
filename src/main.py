import os
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from yaml import Loader, load

from functions import write_file


version: str = os.environ.get("GITHUB_WORKFLOW_REF", "") or "Dev Build"
version = version.rsplit("/", 1)[-1]

print(f"🏳️ Starting Create Files Action - {version}")


# Environment
print("::group::Environment")
src_path = Path(__file__).resolve().parent
print(f"src_path: {src_path}")
templates = src_path / "templates"
print(f"templates: {templates}")
print("::endgroup::")  # Environment


# Inputs
print("::group::Parse Inputs")
input_type = os.environ.get("INPUT_TYPE", "").strip().lower()
print(f"input_type: \033[36;1m{input_type}")
input_file = os.environ.get("INPUT_FILE", "").strip()
print(f"input_file: \033[36;1m{input_file}")
input_data = os.environ.get("INPUT_DATA", "").strip()
# print(f"input_data: \033[36;1m{input_data}")
print("::endgroup::")  # Parse Inputs


# Data
print("::group::Parse Data")
data = load(input_data, Loader=Loader)
print(f"data: {data}")
print("::endgroup::")  # Parse Data


env = Environment(loader=FileSystemLoader(templates), autoescape=select_autoescape())

print(f"⌛ Processing type: \033[32m{input_type}")

result = None

if input_type == "redirect":
    if "url" not in data:
        print("::error::Missing required data: url")
        sys.exit(1)
    ctx = {"title": "Redirecting", "timer": 3}
    ctx.update(data)
    if "text" not in ctx:
        ctx["text"] = data["url"]
    template = env.get_template("redirect.jinja")
    result = template.render(ctx)
    # print(f"result: {result}")
    if input_file:
        write_file(input_file, result, True)
elif input_type == "robots":
    content = "User-agent: *\nDisallow: /\n"
    with open(input_file, "w") as f:
        f.write(content)
else:
    print(f"::error::Unknown type: {input_type}")
    sys.exit(1)


# Outputs
# https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
if result:
    print("Setting output: content")
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        # noinspection PyTypeChecker
        print(f"content<<EOF\n{result}\nEOF", file=f)


print("✅ \033[32;1mFinished Success")
