# %%
import pyodbc
import pandas as pd
import pickle

conn_str = (
            "DRIVER={PostgreSQL ODBC Driver(UNICODE)};"
            "SERVER=localhost;"
            "DATABASE=NLP;"
            "UID=postgres;"
            "PWD=postgres;"
            "PORT=5432;"
            )
pyodbcConn = pyodbc.connect(conn_str)

# %%
BGG_sample = pd.read_sql_query(
                f"""
                SELECT comment
                , round(cast(rating as real)) as Rating
                FROM public.bgg_bgg_15m_reviews
                WHERE round(cast(rating as real))>=1
                    and comment !='NaN'
                    and length(comment)>10
                LIMIT 1000000;
                """
                , pyodbcConn, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)

BGG_sample

# %%
BGG_sample.to_pickle('BGG_sample.pickle')

# %%
