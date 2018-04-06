CREATE TABLE IF NOT EXISTS user.users(                            
    -> id INT NOT NULL AUTO_INCREMENT,
    -> nome varchar(50) NOT NULL, 
    -> sobrenome varchar(50) NOT NULL, 
    -> endereco varchar(100) NOT NULL,
    -> PRIMARY KEY(id)
    -> );