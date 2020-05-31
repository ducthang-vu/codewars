/*
SQL: Concatenating Columns

https://www.codewars.com/kata/59440034e94fae05b2000073/train/sql

Given the table below:

** names table schema **

id
prefix
first
last
suffix
Your task is to use a select statement to return a single column table containing the full title of the person (concatenate all columns together except id), as follows:

** output table schema **

title
Don't forget to add spaces.
*/


select (prefix || ' ' || first || ' ' || last || ' ' || suffix) as title
from names


/* SOLUTION
SELECT concat_ws(' ', prefix,first,last,suffix) AS title FROM names;
*/