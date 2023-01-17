SELECT * FROM my_schema.todo;

INSERT INTO my_schema.todo (prio, comment)
VALUES 
('Prio 1', 'Buy Pie soup'),
('Prio 2', 'Buy toothpaste')
;

ALTER TABLE my_schema.todo ADD COLUMN status VARCHAR(10);

UPDATE my_schema.todo
SET status = ('Done')
WHERE prio = 'Prio 1';

UPDATE my_schema.todo
SET status = ('not done')
WHERE prio = 'Prio 2';
