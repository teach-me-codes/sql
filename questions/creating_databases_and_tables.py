questions = [
    {
        'Main question': 'What is the importance of creating databases and tables in SQL Basics?',
        'Explanation': "Creating databases and tables is crucial in SQL Basics as it defines the structure and schema of the data to be stored, enabling efficient data organization, retrieval, and manipulation.",
        'Follow-up questions': ['How does the creation of databases enhance data management in SQL?', 'What role do tables play in structuring data within a database?', 'Can you explain the significance of defining schema while creating tables in SQL?']
    },
    {
        'Main question': 'How is the database creation process typically done using SQL statements?',
        'Explanation': "SQL statements like CREATE DATABASE are used to create a new database in SQL, allowing users to specify the database name, character set, and other properties.",
        'Follow-up questions': ['What are the key parameters to consider when creating a new database in SQL?', 'Can you demonstrate the syntax for creating a database in SQL with an example?', 'How can databases be managed and manipulated after they are created using SQL commands?']
    },
    {
        'Main question': 'What are the essential components of creating tables within a database using SQL?',
        'Explanation': "Creating tables in SQL involves specifying the table name, column names, data types, constraints, and relationships to establish the structure of the stored data within the database.",
        'Follow-up questions': ['How do data types in SQL contribute to defining the attributes of table columns?', 'In what ways can constraints ensure data integrity and consistency in SQL tables?', 'Discuss the importance of defining relationships between tables for data normalization and efficiency in SQL databases.']
    },
    {
        'Main question': 'How can primary keys be defined and utilized in SQL table creation?',
        'Explanation': "Primary keys are used to uniquely identify each record in a table, ensuring data integrity and enabling efficient data retrieval and indexing in SQL databases.",
        'Follow-up questions': ['What criteria should be considered when selecting a primary key for a table in SQL?', 'How does the concept of indexing relate to primary keys and data retrieval performance?', 'Can you explain the potential impacts of primary key constraints on data insertion and modification operations in SQL tables?']
    },
    {
        'Main question': 'What is the role of foreign keys in establishing relationships between tables in SQL databases?',
        'Explanation': "Foreign keys link tables by referencing the primary key of another table, enforcing referential integrity and facilitating data retrieval and maintenance across related tables in SQL databases.",
        'Follow-up questions': ['How do foreign key constraints support data consistency and relational integrity in SQL databases?', 'Discuss the impact of cascading actions associated with foreign keys on data modifications in related tables.', 'Can you provide an example scenario where foreign keys are essential for maintaining data relationships and integrity in SQL databases?']
    },
    {
        'Main question': 'How can different types of constraints be applied during table creation in SQL?',
        'Explanation': "Constraints like NOT NULL, UNIQUE, DEFAULT, and CHECK can be specified when creating tables in SQL to enforce data integrity, uniqueness, and validation rules on column values.",
        'Follow-up questions': ['Explain the purpose and functionality of the NOT NULL constraint in SQL table creation.', 'In what scenarios would you use the UNIQUE constraint to ensure data uniqueness in SQL tables?', 'How does the CHECK constraint help validate and restrict data values entered into specific columns of a table in SQL?']
    },
    {
        'Main question': 'What options are available for defining relationships between tables in SQL, apart from foreign keys?',
        'Explanation': "In addition to foreign keys, relationships between tables in SQL can be established using constraints like UNIQUE constraints, CHECK constraints, and triggers to enforce data validation and maintain data consistency.",
        'Follow-up questions': ['How does a UNIQUE constraint contribute to defining one-to-one relationships between tables in SQL?', 'Discuss the use of CHECK constraints for implementing custom data validation rules and conditions across related tables.', 'Can you explain how triggers can be utilized to automate actions and maintain data integrity in interrelated tables within an SQL database?']
    },
    {
        'Main question': 'How is the process of normalizing data handled during table creation in SQL databases?',
        'Explanation': "Normalization in SQL involves organizing data into multiple related tables to reduce redundancy and dependency, ensuring data integrity and efficiency in storage and retrieval.",
        'Follow-up questions': ['What are the different normal forms in database normalization, and how do they eliminate data anomalies?', 'Explain the concept of denormalization and when it can be beneficial in SQL database design.', 'How does the normalization process optimize database performance and query efficiency in SQL systems?']
    },
    {
        'Main question': 'What are the advantages of using views in SQL database management?',
        'Explanation': "Views in SQL provide a virtual representation of data stored in tables, offering simplified data access, enhanced security, and encapsulation of complex queries for improved performance and usability.",
        'Follow-up questions': ['How can views improve data security by restricting access to specific columns or rows in SQL databases?', 'Discuss the benefits of using views for simplifying complex queries and aggregating data from multiple tables.', 'In what scenarios would materialized views be preferred over standard views for optimizing query performance in SQL database systems?']
    },
    {
        'Main question': 'How does the concept of indexing contribute to optimizing data retrieval performance in SQL databases?',
        'Explanation': "Indexing in SQL allows for the creation of ordered data structures that expedite data retrieval operations by enabling faster search and retrieval of specific data based on indexed columns.",
        'Follow-up questions': ['What factors should be considered when determining which columns to index in a table for performance enhancement in SQL databases?', 'Explain the differences between clustered and non-clustered indexes in SQL and their impact on query performance.', 'Can you discuss the potential trade-offs associated with indexing, such as increased storage requirements and performance overhead in SQL database systems?']
    }
]