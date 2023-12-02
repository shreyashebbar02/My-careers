from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://hb7i1o31cw024amigpzh:pscale_pw_x4LgA7V3oxRlZ5zVbEs0FdMluiRAYJCAvESTesKy9Ho@aws.connect.psdb.cloud/mycareers?charset=utf8mb4"

engine = create_engine(db_connection_string, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(zip(result.keys(), row)))
    return jobs
