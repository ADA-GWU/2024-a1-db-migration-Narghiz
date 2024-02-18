import psycopg2

dbname = "students"
user = "postgres"
password = "1234"
host = "localhost"
port = "5432"

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()

try:
    cur.execute("ALTER TABLE interests RENAME COLUMN interests TO interest")
    cur.execute("ALTER TABLE interests ALTER COLUMN interest TYPE VARCHAR(255)")

    cur.execute("ALTER TABLE students ALTER COLUMN st_name TYPE VARCHAR(20)")
    cur.execute("ALTER TABLE students ALTER COLUMN st_last TYPE VARCHAR(20)")

    cur.execute("ALTER TABLE students RENAME COLUMN student_id TO st_id")

    cur.execute("""
        UPDATE interests i
        SET interest = (
            SELECT interest
            FROM interests
            WHERE student_id = i.student_id
            LIMIT 1
        )
        WHERE EXISTS (
            SELECT 1
            FROM interests
            WHERE student_id = i.student_id
            GROUP BY student_id
            HAVING COUNT(*) > 1
        )
    """)

    conn.commit()
    print("Rollback completed successfully.")

except Exception as e:
    conn.rollback()
    print("Error during rollback:", e)

finally:
    cur.close()
    conn.close()
