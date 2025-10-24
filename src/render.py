import os
import sys
from datetime import datetime

from jinja2 import Environment, FileSystemLoader, select_autoescape

from functions import write_file


src_dir = os.path.dirname(os.path.realpath(__file__))
templates = os.path.join(src_dir, "templates")
output = os.path.join(src_dir, "output")

env = Environment(loader=FileSystemLoader(templates), autoescape=select_autoescape())


def render_file(source, target, data):
    print(f"rendering: {source} -> {target}")
    template = env.get_template(f"{source}")
    result = template.render(data)
    write_file(os.path.join(output, f"{target}"), result, True)


to_render = sys.argv[1] if len(sys.argv) > 1 else "all"
print(f"{datetime.now().isoformat()} - Rendering: {to_render}")

if to_render in ["all", "redirect"]:
    file_data = {
        "url": "https://smashedr.github.io/github-projects/",
        "text": "/github-projects",
        "title": "Rolf Broke",
        "timer": 3,
    }
    render_file("redirect.jinja", "redirect.html", file_data)
