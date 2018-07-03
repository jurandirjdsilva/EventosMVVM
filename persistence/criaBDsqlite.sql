DROP TABLE  Endereco;
CREATE TABLE Endereco(
    enderecoID INTEGER PRIMARY KEY AUTOINCREMENT,
    logradouro TEXT,
    bairro TEXT,
    cidade  TEXT,
    cep TEXT
);
DROP TABLE  Evento; 
CREATE TABLE Evento (
    eventoID INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT ,
    dataInicio TEXT ,
    dataFinal TEXT ,
    nomeEvento TEXT ,
    descricao TEXT ,
    cartazDoEvento TEXT ,
    fotoIcone TEXT,
    enderecoID INTEGER,
    CONSTRAINT enderecoFK
        FOREIGN KEY (enderecoID)
        REFERENCES Endereco(enderecoID)
);

DROP TABLE User;
CREATE TABLE User(
  userID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
);
DROP TABLE Credential;
CREATE TABLE Credential(
  credentialID INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    password TEXT,
    
    userID INTEGER,
    CONSTRAINT userFK
        FOREIGN KEY (userID)
        REFERENCES User(userID)
);