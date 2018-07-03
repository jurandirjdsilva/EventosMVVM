insert INTO User values(NULL,'nome','email@email.email');
insert INTO Credential values(NULL,'usuario','senhaMD5',1);
insert INTO Endereco values(NULL,'rua xyz','bairro feliz','goiania','74000-000');
insert INTO Evento values (NULL,'feira','29/06/2018','29/06/2018','feira da fruta','onde uns vendem frutas para os outros... ',NULL,NULL,1);


selct * from User;
select userID,name,email from User where userID = 1;
select userID from Credential 