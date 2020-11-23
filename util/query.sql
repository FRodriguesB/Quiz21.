create table categoria(
	cod_categoria integer primary key autoincrement,
	categoria varchar(500) not null
);

create table pergunta(
	cod_pergunta integer primary key autoincrement,
	pergunta varchar(500) not null,
	cod_categoria integer not null,
	imagem blob not null, 
	constraint fk_pergunta_cod_categoria
		foreign key (cod_categoria)
		references categoria(cod_categoria)
);


create table resposta(
	cod_resposta integer primary key autoincrement,
	resposta varchar(4000) not null,
	cod_pergunta integer not null,
	constraint fk_resposta_cod_pergunta
		foreign key (cod_pergunta)
		references resposta(cod_resposta)
);

create table gabarito(
	cod_gabarito integer primary key autoincrement,
	cod_pergunta integer not null unique,
	cod_resposta integer not null,
	constraint fk_gabarito_cod_pergunta
		foreign key (cod_pergunta)
		references pergunta(cod_pergunta),
	constraint fk_gabarito_cod_resposta
		foreign key (cod_resposta)
		references resposta(cod_resposta)
);

create table resultado(
	cod_resultado integer primary key autoincrement,
	cod_pergunta integer not null,
	correta char(1) check(correta in ('S', 'N')),
	data_registro timestamp default current_timestamp,
	constraint fk_resultado_cod_pergunta
		foreign key (cod_pergunta)
		references pergunta(cod_pergunta)
);

drop table resultado;

create table resultado(
	cod_resultado integer primary key autoincrement,
	cod_pergunta integer not null,
	correta char(1) check(correta in ('S', 'N')),
	data_registro date,
	constraint fk_resultado_cod_pergunta
		foreign key (cod_pergunta)
		references pergunta(cod_pergunta)
);

CREATE TRIGGER tg_data_resultado
AFTER INSERT ON resultado
BEGIN
   UPDATE resultado SET data_registro =STRFTIME('%Y-%m-%d', 'NOW') WHERE cod_resultado = NEW.cod_resultado;
END;

