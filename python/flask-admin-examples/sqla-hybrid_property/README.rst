Example of how to use (and filter on) a hybrid_property with the SQLAlchemy backend.

Hybrid properties allow you to treat calculations (for example: first_name + last_name)
like any other database column.

To run this example:

1. Clone the repository::

    git clone https://github.com/flask-admin/flask-admin.git
    cd flask-admin

2. Create and activate a virtual environment::

    virtualenv env
    source env/bin/activate

3. Install requirements::

    pip install -r 'examples/sqla-hybrid_property/requirements.txt'

4. Run the application::

    python examples/sqla-hybrid_property/app.py

The first time you run this example, a sample sqlite database gets populated automatically. To suppress this behaviour,
comment the following lines in app.py:::

    if not os.path.exists(database_path):
        build_sample_db()
