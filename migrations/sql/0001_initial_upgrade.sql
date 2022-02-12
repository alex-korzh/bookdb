CREATE TABLE users (
	id UUID NOT NULL,
	email VARCHAR(120) NOT NULL,
	username VARCHAR(120) NOT NULL,
	password VARCHAR(120) NOT NULL,
	is_active BOOLEAN NOT NULL,
	is_banned BOOLEAN NOT NULL,
	role roletype,
	PRIMARY KEY (id),
	UNIQUE (id),
	UNIQUE (email),
	UNIQUE (username)
);
CREATE TABLE books (
	id SERIAL NOT NULL,
	image VARCHAR(255),
	isbn VARCHAR(255) NOT NULL,
	language VARCHAR(64) NOT NULL,
	publisher VARCHAR(255) NOT NULL,
	size INTEGER,
	title VARCHAR(64) NOT NULL,
	year INTEGER,
	PRIMARY KEY (id),
	UNIQUE (id),
	UNIQUE (isbn)
);
CREATE TABLE authors (
	id SERIAL NOT NULL,
	name VARCHAR(255) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (id)
);
CREATE TABLE genres (
	id SERIAL NOT NULL,
	name VARCHAR(255) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (id)
);
CREATE TABLE book_to_author (
	book_id INTEGER,
	author_id INTEGER,
	FOREIGN KEY(book_id) REFERENCES books (id),
	FOREIGN KEY(author_id) REFERENCES authors (id)
);
CREATE TABLE book_to_genre (
	book_id INTEGER,
	genre_id INTEGER,
	FOREIGN KEY(book_id) REFERENCES books (id),
	FOREIGN KEY(genre_id) REFERENCES genres (id)
);