from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://awvpe68xmutlpqm80gxb:pscale_pw_9Y9Gz4weXOb3fDiAocwnivqCRinigMDWNWHn2EAPZ9w@aws.connect.psdb.cloud/mycareers?charset=utf8mb4"

engine = create_engine(db_connection_string,connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})