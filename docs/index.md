---
hide:
  - navigation
---

#### Description
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

#### Flask
The directory structure for flask boilerplate is as:

```
flask-project
├── app.py
├── static
└── templates
    ├── base.html
    └── index.html

3 directories, 3 files
```

This is the default structure expected by flask and each of the files generated here are populated with template content.

Boilerplate within `app.py` is as:
```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

Similarly other files are also populated in flask boilerplate to scaffold a ready to run template project.

#### Servlets
Servlet boilerplate generation is more aligned with legacy way of handling servlets.
```bash
Usage: mint servlet [OPTIONS] FOLDER

Options:
  -n, --number INTEGER  Specify number of servlet objects in web.xml
  --no-xml              Opt out of generating web.xml
  --index               Generate index.html
  --help                Show this message and exit.
```

Default template structure:
```bash
template-servlet
└── WEB-INF
    ├── classes
    └── web.xml
```

The file `web.xml` here is populated with one servlet inside the root `web-app` element as:
```bash
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
```

##### `--number` option
The number of servlet elements in the file can be controlled with the `-n` (shorthand for `--number`) as:
```
mint servlet -n 3 template-servlet
```

This produces 3 `servlet` elements within the root element `web-app`

##### `--no-xml` flag
You can use the `--no-xml` flag to opt out of generating `web.xml` in the boilerplate as:
```bash
mint servlet --no-xml template-servlet
```

so the structure would be:

```bash
template-servlet
└── WEB-INF
    └── classes
```

##### `--index` flag
The `--index` flag is used to generate an `index.html` at the boilerplate root
```bash
mint servlet --index servlet-1
```

so the structure would be
```bash
servlet-1
├── WEB-INF
│   ├── classes
│   └── web.xml
└── index.html
```


