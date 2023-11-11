# FIFA WORLD CUP - EDA ⚽

This project endeavors to comprehensively investigate the FIFA dataset through the utilization of structured query language (SQL). The intricacies of the dataset were meticulously scrutinized by executing queries on an Oracle database, with the ensuing results meticulously documented to provide a comprehensive exploratory data analysis (EDA) output. The objective of this endeavor is to extract meaningful insights and patterns inherent within the FIFA dataset, thereby contributing to a deeper understanding of the intricate dynamics encapsulated within the realm of football analytics.


## How to Run?

1. Clone this repository to your local machine using:
    ```
    git clone https://github.com/Magical-Mist/FIFA_SQL_EDA.git
    ```
2. Execute create_table.sql on your SQL server
3. Execute insert.py using:
    ```
    python insert.py
    ```
    Note: The code is written to connect to `Oracle DB`
4. Finally, execute EDA.sql


## Program Structure

- datasets: This directory houses three CSV files, each containing pertinent information about FIFA winners, match details, and player profiles.
- create_table.sql: SQL queries have been implemented to establish the requisite tables for storing data extracted from the aforementioned datasets.
- insert.py: This Python script serves as a dynamic tool for seamlessly inserting all records into the established tables. Its functionality is designed to maintain the integrity and format consistency of the stored information.
- EDA.sql: This file encapsulates the essence of exploratory data analysis (EDA) through a series of SQL queries. These queries unravel a deeper comprehension of the intricacies involved in the FIFA dataset.
- Output: The Output directory holds spool files meticulously capturing the outputs of each query contained in the EDA.sql file.
