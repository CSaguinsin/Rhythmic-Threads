# Rhythmic Threads API

## Development

> [!NOTE]\
> API Documentation can be accessed at [http://localhost:5000/docs](http://localhost:5000/docs)

Activate virtual environment (inside `./api` directory)

```sh
python -m venv .venv
```

Enter virtual environment:

```
For Windows Powershell
./.venv/Scripts/Activate.ps1

or:

./.venv/Scripts/activate
```

### Installing Dependencies

```sh
pip install -r requirements.txt
```

### Preparing the database

Create a new database:

```sh
# Schema are inside sql/schema.sql
flask --app app setup-db
```

This will create a new SQLite database in the `instance` folder.

### Running the API

Create `.env` from `.env.sample` file in the `./api` directory:

```shell
cp .env.sample .env
```

Generate secret key for authentication:

```sh
python -c 'import secrets; print(secrets.token_hex())'
```

and add the following:

```sh
DEBUG=True
SECRET_KEY=<secret_key>
```

Run flask inside `api/`:

```sh
flask run # or with --debug
```

### Submitting Changes

After making changes, make sure all tests pass to
verify that the changes are working as expected,
and did not break any existing functionality:

```sh
./.venv/Scripts/pytest
```

or

```sh
pytest
```
