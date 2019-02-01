# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'postgres': {
        'command': ['pg_ctl', '-D', '"${PGDATA:-/home/jovyan/srv/pgsql}"','-l','"${PGDATA:-/home/jovyan/srv/pgsql}/pg.log"','restart'],
        'timeout': 120,
        'launcher_entry': {
            'enabled': True,
            'icon_path': '/home/jovyan/.jupyter/postgresql-logo.svg',
            'title': 'PostgreSQL',
        },
    },
    'pgadmin': {
        'command': ['python', '/srv/conda/lib/python3.6/site-packages/pgadmin4/pgAdmin4.py'],
        'timeout': 120,
        'port': 5050,
        'launcher_entry': {
            'enabled': True,
            'icon_path': '/home/jovyan/.jupyter/postgresql-logo.svg',
            'title': 'pgAdmin',
        },
    },
}
