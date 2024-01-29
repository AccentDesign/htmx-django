# HTMX Django

Some basic examples using htmx in django:

* search form
* file list with upload and actions
* contact form

## Env vars

Copy `.env` to `.env.local` and edit accordingly.
```bash
cp .env .env.local
```

## Running

Using docker compose:
```bash
docker compose up
```

## Installing python packages

From the docker container terminal inside /app.

Install a package:
```bash
poetry add <package>
```

Install a dev package:
```bash
poetry add --dev <package>
```

Update all package:
```bash
poetry update
```

Update one or more package:
```bash
poetry update <package>
```

Show package dependency tree:
```bash
poetry show --tree
```

## Auto Code Linting

From the docker container terminal inside /app.

```bash
black .
```

```bash
ruff --fix .
```
