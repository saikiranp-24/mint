from pathlib import Path
import click
import textwrap

# print(Path.cwd())

@click.command()
@click.argument('target')
@click.argument('folder')
def main(target, folder):
    base_dir = Path.cwd() / folder

    target = target.lower()
    if target == 'flask':
        flask(base_dir)
    elif target == 'servlet':
        servlet(base_dir)


def flask(base_dir):

    static_folder = base_dir / 'static'
    base_html = base_dir / 'templates' / 'base.html'
    index_html = base_dir / 'templates' / 'index.html'
    app = base_dir / 'app.py'


    try:
        base_dir.mkdir(exist_ok=False)

        static_folder.mkdir(exist_ok=True)
        base_html.parent.mkdir(parents=True, exist_ok=True)
        base_html.touch(exist_ok=True)
        index_html.parent.mkdir(parents=True, exist_ok=True)
        index_html.touch(exist_ok=True)
        app.touch(exist_ok=True)

        base_content = textwrap.dedent("""\
            <!DOCTYPE html>
            <html lang="en">
            <head>
                {% block head %}
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{% block title %}{% endblock %}</title>
                {% endblock %}
            </head>
            <body>
                {% block content %}{% endblock %}
            </body>
            </html>
            """)

        index_content = textwrap.dedent("""\
            {% extends "base.html" %}

            {% block title %}Home{% endblock %}
            {% block head %}

            {# This template part can be removed #}
            <style>
                    :root {
                        --bg: #f8fafc;
                        --text: #0f172a;
                        --primary: #3b82f6;
                        --card-bg: #ffffff;
                    }
                    body {
                        font-family: system-ui, -apple-system, sans-serif;
                        background-color: var(--bg);
                        color: var(--text);
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        min-height: 100vh;
                        margin: 0;
                    }
                    .hero {
                        background-color: var(--card-bg);
                        padding: 3rem;
                        border-radius: 12px;
                        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
                        text-align: center;
                        max-width: 500px;
                    }
                    h1 {
                        margin-top: 0;
                        color: var(--primary);
                    }
                    p {
                        color: #475569;
                        line-height: 1.6;
                    }
                    .code-block {
                        background: #f1f5f9;
                        padding: 0.5rem 1rem;
                        border-radius: 6px;
                        font-family: monospace;
                        color: #d946ef;
                        margin-top: 1.5rem;
                        display: inline-block;
                    }
                </style>
            {% endblock %}

            {% block content %}
            {# This template part can be removed #}
            <div class="hero">
                    <h1>Project Generated!</h1>
                    <p>Your application has been successfully scaffolded and is ready for development.</p>
                    <p>Next steps:</p>
                    <div class="code-block">
                        Edit <b>index.html</b> to get started
                    </div>
                </div>
            {% endblock %}
        """)

        app_content = textwrap.dedent("""\
            from flask import Flask, render_template

            app = Flask(__name__)

            @app.route('/')
            def index():
                return render_template('index.html')

            if __name__ == '__main__':
                app.run(debug=True)
        """)

        base_html.write_text(base_content)
        index_html.write_text(index_content)
        app.write_text(app_content)

        click.secho("Flask boilerplate generated successfully!", fg="green", bold=True)

    except FileExistsError:
        click.secho("Folder already exists", fg="red", bold=True)
        raise click.Abort()
    except Exception:
        click.secho("Couldn't generate boilerplate files!", fg="red", bold=True)
        raise click.Abort()

def servlet(base_dir):
    web_inf = base_dir / 'WEB-INF'
    classes = web_inf / 'classes'
    xml = web_inf / 'web.xml'

    try:
        base_dir.mkdir(exist_ok=False)

        web_inf.mkdir(exist_ok=True)
        classes.mkdir(exist_ok=True)
        xml.touch(exist_ok=True)

        xml_content = textwrap.dedent("""\
        <web-app>
            <servlet>
                <servlet-name></servlet-name>
                <servlet-class></servlet-class>
            </servlet>
            <servlet-mapping>
                <servlet-name></servlet-name>
                <url-pattern></url-pattern>
            </servlet-mapping>
        </web-app>
        """)

        xml.write_text(xml_content)

        click.secho("Boilerplate generated successfully!", fg='green', bold=True)

    except FileExistsError:
        click.secho("Folder already exists", fg="red", bold=True)
        raise click.Abort()
    except Exception:
        click.secho("Couldn't generate boilerplate files!", fg="red", bold=True)
        raise click.Abort()


if __name__ == '__main__':
    main()
