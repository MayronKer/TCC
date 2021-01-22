CREATE DATABASE projeto;

USE projeto;

CREATE TABLE usuario(
	id INT AUTO_INCREMENT PRIMARY KEY,
    email varchar(45) NOT NULL,
    senha varchar(45) NOT NULL,
    nome varchar(45) NOT NULL,
    dataCadastro date NOT NULL,
    genero TINYINT(3),
    dataNasc date
);

CREATE TABLE transtorno(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome varchar(45) NOT NULL,
    descricao varchar(45),
    ocorrencia double #Índice de ocorrência desse transtorno
);

CREATE TABLE sintoma(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome varchar(45) NOT NULL,
    descricao varchar(45)
);

CREATE TABLE sessao(
	id INT AUTO_INCREMENT PRIMARY KEY,
	dataInicio datetime,
    dataTermino datetime,
    statusSessao TINYINT(3),
    idUsuario INT
);

CREATE TABLE transtorno_has_sintoma(
	idTranstorno INT,
    idSintoma INT,
    FOREIGN KEY (idTranstorno)
		REFERENCES transtorno(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	FOREIGN KEY (idSintoma)
		REFERENCES sintoma(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
