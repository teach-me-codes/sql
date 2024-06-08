questions = [
{'Main question': 'What is the basic concept of querying data in SQL?',
 'Explanation': 'The main concept of querying data in SQL involves using the SELECT statement to retrieve data from one or more tables. It includes filtering, sorting, and aggregating data using various clauses and functions.',
 'Follow-up questions': ['How can the WHERE clause be used to filter data in SQL queries?', 'What are some common aggregate functions used in SQL for data summarization?', 'Explain the difference between the GROUP BY and ORDER BY clauses in SQL.']
},

{'Main question': 'How does the GROUP BY clause function in SQL queries?',
 'Explanation': 'The GROUP BY clause in SQL is used to group rows that have the same values into summary rows, such as finding the total sales per region or the average salary per department.',
 'Follow-up questions': ['What is the purpose of the HAVING clause in conjunction with the GROUP BY clause in SQL?', 'Can you explain the difference between GROUP BY and DISTINCT in SQL queries?', 'How does the ORDER BY clause interact with the GROUP BY clause in SQL queries?']
},

{'Main question': 'What are the different types of JOIN operations in SQL?',
 'Explanation': 'JOIN operations in SQL are used to combine rows from two or more tables based on a related column between them, with common types including INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.',
 'Follow-up questions': ['When would you use an INNER JOIN versus an OUTER JOIN in SQL queries?', 'What is a self-join in SQL and in what scenarios is it used?', 'How does the CROSS JOIN operation differ from other types of JOINs in SQL?']
},

{'Main question': 'How can subqueries be utilized in SQL for data retrieval and manipulation?',
 'Explanation': 'Subqueries in SQL are nested queries that provide a way to use the output of an inner query (subquery) as the input for the outer query, often used for complex filtering, calculations, or conditional logic.',
 'Follow-up questions': ['What are correlated subqueries and how do they differ from non-correlated subqueries in SQL?', 'Can you give an example of using a subquery to find the second highest value in a table?', 'In what scenarios would you choose to use a subquery over a JOIN operation in SQL?']
},

{'Main question': 'What is the purpose of the ORDER BY clause in SQL queries?',
 'Explanation': 'The ORDER BY clause in SQL is used to sort the result set of a query in ascending or descending order based on one or more columns, allowing for customized presentation of query results.',
 'Follow-up questions': ['How does the ORDER BY clause interact with the DISTINCT keyword in SQL queries?', 'Can you provide an example of using the ORDER BY clause with multiple columns for sorting?', 'What role does the NULLS FIRST or NULLS LAST option play in the ORDER BY clause?']
},

{'Main question': 'How can the WHERE clause be used for filtering data in SQL queries?',
 'Explanation': 'The WHERE clause in SQL is used to filter records based on specified conditions, allowing for the retrieval of specific data that meets the defined criteria within a query.',
 'Follow-up questions': ['What logical operators can be used in conjunction with the WHERE clause for complex filtering conditions?', 'How does the BETWEEN operator work in filtering data compared to using multiple AND conditions?', 'Can you explain the difference between the LIKE and = operators in SQL for pattern matching in WHERE clause conditions?']
},

{'Main question': 'What are the key differences between the DISTINCT and GROUP BY clauses in SQL queries?',
 'Explanation': 'The DISTINCT keyword in SQL is used to return unique rows from the result set, while the GROUP BY clause is used to group rows that have the same values into summary rows with aggregate functions.',
 'Follow-up questions': ['How does the performance of DISTINCT compare to GROUP BY in SQL queries on large datasets?', 'In what scenarios would you choose to use DISTINCT over GROUP BY or vice versa?', 'Can you provide an example where using DISTINCT and GROUP BY would yield different query results?']
},

{'Main question': 'How does the LIMIT clause aid in controlling result set size in SQL queries?',
 'Explanation': 'The LIMIT clause in SQL is used to restrict the number of rows returned by a query, allowing for the control of the result set size and improving query efficiency by reducing unnecessary data retrieval.',
 'Follow-up questions': ['What is the difference between the LIMIT and OFFSET clauses when used together in SQL queries?', 'Can you explain how the ROW_NUMBER() function can achieve similar functionality to the LIMIT clause in SQL?', 'How does the TOP clause in Microsoft SQL Server compare to the LIMIT clause in other database systems like MySQL or PostgreSQL?']
},

{'Main question': 'What role does the HAVING clause play in SQL queries, and how does it differ from the WHERE clause?',
 'Explanation': 'The HAVING clause in SQL is used in combination with the GROUP BY clause to filter rows based on aggregate conditions, typically for aggregate functions like SUM, AVG, COUNT, MIN, or MAX, after the GROUP BY operation has been performed.',
 'Follow-up questions': ['Why can\'t you use the WHERE clause with aggregate functions directly, and when is the HAVING clause necessary?', 'In what order are the clauses (WHERE, GROUP BY, HAVING) evaluated in a SQL query?', 'Can you provide an example where using HAVING produces different results from using WHERE in a SQL query?']
},

{'Main question': 'How are NULL values handled in SQL queries, and what considerations should be made when working with NULLs?',
 'Explanation': 'NULL values in SQL represent missing or unknown data, and they require special handling to correctly include or exclude them in filtering or aggregation operations, often requiring the use of IS NULL or IS NOT NULL conditions.',
 'Follow-up questions': ['What impact can NULL values have on the result set of a query and the calculations performed on columns?', 'How does the COALESCE function help in managing NULL values when retrieving data in SQL?', 'Can you discuss the potential pitfalls and challenges of working with NULL values in database queries and how to address them effectively?']
}
]