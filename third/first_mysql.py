import pymysql.cursors


conn = pymysql.connect(host='localhost',
                       user='root',
                       password='ya', db='scraping')


c = conn.cursor()

c.execute("""
    CREATE TABLE `cities` (
            `rank` integer,
            `city` text,
            `population` integer)
    """)
c.execute(`INSERT INTO `cities` VALUES (%(rank)s, %(city)s, %(population)s)`,
        {'rank': 2, 'city': 'KARACHI', 'population':235000})

with connection.
