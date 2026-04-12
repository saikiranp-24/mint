import pathlib
from pathlib import Path
import click
import textwrap

# print(Path.cwd())

@click.command()
@click.argument('target')
def main(target):
    fp = Path.cwd()

    target = target.lower()
    if target == 'flask':
        flask(fp)
    elif target == 'servlet':
        servlet(fp)


def flask(fp):

    static_folder = fp / 'static'
    base_html = fp / 'templates' / 'index.html'
    app = fp / 'app.py'

    html_content = textwrap.dedent("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{% block title %}{% endblock %}</title>
        </head>
        <body>
            {% block content %}{% endblock %}
        </body>
        </html>
        """).strip()

    click.echo(static_folder)
    click.echo(base_html)
    click.echo(app)

    static_folder.mkdir(exist_ok=True)
    base_html.parent.mkdir(parents=True, exist_ok=True)
    base_html.touch(exist_ok=True)
    app.touch(exist_ok=True)

    base_html.write_text(html_content)

    click.secho("Flask boilerplate generated successfully!", fg="green", bold=True)

def servlet(fp):
    web_inf = fp / 'WEB-INF'
    classes = web_inf / 'classes'
    xml = web_inf / 'web.xml'



if __name__ == '__main__':
    main()