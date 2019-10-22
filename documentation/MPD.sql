CREATE DATABASE PurBeurre CHARACTER SET 'utf8';
USE PurBeurre;

-- creating the table `category`
CREATE TABLE category (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL UNIQUE,
                PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- creating the table `store`
CREATE TABLE store (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL UNIQUE,
                PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- creating the table `brand`
CREATE TABLE brand (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL,
                PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- creating the table `food`
CREATE TABLE food (
                id INT NOT NULL,
                name VARCHAR(500) NOT NULL UNIQUE,
                nutriscore VARCHAR(1),
                url VARCHAR(255),
                last_modified DATE,
                PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- creating the table `users`
CREATE TABLE user (
                id INT AUTO_INCREMENT NOT NULL,
                e_mail VARCHAR(255) NOT NULL,
                pseudo VARCHAR(255) NOT NULL,
                password VARCHAR(20) NOT NULL,
                PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE UNIQUE INDEX user_idx
 ON user
 ( password, pseudo );

-- creating the table `food_brand`
CREATE TABLE food_brand (
                id_food INT NOT NULL,
                id_brand INT NOT NULL,
                PRIMARY KEY (id_food, id_brand)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- creating the table `food_store`
CREATE TABLE food_store (
                id_food INT NOT NULL,
                id_store INT NOT NULL,
                PRIMARY KEY (id_food, id_store)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- creating the table `category_food`
CREATE TABLE category_food (
                id_category INT NOT NULL,
                id_food INT NOT NULL,
                PRIMARY KEY (id_category, id_food)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- creating the table `user_food`
CREATE TABLE user_food (
                id_user INT NOT NULL,
                id_food INT NOT NULL,
                id_substitute INT NOT NULL,
                PRIMARY KEY (id_user, id_food, id_substitute)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE food_brand ADD CONSTRAINT brands_food_brands_fk
FOREIGN KEY (id_brand)
REFERENCES brand (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE food_store ADD CONSTRAINT store_food_store_fk
FOREIGN KEY (id_store)
REFERENCES store (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE food_store ADD CONSTRAINT food_food_store_fk
FOREIGN KEY (id_food)
REFERENCES food (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE user_food ADD CONSTRAINT food_user_food_fk
FOREIGN KEY (id_food)
REFERENCES food (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE user_food ADD CONSTRAINT food_user_food_fk1
FOREIGN KEY (id_substitute)
REFERENCES food (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE category_food ADD CONSTRAINT food_category_food_fk
FOREIGN KEY (id_food)
REFERENCES food (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE food_brand ADD CONSTRAINT food_food_brands_fk
FOREIGN KEY (id_food)
REFERENCES food (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE category_food ADD CONSTRAINT category_category_food_fk
FOREIGN KEY (id_category)
REFERENCES category (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE user_food ADD CONSTRAINT user_user_food_fk
FOREIGN KEY (id_user)
REFERENCES user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;