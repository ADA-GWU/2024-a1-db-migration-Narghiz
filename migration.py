import psycopg2

dbname = "students"
user = "postgres"
password = "1234"
host = "localhost"
port = "5432"

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()

try:
    cur.execute("ALTER TABLE students RENAME COLUMN st_id TO student_id")

    cur.execute("ALTER TABLE students ALTER COLUMN st_name TYPE VARCHAR(30)")
    cur.execute("ALTER TABLE students ALTER COLUMN st_last TYPE VARCHAR(30)")

    cur.execute("ALTER TABLE interests RENAME COLUMN interest TO interests")
    cur.execute("ALTER TABLE interests ALTER COLUMN interests TYPE VARCHAR(255)")

    cur.execute("""
        UPDATE interests i
        SET interests = (
            SELECT '[' || string_agg(QUOTE_LITERAL(interests), ',') || ']'
            FROM (
                SELECT DISTINCT interests
                FROM interests
                WHERE student_id = i.student_id
            ) AS subquery
        )
    """)

    conn.commit()
    print("Migration completed successfully.")

except Exception as e:
    conn.rollback()
    print("Error during migration:", e)

finally:
    cur.close()
    conn.close()
