CREATE DATABASE PurBeurre CHARACTER SET 'utf8';
USE PurBeurre;

-- creating the table `store`
CREATE TABLE store (
                id SMALLINT AUTO_INCREMENT NOT NULL,
                name VARCHAR(100) NOT NULL,
                PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- creating the table `category`
CREATE TABLE category (
                id SMALLINT AUTO_INCREMENT NOT NULL,
                name VARCHAR(40) NOT NULL,
                number INT NOT NULL,
                PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- creating the table `food_store`
CREATE TABLE food_store (
                id_food SMALLINT UNSIGNED NOT NULL,
                id_store SMALLINT NOT NULL,
                PRIMARY KEY (id_food, id_store)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- creating the table `users`
CREATE TABLE users (
                id SMALLINT AUTO_INCREMENT NOT NULL,
                e_mail VARCHAR(100) NOT NULL,
                password VARCHAR(20) NOT NULL,
                pseudo VARCHAR(20) NOT NULL,
                PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE UNIQUE INDEX user_idx
 ON users
 ( password, pseudo );

-- creating the table `user_food`
CREATE TABLE user_food (
                id_food SMALLINT UNSIGNED NOT NULL,
                id_user SMALLINT NOT NULL,
                id_substitute SMALLINT UNSIGNED NOT NULL,
                PRIMARY KEY (id_food, id_user, id_substitute)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- creating the table `food`
CREATE TABLE food (
                id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                id_store SMALLINT NOT NULL,
                id_category SMALLINT NOT NULL,
                name VARCHAR(40) NOT NULL,
                number INT NOT NULL,
                brands VARCHAR(100),
                nutriscore VARCHAR(1),
                url VARCHAR(50)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


ALTER TABLE food_store
ADD CONSTRAINT store_food_store_fk1
FOREIGN KEY (id_store)
REFERENCES store(id);

ALTER TABLE food_store
ADD CONSTRAINT food_food_store_fk
FOREIGN KEY (id_food)
REFERENCES food (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE food
ADD CONSTRAINT category_food_fk
FOREIGN KEY (id_category)
REFERENCES category (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE user_food
ADD CONSTRAINT food_user_food_fk
FOREIGN KEY (id_food)
REFERENCES food (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE user_food ADD CONSTRAINT food_user_food_fk1
FOREIGN KEY (id_substitute)
REFERENCES food (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE user_food ADD CONSTRAINT user_user_food_fk
FOREIGN KEY (id_user)
REFERENCES users (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;