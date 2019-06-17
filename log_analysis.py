#!/usr/bin/env python2

import psycopg2
import datetime

DBNAME = "news"


# function to connect with database and execute db queries
def execute_query(query):
    try:
        # Connect to database
        conn = psycopg2.connect(database=DBNAME)
        # Open a cursor to perform database operations
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        # Close database connection
        cur.close()
        conn.close()
        return result

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


# function to find 3 most popular three articles of all time
def most_viewed_articles():
    # Query to retrieve top three most popular articles
    query = """
    SELECT articles.title, count(log.path) AS views
    FROM articles LEFT JOIN log
    ON log.path = concat('/article/',articles.slug)
    WHERE log.status = '200 OK'
    GROUP BY articles.title
    ORDER BY views DESC
    LIMIT 3;
    """
    articleviews = execute_query(query)
    # print the top 3 articles
    for article in articleviews:
        output = (article[0] + " - " + str(article[1]) + " views")
        print(output)


# funtion to find most popular article authors of all time
def most_popular_authors():
    # Query for finding most popular authors
    query = """
    SELECT name, count(log.path) AS views
    FROM authors JOIN articles ON authors.id = articles.author
    LEFT JOIN log ON log.path = concat('/article/', articles.slug)
    WHERE log.status = '200 OK'
    GROUP BY authors.name
    ORDER BY views desc;
    """
    authorviews = execute_query(query)
    # print most viewed authors
    for authorview in authorviews:
        output = (authorview[0] + " - " + str(authorview[1]) + " views")
        print(output)


# function to find which days did more than 1% of requests lead to errors?
# View should be present in the database for this function to run
def error_report():
    # query to find the date with >1% failed requests
    query = """
    SELECT request_date,
    ROUND((failed_views*100.0/total_views)::decimal, 2) AS failed_req_rate
    FROM view_log
    WHERE failed_views*100.0/total_views > 1;
    """
    failed_req_rates = execute_query(query)

    # print the error_rates
    for failed_req_rate in failed_req_rates:
        output = (failed_req_rate[0].strftime('%B %d, %Y') + " - " +
                  str(failed_req_rate[1]) + "% errors")
        print(output)


if __name__ == '__main__':
    title = "LOG REPORT"
    print('________________________________________________________________')
    print(title.center(60, ' '))
    print('________________________________________________________________')
    print('\n1. What are the most popular three articles of all time?\n')
    most_viewed_articles()
    print('\n----------------------------------------------------------------')
    print('2. Who are the most popular article authors of all time?\n')
    most_popular_authors()
    print('\n----------------------------------------------------------------')
    print("3. On which days did more than 1% of requests lead to errors?\n")
    error_report()
    print('________________________________________________________________')
