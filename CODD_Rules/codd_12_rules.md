# Codd's 12 Rules for Relational Database Management Systems

Dr. E.F. Codd, the creator of the relational model for databases, defined these rules to determine if a Database Management System (DBMS) can be considered a true Relational DBMS (RDBMS). Note that there are actually 13 rules (numbered 0 to 12).

## Rule 0: The Foundation Rule
For any system that is advertised as, or claimed to be, a relational data base management system, that system must be able to manage data bases entirely through its relational capabilities.

## Rule 1: The Information Rule
All information in a relational data base is represented explicitly at the logical level and in exactly one way - by values in tables.

## Rule 2: The Guaranteed Access Rule
Each and every datum (atomic value) in a relational data base is guaranteed to be logically accessible by resorting to a combination of table name, primary key value and column name.

## Rule 3: Systematic Treatment of Null Values
Null values (distinct from the empty character string or a string of blank characters and distinct from zero or any other number) are supported in fully relational DBMS for representing missing information and inapplicable information in a systematic way, independent of data type.

## Rule 4: Dynamic Online Catalog Based on the Relational Model
The data base description is represented at the logical level in the same way as ordinary data, so that authorized users can apply the same relational language to its interrogation as they apply to the regular data.

## Rule 5: The Comprehensive Data Sublanguage Rule
A relational system may support several languages and various modes of terminal use (for example, the fill-in-the-blanks mode). However, there must be at least one language whose statements are expressible, per some well-defined syntax, as character strings and that is comprehensive in supporting all of the following items:
1. Data definition
2. View definition
3. Data manipulation (interactive and by program)
4. Integrity constraints
5. Authorization
6. Transaction boundaries (begin, commit and rollback)

## Rule 6: The View Updating Rule
All views that are theoretically updatable are also updatable by the system.

## Rule 7: High-Level Insert, Update, and Delete
The capability of handling a base relation or a derived relation as a single operand applies not only to the retrieval of data but also to the insertion, update and deletion of data.

## Rule 8: Physical Data Independence
Application programs and terminal activities remain logically unimpaired whenever any changes are made in either storage representations or access methods.

## Rule 9: Logical Data Independence
Application programs and terminal activities remain logically unimpaired when information-preserving changes of any kind that theoretically permit unimpairment are made to the base tables.

## Rule 10: Integrity Independence
Integrity constraints specific to a particular relational data base must be definable in the relational data sublanguage and storable in the catalog, not in the application programs.

## Rule 11: Distribution Independence
A relational DBMS has distribution independence. Distribution independence implies that users should not have to be aware of whether a database is distributed or not.

## Rule 12: The Nonsubversion Rule
If a relational system has a low-level (single-record-at-a-time) language, that low-level cannot be used to subvert or bypass the integrity rules and constraints expressed in the higher-level relational language (multiple-records-at-a-time).
