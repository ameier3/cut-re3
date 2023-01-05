import os

server_url = os.environ.get("SERVER_URL", "localhost:3000")

# DATABASE
postgres_db = os.environ.get("POSTGRES_DB", "cut_dev")
postgres_host = os.environ.get("POSTGRES_HOST", "postgis")
postgres_user = os.environ.get("POSTGRES_USER", "postgres")
postgres_password = os.environ.get("POSTGRES_PASSWORD", "postgres")
postgres_port = os.environ.get("POSTGRES_PORT", "5432")

# GEOSERVER
geoserver_workspace = os.environ.get("GEOSERVER_WORKSPACE", "cut_dev")
geoserver_admin_user = os.environ.get("GEOSERVER_ADMIN_USER", "admin")
geoserver_admin_password = os.environ.get("GEOSERVER_ADMIN_PASSWORD", "geoserver")
