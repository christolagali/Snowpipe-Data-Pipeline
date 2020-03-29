import connect as cn

try:

    conn = cn.getConnection()

    query = 'select * from "PUBLIC"."VENUE" limit 3'

    resultset = conn.cursor().execute(query)

    for i in resultset.description:
        print(i)
    

    conn.cursor().execute('ALTER WAREHOUSE SUSPEND')

except Exception as e:
    print(e)
