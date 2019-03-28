DROP TABLE IF EXISTS todos;

CREATE TABLE todos (
  id bigserial PRIMARY KEY,
  completed boolean NOT NULL,
  todo_date date NOT NULL,
  todo_text text NOT NULL
);
