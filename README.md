### Install mint
#### Linux
Use our installer [script](https://raw.githubusercontent.com/saikiranp-24/mint/main/install.sh)
```
curl -fsSL https://raw.githubusercontent.com/saikiranp-24/mint/main/install.sh | sh
```

or install with homebrew
```bash
brew install saikiranp-24/tap/mint
```

#### macOS
Install with homebrew
```bash
brew install saikiranp-24/tap/mint
```

### Windows
Install with scoop
```bash
scoop bucket add saikiranp-24 https://github.com/saikiranp-24/scoop-bucket
scoop install saikiranp-24/mint
```

Alternatively, you could use [uv](https://github.com/astral-sh/uv) on any of its supported platforms to install
```
uv tool install git+https://github.com/saikiranp-24/mint
```

#### Usage
`mint` is a boilerplate scaffold tool designed for

- Flask
- Servlets

Get started with:
```
mint --help
Usage: mint [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  flask
  servlet
```

The sub-commands available are `flask` and `servlet`, each sub-command expects a required argument `FOLDER`
`FOLDER` here is the target directory where boilerplate is generated.
The directory should be non-existent or should be empty for mint to scaffold in it.

So the structure is:
```
mint [OPTIONS] COMMAND <FOLDER> [ARGS]
```

See [docs](https://saikiranp-24.github.io/mint/) for complete usage description of mint
