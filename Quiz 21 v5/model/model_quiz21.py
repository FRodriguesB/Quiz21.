#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

class sql():
	def __init__(self, id=0, pergunta="", categoria="", resposta1="", resposta2="", resposta3=""):
		self.conexao = sqlite3.connect("banco.db")
		self.cursor = self.conexao.cursor()

#----------------------------------------------------------------------------------------------------------------------#
                                                                                            #Tela Cadastrar Pergunta
#----------------------------------------------------------------------------------------------------------------------#
	def inserirPergunta(self, pergunta, cod_categoria, imagem):
			
		sql_args = [pergunta, cod_categoria, sqlite3.Binary(imagem)]
		sql_nova_pergunta = (" insert into pergunta"
					         " (pergunta, cod_categoria,"
					         " imagem)"
					         " values (?, ?, ?)")
		self.cursor.execute(sql_nova_pergunta, sql_args)
		self.conexao.commit()
	
	def atualizarPergunta(self, pergunta, cod_pergunta):
		sql_args = [pergunta, cod_pergunta]
		sql_update_pergunta = (" update pergunta"
							   " set pergunta = (?)"
							   " where cod_pergunta = (?)")
		self.cursor.execute(sql_update_pergunta, sql_args)
		self.conexao.commit()
        
	def buscarPergunta(self, filtro):        
		sql_busca_pergunta = (" select p.cod_pergunta, p.pergunta,"
							  " c.categoria "
					          " from pergunta p"
					          " join categoria c"
					          " on p.cod_categoria ="
					          " c.cod_categoria"
					          " where p.pergunta"
					          " like '%{}%'".format(filtro))
		self.cursor.execute(sql_busca_pergunta)
		return self.cursor.fetchall()
		
	def apagarPergunta(self, codigo):
		for i in codigo:
			sql_args = [i]
			sql_deletar_pergunta = (" delete from pergunta"
									" where cod_pergunta in (?)")
			self.cursor.execute(sql_deletar_pergunta, sql_args)
			self.conexao.commit()
            
#----------------------------------------------------------------------------------------------------------------------#
                                                                                           #Tela Cadastrar Categoria
#----------------------------------------------------------------------------------------------------------------------#

	def inserirCategoria(self, categoria):
		sql_args = [categoria]
		sql_nova_categoria = ("insert into categoria"
							  "(categoria) values (?)")
		self.cursor.execute(sql_nova_categoria, sql_args)
		self.conexao.commit()
        
	def atualizarCategoria(self, categoria, cod_categoria):
		sql_args = [categoria, cod_categoria]
		sql_update_categoria = (" update categoria"
							    " set categoria = (?)"
							    " where cod_categoria = (?)")
							    
		self.cursor.execute(sql_update_categoria, sql_args)
		self.conexao.commit()

	def buscarCategoria(self, filtro):
		sql_busca_categoria = (" select c.cod_categoria,"
							   " c.categoria "
					           " from categoria c"
					           " where c.categoria"
					           " like '%{}%'".format(filtro))
       
		self.cursor.execute(sql_busca_categoria)
		return self.cursor.fetchall()

	def apagarCategoria(self, codigo):
		for i in codigo:
			sql_args = [i]
			sql_deletar_categoria = (" delete from categoria"
									 " where cod_categoria in (?)")
			self.cursor.execute(sql_deletar_categoria, sql_args)
			self.conexao.commit()

#----------------------------------------------------------------------------------------------------------------------#
                                                                                           #Tela Cadastrar Resposta
#----------------------------------------------------------------------------------------------------------------------#
	def buscarPerguntaCombo(self):
		sql_busca_pergunta = (" select p.cod_pergunta,"
						      " p.pergunta"
							  " from pergunta p")
		self.cursor.execute(sql_busca_pergunta)
		return self.cursor.fetchall()
        							  
	def novaResposta(self, resposta, cod_pergunta):
		sql_args = [resposta, cod_pergunta]
		sql_nova_resposta = ("insert into resposta"
							 "(resposta, cod_pergunta)"
							 " values (?,?)")
		self.cursor.execute(sql_nova_resposta, sql_args)
		self.conexao.commit()
	
	def atualizar_Resposta(self, resposta, cod_resposta):
		sql_args = [resposta, cod_resposta]
		sql_update_resposta = (" update resposta"
							   " set resposta = (?)"
							   " where cod_resposta = (?)")
							    
		self.cursor.execute(sql_update_resposta, sql_args)
		self.conexao.commit()
		
	def buscarResposta(self, filtro):
		sql_busca_resposta = (" select r.cod_pergunta,"
							  " p.pergunta,"
							  " r.cod_resposta,"
							  " r.resposta,"
							  " g.cod_gabarito"
							  " from resposta r"
							  " join pergunta p"
							  " on p.cod_pergunta = r.cod_pergunta"
							  " left join gabarito g"
							  " on r.cod_resposta = g.cod_resposta"
							  " where p.cod_pergunta = %s" % (filtro))
		self.cursor.execute(sql_busca_resposta)
		return self.cursor.fetchall()
    
	def apagarResposta(self, cod_resposta):
		for i in cod_resposta:
			sql_args = [i]
			sql_deletar_resposta = (" delete from resposta"
									" where cod_resposta in (?)")
			self.cursor.execute(sql_deletar_resposta, sql_args)
			self.conexao.commit()
	
	def vincularGabarito(self, cod_p, cod_r):
		sql_args = [cod_p, cod_r]
		
		sql_busca_gabarito = (" select cod_gabarito,"
							  " cod_resposta,"
							  " cod_pergunta"
							  " from gabarito"
							  " where cod_pergunta ="
							  " %s" % (cod_p))
		
		self.cursor.execute(sql_busca_gabarito)
		if self.cursor.fetchall() == []:
			sql_novo_gabarito = (" insert into gabarito"
								 " (cod_pergunta, cod_resposta)"
								 " values (?, ?)")
			self.cursor.execute(sql_novo_gabarito, sql_args) 
			self.conexao.commit()
		
		else:
			sql_deletar_gabarito = (" delete from gabarito"
								    " where cod_pergunta = (?)")
			self.cursor.execute(sql_deletar_gabarito, [sql_args[0]])
			self.conexao.commit()
		
#----------------------------------------------------------------------------------------------------------------------#
                                                                                           #Relatórios
#----------------------------------------------------------------------------------------------------------------------#
	def relatorio_resultado(self, dh_inicial, dh_final):		
		sql_relatorio = (" select cod_pergunta,"
						 " correta,"
						 " data_registro"
						 " from resultado"
						 " where data_registro"
						 " between '{}'"
						 " and '{}'".format(dh_inicial, dh_final))
						 
		self.cursor.execute(sql_relatorio)
		return self.cursor.fetchall()

	def soma_resposta_correta(self, dh_inicial, dh_final):
		sql_soma_resposta_correta = (" select count(correta)"
									 " from resultado"
									 " where correta = 'S'"
									 " and data_registro"
									 " between '{}'"
									 " and '{}'".format(dh_inicial,
													    dh_final))
		self.cursor.execute(sql_soma_resposta_correta)
		busca = self.cursor.fetchall()[0][0]
		dados = "Repostas corretas: {}".format(busca)
		return dados
	
	def soma_resposta_incorreta(self, dh_inicial, dh_final):
		sql_soma_resposta_correta = (" select count(correta)"
									 " from resultado"
									 " where correta = 'N'"
									 " and data_registro"
									 " between '{}'"
									 " and '{}'".format(dh_inicial,
													    dh_final))
		self.cursor.execute(sql_soma_resposta_correta)
		busca = self.cursor.fetchall()[0][0]
		dados = "Repostas incorreta: {}".format(busca)
		return dados
