--
-- File generated with SQLiteStudio v3.2.1 on Sun Oct 13 17:02:24 2019
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: movie_list
CREATE TABLE movie_list (movie_name VARCHAR, s_no INTEGER PRIMARY KEY NOT NULL UNIQUE, release_year INTEGER, rating_imdb DECIMAL (10, 2));
INSERT INTO movie_list (movie_name, s_no, release_year, rating_imdb) VALUES ('Interstellar', 1, 2014, 10);
INSERT INTO movie_list (movie_name, s_no, release_year, rating_imdb) VALUES ('Interstellar', 2, 2014, 10);
INSERT INTO movie_list (movie_name, s_no, release_year, rating_imdb) VALUES ('Interstellar', 3, 2014, 10);
INSERT INTO movie_list (movie_name, s_no, release_year, rating_imdb) VALUES ('Interstellar', 4, 2014, 10);
INSERT INTO movie_list (movie_name, s_no, release_year, rating_imdb) VALUES ('Interstellar', 5, 2014, 10);
INSERT INTO movie_list (movie_name, s_no, release_year, rating_imdb) VALUES ('Interstellar', 6, 2014, 10);
INSERT INTO movie_list (movie_name, s_no, release_year, rating_imdb) VALUES ('Interstellar', 7, 2014, 10);
INSERT INTO movie_list (movie_name, s_no, release_year, rating_imdb) VALUES ('Interstellar', 8, 2014, 10);
INSERT INTO movie_list (movie_name, s_no, release_year, rating_imdb) VALUES ('Interstellar', 9, 2014, 10);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
