from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://u25x8dti78pwwfsu774l:pscale_pw_DxaGUWS3Ktz2CG5x9Go09L6aXUExjsJC9ZzKXz8NvBg@aws.connect.psdb.cloud/mycareers?charset=utf8mb4"

engine = create_engine(db_connection_string, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(zip(result.keys(), row)))
    return jobs
