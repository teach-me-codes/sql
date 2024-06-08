questions = [
    {
        'Main question': 'What is a subquery in SQL, and how is it used?',
        'Explanation': 'The candidate should explain the concept of a subquery as a query nested within another query in SQL to retrieve intermediate results for further processing or filtering the main query results.',
        'Follow-up questions': [
            'Can you provide an example of a subquery being used in a SELECT statement?',
            'How does the result of a subquery impact the overall query performance?',
            'What are the different types of subqueries that can be used in SQL?'
        ]
    },
    {
        'Main question': 'How can subqueries be classified based on their return value?',
        'Explanation': 'The candidate should discuss the classification of subqueries as scalar, row, column, and table subqueries based on the number of rows and columns they return and where they can be used within SQL statements.',
        'Follow-up questions': [
            'What distinguishes a scalar subquery from other types of subqueries?',
            'When would you choose to use a row subquery over a column subquery in SQL queries?',
            'Can you explain the scenarios where a table subquery would be the most appropriate choice?'
        ]
    },
    {
        'Main question': 'How do correlated subqueries differ from non-correlated subqueries?',
        'Explanation': 'The candidate should differentiate between correlated and non-correlated subqueries based on their interaction with the outer query and how they can reference values from the outer query within the subquery.',
        'Follow-up questions': [
            'What are the performance implications of using correlated subqueries?',
            'Can you provide an example where a correlated subquery is more suitable than a non-correlated subquery?',
            'How does the optimizer handle the execution of correlated subqueries compared to non-correlated ones?'
        ]
    },
    {
        'Main question': 'What are the advantages of using subqueries in SQL?',
        'Explanation': 'The candidate should discuss the benefits of using subqueries, such as simplifying complex queries, improving code readability, and enabling dynamic queries by providing a way to break down a problem into smaller, manageable parts.',
        'Follow-up questions': [
            'How can subqueries help in reducing redundancy in SQL queries?',
            'In what scenarios would you recommend using a subquery instead of a JOIN operation?',
            'Can you elaborate on how subqueries contribute to writing more modular and reusable SQL code?'
        ]
    },
    {
        'Main question': 'How can subqueries be optimized for better query performance?',
        'Explanation': 'The candidate should explain optimization techniques for subqueries, including using appropriate indexing, avoiding unnecessary subqueries, and understanding the query execution plan to improve overall query efficiency.',
        'Follow-up questions': [
            'What role does query caching play in optimizing subquery performance?',
            'When should correlated subqueries be rewritten as non-correlated subqueries for better optimization?',
            'Can you discuss any common pitfalls to avoid when working with subqueries for performance considerations?'
        ]
    },
    {
        'Main question': 'How do subqueries contribute to data manipulation in SQL?',
        'Explanation': 'The candidate should illustrate how subqueries can be employed for data manipulation tasks such as inserting, updating, deleting, or filtering data based on specific conditions by using the results of the subquery as part of the manipulation operation.',
        'Follow-up questions': [
            'In what scenarios would you use a subquery for updating data in a relational database?',
            'Can you provide an example of using a subquery to filter and delete specific records from a table?',
            'How can subqueries be utilized to perform bulk insertions based on conditions in SQL statements?'
        ]
    },
    {
        'Main question': 'How can subqueries be nested to handle more complex querying tasks?',
        'Explanation': 'The candidate should demonstrate the nesting of multiple subqueries within a single SQL statement to tackle intricate querying requirements, involving multiple levels of subquery dependencies and logical operations.',
        'Follow-up questions': [
            'What are the considerations when nesting multiple subqueries to maintain query clarity and manageability?',
            'Can you explain a scenario where nesting subqueries becomes essential for achieving the desired query result?',
            'How does nesting subqueries impact query optimization and execution compared to using single-level subqueries?'
        ]
    },
    {
        'Main question': 'What are the limitations or challenges associated with using subqueries in SQL?',
        'Explanation': 'The candidate should address the limitations like potential performance bottlenecks, readability issues in complex nested queries, and the need for understanding optimizer behavior to tackle challenges related to subquery usage in SQL.',
        'Follow-up questions': [
            'How does the depth of nesting subqueries affect query readability and maintenance?',
            'What strategies can be employed to mitigate performance issues when using multiple levels of subqueries?',
            'In what scenarios would you consider refactoring subqueries into temporary tables for better query performance and management?'
        ]
    },
    {
        'Main question': 'How can correlated subqueries be rewritten as JOIN operations for optimization?',
        'Explanation': 'The candidate should explain the process of transforming correlated subqueries into JOIN operations to enhance query performance by leveraging the relational algebra and optimizing the query execution plan.',
        'Follow-up questions': [
            'What are the key differences in execution between a correlated subquery and an equivalent JOIN operation?',
            'Can you provide an example where rewriting a correlated subquery as a JOIN leads to a more efficient query execution?',
            'How do JOIN strategies like nested loop, hash join, and merge join impact the performance of the transformed query compared to the original correlated subquery?'
        ]
    },
    {
        'Main question': 'How do subqueries interact with the main query in terms of data flow and result processing?',
        'Explanation': 'The candidate should describe the flow of data between the main query and subquery, including how results are passed, processed, and integrated to produce the final result set, highlighting the sequential execution of SQL statements.',
        'Follow-up questions': [
            'What happens when a subquery returns multiple rows or no rows during execution?',
            'How is the output of a subquery utilized by the main query in scenarios involving aggregation or filtering operations?',
            'Can you explain the sequence of events that occur when a main query contains multiple subqueries with dependencies on each other?'
        ]
    }
]