# Rhythmic Threads API

> [!CAUTION]\
> Login functionality is not yet implemented. All actions/endpoints can be accessed without authentication.

## Development

> [!NOTE]\
> API Documentation can be accessed at [http://localhost:5000](http://localhost:5000) by default.

Activate virtual environment

```sh
python -m venv .venv
```

> [!IMPORTANT]\
> Make sure you execute that command **inside `./api` directory**.

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

#### Seeding the database (Optional)

To seed the database with sample random data:

```sh
flask -A app seed-db
```

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

> [!NOTE]\
> If you encounter `An attempt was made to access a socket in a way forbidden by its access permissions`,
>
> Change port where the app is served:
>
> ```sh
> flask run -p 6060  # 6060 or whatever port you want
> ```
>
> API can now be accessed at designated port. Ex: [http://localhost:6060](http://localhost:6060).

### Submitting Changes

**Verify** that the changes are working as expected,
and **did not break any existing functionality**:

```sh
pytest
```

> [!CAUTION]\
> **Failing existing tests signifies existing feature breakages.**
