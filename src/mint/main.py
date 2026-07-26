from pathlib import Path
import click
import shutil


def shared_inputs(func):
    func = click.argument("folder")(func)
    return func


@click.group()
def main():
    pass


@main.command()
@shared_inputs
def flask(folder):
    base_dir = Path.cwd() / folder

    try:
        template_path = Path(__file__).parent / "templates" / "flask" / "core"
        shutil.copytree(template_path, base_dir, ignore=shutil.ignore_patterns(".gitkeep"))
    except FileExistsError:
        click.secho("Folder already exists", fg="red", bold=True)
        raise click.Abort()
    except Exception as e:
        click.secho(f"Error: {e}", fg="red", bold=True)
        shutil.rmtree(base_dir, ignore_errors=True)
        raise click.Abort()


@main.command()
@shared_inputs
@click.option("--number", "-n", type=int, default=1)
@click.option("--no-xml", is_flag=True, default=False)
def servlet(folder, number, no_xml):
    base_dir = Path.cwd() / folder

    if no_xml and number != 1:
        raise click.UsageError("You cannot use --number/-n when --no-xml is passed.")

    if (number < 0):
        raise click.BadParameter("-n/--number should strictly be greater than or equal to 1", param_hint="--number")

    try:
        template_path = Path(__file__).parent / "templates" / "servlet" / "core"
        shutil.copytree(template_path, base_dir, ignore=shutil.ignore_patterns(".gitkeep"))


        with open(Path(__file__).parent / "templates" / "servlet" / "extra" / "web.xml", "r") as f:
            web_xml = f.read()

        repeated_content = "\n".join([web_xml for i in range(number)]).strip()

        xml_content = "\n".join(["<web-app>", repeated_content, "</web-app>"])

        with open(base_dir / "WEB-INF" / "web.xml", "w") as f:
            f.write(xml_content)

    except FileExistsError:
        click.secho("Folder already exists", fg="red", bold=True)
        raise click.Abort()
    except Exception as e:
        click.secho(f"Error: {e}", fg="red", bold=True)
        shutil.rmtree(base_dir, ignore_errors=True)
        raise click.Abort()


if __name__ == "__main__":
    main()
