#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gi
import sqlite3
import zlib
import datetime
testing = True

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from engineers.mikeUtil import MikeGtk
from widgets.widgets_quiz21 import WidgetsConstructor
from model.model_quiz21 import sql
from test import UnitTest

builder = Gtk.Builder()

#----------------------------------------------------------------------------------------------------------------------#

class Handler(MikeGtk, WidgetsConstructor, UnitTest):
    def __init__(self, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)
        # >> Estilo e persolanização
        self.screen = Gdk.Screen()
        self.style_app(os.path.join("static/estilos.css"), self.screen)
        
        # >>  -- Uso Global -- << #
        
        # >> Conexão com o Banco de Dados << #
        self.conexao = sqlite3.connect(os.path.join("banco.db"))
        self.conexao = sqlite3.connect(os.path.join("banco.db"))
        self.cursor = self.conexao.cursor()
        self.bd = sql()
        
        # >> id das perguntas selecionadas
        self.id_pergunta = []
        
        # >> id das categorias selecionadas
        self.id_categoria = []
        
        # >> id da reposta selecionada
        self.id_resposta = []
        
        # >> conta pergunta selecionada (jogo)
        self.id_pergunta_selec = []
        
        # >> Inicia a execução dos Widgets
        self.startWidgets(builder, os.path.join("interface/interface.glade"))
        
    #Destroy Tela ao fechar
    def on_janelaPrincipal_destroy(self, *args):
        try:
            Gtk.main_quit()
            if testing == True:
                self.unitTestchecklog()
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
                                
    def btnGerenciar(self, *args):
        try:
            self.Stack.set_visible_child_name("viewGerenciar")
            if testing == True:
                param = self.Stack.props.visible_child_name
                self.unitTestbtnGerenciar(param, "btnGerenciar")
            
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
    
    def btnGerenciarPerguntas(self, *args):
        try:
            # >> Limpa a ComboBox Categoria
            self.lst_combo_categoria.clear()
            self.lst_combo_categoria.append(self.op_categoria_default)
            self.cmb_categoria.set_active(0)
        
            # >> Realiza a busca da categoria
            sql_busca_categoria = (" select cod_categoria, categoria"
                                   " from categoria")
            
            self.cursor.execute(sql_busca_categoria)
            for i in self.cursor.fetchall():
                cod = i[0]
                categoria = i[1]
                lst_categoria = (cod, categoria)
                self.lst_combo_categoria.append(lst_categoria)
            
            self.Stack.set_visible_child_name("viewPergunta")
            
            if testing == True:
                param = self.Stack.props.visible_child_name
                self.unitTestGerenciarPerguntas(param, "btnGerenciarPerguntas")
            
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
    
    def btnGerenciarRespostas(self, *args):
        try:
            busca_pergunta = self.bd.buscarPerguntaCombo()
            if busca_pergunta != []:
                self.lst_cmb_pergunta.clear()
                self.lst_cmb_pergunta.append(self.op_pergunta_default)
                self.cmb_pergunta.set_active(0)
                self.Stack.set_visible_child_name("viewResposta")
                for i in busca_pergunta:
                    cod_pergunta = i[0]
                    pergunta = str(i[0]) + " - " + i[1]
                    lst_pergunta = (cod_pergunta, pergunta)
                    self.lst_cmb_pergunta.append(lst_pergunta)
                    
            else:
                self.simple_msg_box(self.msg_dialog, "Atenção",
                                ("Não existe perguntas cadastradas\n"
                                 "Cadastre as perguntas e retorne "
                                 "neste menu"))
                return
            
            if testing == True:
                param = self.Stack.props.visible_child_name
                self.unitTestbtnGerenciarRespostas(param, "btnGerenciarRespostas")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
                                "Erro ao selecionar perguntas "
                                "%s" % (str(ex)))
        
    def btnGerenciarCategorias(self, *args):
        try:
            self.Stack.set_visible_child_name("viewCategoria")
            if testing == True:
                param = self.Stack.props.visible_child_name
                self.unitTestbtnGerenciarCategorias(param, "btnGerenciarCategorias")
            
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
            
#----------------------------------------------------------------------------------------------------------------------#
                                                                                            #Tela Cadastrar Pergunta
#----------------------------------------------------------------------------------------------------------------------#

    #Botão Incluir
    def btnNovoPergunta(self, *args):
        try:
            combo = self.cmb_categoria
            pergunta = self.entryPergunta.get_text()
            categoria = combo.get_model()[combo.get_active()][1]
            cod_categoria = combo.get_model()[combo.get_active()][0]
            arquivo = self.selecionar_imagem.get_filename()
            with open(arquivo, "rb") as imagem:
                img_zip = zlib.compress(imagem.read(), 9)
                
            if combo.get_active() == 0:
                self.simple_msg_box(self.msg_dialog, "Atenção!",
                                ("É obrigatório informar a categoria"))
                                
            else:
                self.bd.inserirPergunta(pergunta, cod_categoria, img_zip)
                self.simple_msg_box(self.msg_dialog, "Sucesso!",
                                    "Pergunta cadastrada com sucesso!")
                
            # >> Atualiza a grade
            sql_busca = (" select p.cod_pergunta, p.pergunta,"
                         " c.categoria "
                         " from pergunta p"
                         " join categoria c"
                         " on p.cod_categoria = c.cod_categoria")
            
            self.cursor.execute(sql_busca)
            busca_pergunta = self.cursor.fetchall()
            self.lstPergunta.clear()
            for perguntas in busca_pergunta:
                selecao = False
                id = perguntas[0]
                pergunta = perguntas[1]
                categoria = perguntas[2]
                lista_pergunta = (selecao, id, pergunta, categoria)
                self.lstPergunta.append(lista_pergunta)
            
            if testing == True:
                param = self.lstPergunta
                self.unitTestbtnNovoPergunta(param, "btnNovoPergunta")
            
        except Exception as ex:
            print(str(ex))
            self.simple_msg_box(self.msg_dialog, "Erro",
                                ("Erro ao incluir a pergunta %s"
                                    % (str(ex))))
                                    
    #Botão Alterar
    def btnAlterarPergunta(self, *args):
        # >> verifica se existe a pergunta selecionada
        # >> caso exista é chamada a janela de atualização do registro
        try:
            if len(self.id_pergunta) > 0:
                cod_alteracao = self.id_pergunta[0]
                titulo = ("Alterar pergunta código %s" %
                            (cod_alteracao))
                sub_titulo = ("Descrição pergunta:")
                self.lb_titulo_alteracao.set_text(titulo)
                self.lb_cod_reg_alter.set_text(sub_titulo)
                self.new_window_main(self.janela_alteracao,
                                    self.main_window, True, False, False)
    
            else:
                self.simple_msg_box(self.msg_dialog, "Atenção!",
                                    ("É necessário selecionar uma"
                                     " pergunta para realizar"
                                     " atualização"))
            if testing == True:
                param = self.id_pergunta
                self.unitTestbtnAlterarPergunta(param, "btnAlterarPergunta")
            
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
            
    #Botão Buscar
    def btnBuscarPergunta(self, *args):
        try:
            # >> reseta a lista para receber novo valor
            self.lstPergunta.clear()
            # >> define um filtro de pesquisa
            filtro = self.entryPergunta.get_text()
            # >> realiza a busca
            busca = self.bd.buscarPergunta(filtro)
            # >> exibe o resultado na grade
            for retorno in busca:
                selecao = False
                cod_pergunta = retorno[0]
                pergunta = retorno[1]
                categoria = retorno[2]				
                lst_busca_pergunta = (selecao, cod_pergunta, pergunta,
                                        categoria)
                self.lstPergunta.append(lst_busca_pergunta)
        
            if testing == True:
                param = busca
                self.unitTestbtnBuscarPergunta(param, "btnBuscarPergunta")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
                                ("Erro ao realizar pesquisa"
                                " %s") % (str(ex)))
            
    #Botão Excluir
    def btnExcluirPergunta(self, *args):
        try:
            if self.id_pergunta != []:
                self.bd.apagarPergunta(self.id_pergunta)
                self.atualizar_grade_pergunta()
                self.simple_msg_box(self.msg_dialog, "Sucesso!",
                                    "Registro exclíudo com sucesso!")
            else:
                self.simple_msg_box(self.msg_dialog, "Atenção!",
                                    "É necessário selecionar"
                                    " o registro para excluir!")
                                                    
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
                                "Erro ao excluir %s" % (str(ex)))
                                
        finally:
            self.atualizar_grade_pergunta()
            self.id_pergunta = []
            if testing == True:
                param = self.id_pergunta
                self.unitTestbtnExcluirPergunta(param, "btnExcluirPergunta")
    
    def ao_selecionar_pergunta(self, *args):
        try:
            
            # >> Define as colunas existentes na Grade
            coluna = {"selecao": 0, "id": 1, "pergunta": 2}
            
            # >> Pega a linha selecionada
            linha = args[1]
            
            # >> Define as regras de valor default e novo valor para seleção
            valor_default = False
            novo_valor = True
            
            # >> Instancia da Treeview 
            grade = self.grade_pergunta
            
            # >> Retorna o status da seleção atual
            status_selecao = grade.get_model()[linha][coluna["selecao"]]
            
            if status_selecao == valor_default:
                # >> Caso o valor da seleção seja igual ao default é setado o novo valor
                grade.get_model()[linha][coluna["selecao"]] = novo_valor
                
                # >> Retorna o id da pergunta selecionada
                self.id_pergunta.append(grade.get_model()
                                        [linha][coluna["id"]])
        
            else:
                # Caso seja removido a seleção é setado o valor default
                grade.get_model()[linha][coluna["selecao"]] = valor_default
                
                # >> Remove o id da pergunta selecionada
                self.id_pergunta.remove(grade.get_model()
                                        [linha][coluna["id"]])
            
            if testing == True:
                param = self.id_pergunta
                self.unitTest_ao_selecionar_pergunta(param, "ao_selecionar_pergunta")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
            
    #Botão Voltar
    def btnVoltarPergunta(self, *args):
        try:
            self.Stack.set_visible_child_name("viewInicio")
            if testing == True:
                param = self.Stack.props.visible_child_name
                self.unitTestbtnVoltarPergunta(param, "btnVoltarPergunta")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
#----------------------------------------------------------------------------------------------------------------------#
                                                                                            #Tela Cadastro Categoria
#----------------------------------------------------------------------------------------------------------------------#

	#Botão Incluir
    def btnNovoCategoria(self, button):
        try:
            categoria = self.entryCategoria.get_text()
            if categoria != "":
                self.bd.inserirCategoria(categoria)
                self.simple_msg_box(self.msg_dialog, "Sucesso!",
                                    ("Categoria cadastrada "
                                        "com sucesso!"))
            else:
                self.simple_msg_box(self.msg_dialog, "Atenção!",
                                    ("Não é possível inserir valores "
                                        "nullos!"))
            if testing == True:
                param = categoria
                self.unitTestbtnNovoCategoria(param, "btnNovoCategoria")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
                                ("Erro ao incluir categoria %s"
                                    % (str(ex))))
                                    
    def ao_selecionar_categoria(self, *args):
        try:
            # >> Define as colunas existentes na Grade
            coluna = {"selecao": 0, "id": 1, "categoria": 2}
            
            # >> Pega a linha selecionada
            linha = args[1]
            
            # >> Define as regras de valor default e novo valor para seleção
            valor_default = False
            novo_valor = True
            
            # >> Instancia da Treeview 
            grade = self.grade_categoria
            
            # >> Retorna o status da seleção atual
            status_selecao = grade.get_model()[linha][coluna["selecao"]]
            
            if status_selecao == valor_default:
                # >> Caso o valor da seleção seja igual ao default é setado o novo valor
                grade.get_model()[linha][coluna["selecao"]] = novo_valor
                
                # >> Retorna o id da pergunta selecionada
                self.id_categoria.append(grade.get_model()
                                            [linha][coluna["id"]])
        
            else:
                # Caso seja removido a seleção é setado o valor default
                grade.get_model()[linha][coluna["selecao"]] = valor_default
                
                # >> Remove o id da pergunta selecionada
                self.id_categoria.remove(grade.get_model()
                                            [linha][coluna["id"]])
            
            if testing == True:
                param = self.id_categoria
                self.unitTest_ao_selecionar_categoria(param, "ao_selecionar_categoria")
            
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
                                
    #Botão Alterar
    def btnAlterarCategoria(self, button):
        try:
                
            # >> verifica se existe a pergunta selecionada
            # >> caso exista é chamada a janela de atualização do registro
            if self.id_categoria != []:
                cod_alteracao = self.id_categoria[0]
                titulo = ("Alterar categoria código: %s" %
                            (cod_alteracao))
                sub_titulo = ("Descrição categoria:")
                self.lb_titulo_alteracao.set_text(titulo)
                self.lb_cod_reg_alter.set_text(sub_titulo)
                self.new_window_main(self.janela_alteracao,
                                        self.main_window, True, False, False)
            else:
                self.simple_msg_box(self.msg_dialog, "Atenção!",
                                    ("É necessário selecionar uma"
                                     " pergunta para realizar"
                                     " atualização"))
            
            if testing == True:
                param = self.id_categoria
                self.unitTestbtnAlterarCategoria(param, "ao_selecionar_categoria")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
            
    #Botão Buscar
    def btnBuscarCategoria(self, *args):
        try:
            # >> reseta a lista para receber novo valor
            self.lstCategoria.clear()
            # >> define um filtro de pesquisa
            filtro = self.entryCategoria.get_text()
            # >> realiza a busca
            busca = self.bd.buscarCategoria(filtro)
            # >> exibe o resultado na grade
            for retorno in busca:
                selecao = False
                cod_categoria = retorno[0]
                categoria = retorno[1]		
                lst_busca_categoria = (selecao, cod_categoria, categoria)
                self.lstCategoria.append(lst_busca_categoria)
            
            if testing == True:
                param = busca
                self.unitTestbtnBuscarCategoria(param, "btnBuscarCategoria")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
                                ("Erro ao realizar pesquisa"
                                 " %s") % (str(ex)))
        
    #Botão Excluir
    def btnExcluirCategoria(self, button):
        try:
            if self.id_categoria != []:
                self.bd.apagarCategoria(self.id_categoria)
                self.atualizar_grade_categoria()
                self.simple_msg_box(self.msg_dialog, "Sucesso!",
                                    "Registro exclíudo com sucesso!")
            else:
                self.simple_msg_box(self.msg_dialog, "Atenção!",
                                    "É necessário selecionar"
                                    " o registro para excluir!")
                                    
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
                                "Erro ao excluir %s" % (str(ex)))
                                
        finally:
            self.atualizar_grade_categoria()
            self.id_categoria = []
            if testing == True:
                param = self.id_categoria
                self.unitTestbtnExcluirCategoria(param, "btnExcluirCategoria")
    
    #Botão Voltar
    def btnVoltarCategoria(self, button):
        try:
            self.Stack.set_visible_child_name("viewInicio")
            if testing == True:
                param = self.Stack.props.visible_child_name
                self.unitTestbtnVoltarCategoria(param, "btnVoltarCategoria")
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
            
#----------------------------------------------------------------------------------------------------------------------#
                                                                                            #Tela Cadastro Resposta
#----------------------------------------------------------------------------------------------------------------------#
	# >> Ao filtrar uma pergunta na ComboBox preenche as respostas
    def on_cmb_pergunta_changed(self, *args):
        try:
            combo = self.cmb_pergunta
            
            if combo.get_active() == -1:
                return
    
            else:
                self.lstResposta.clear()
                cod_pergunta = combo.get_model()[combo.get_active()][0]
                busca_resposta = self.bd.buscarResposta(cod_pergunta)
                self.atualizar_grade_resposta(cod_pergunta)
                
                if testing == True:
                    param = cod_pergunta
                    self.unitTest_on_cmb_pergunta_changed(param, "on_cmb_pergunta_changed")
                    
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
                                "Erro ao realizar a busca"
                                " da respostas %s" % (str(ex)))
            
    #Botão Incluir
    def btnNovoResposta(self, *args):
        try:
            # >> dados para inserção
            combo = self.cmb_pergunta
            cod_pergunta = combo.get_model()[combo.get_active()][0]
            resposta = self.entryResposta.get_text()
            
            # >> tratamento para possível preenchimento incorreto
            if combo.get_active() == 0:
                self.simple_msg_box(self.msg_dialog, "Atenção",
                                    ("É necessário selecionar uma "
                                        "pergunta\nPara vincular uma "
                                        "resposta"))
                return
                
            elif resposta == '':
                self.simple_msg_box(self.msg_dialog, "Atenção",
                                ("Não é possível cadastrar uma"
                                    "resposta nula"))
                return
            
            else:
                self.bd.novaResposta(resposta, cod_pergunta)
                self.simple_msg_box(self.msg_dialog, "Sucesso!",
                                    "Reposta cadastrada com sucesso!")
                self.atualizar_grade_resposta(cod_pergunta)
            
            if testing == True:
                param = resposta
                self.unitTestbtnNovoResposta(param, "btnNovoResposta")
            
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro!",
                                    ("Erro ao cadastrar resposta\n!"
                                    "%s" % str(ex)))
    
    def ao_selecionar_resposta(self, *args):
        try:
            # >> Define referencia para as colunas existentes na Grade
            coluna = {"selecao": 0, "cod_pergunta": 1, "pergunta": 2,
                    "cod_resposta": 3, "resposta": 4, "gabarito": 5}
            
            # >> Pega a linha selecionada
            linha = args[1]
            
            # >> Define as regras de valor default e novo valor para seleção
            valor_default = False
            novo_valor = True
            
            # >> Instancia da Treeview 
            grade = self.grade_resposta
            
            # >> Retorna o status da seleção atual
            status_selecao = grade.get_model()[linha][coluna["selecao"]]
            
            if status_selecao == valor_default:
                # >> Caso o valor da seleção seja igual ao default é setado o novo valor
                grade.get_model()[linha][coluna["selecao"]] = novo_valor
                            
                # >> Retorna o id da resposta selecionada
                self.id_resposta.append(grade.get_model()
                                        [linha][coluna["cod_resposta"]])
        
            else:
                # Caso seja removido a seleção é setado o valor default
                grade.get_model()[linha][coluna["selecao"]] = valor_default
                
                # >> Remove o id da resposta selecionada
                self.id_resposta.remove(grade.get_model()
                                        [linha][coluna["cod_resposta"]])
            
            if testing == True:
                param = self.id_resposta
                self.unitTest_ao_selecionar_resposta(param, "ao_selecionar_categoria")
        
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
            
        
    def ao_selecionar_resposta_gabarito(self, *args):
        try:
            # >> Define referencia para as colunas existentes na Grade
            coluna = {"selecao": 0, "cod_pergunta": 1, "pergunta": 2,
                      "cod_resposta": 3, "resposta": 4, "gabarito": 5}
            
            # >> Pega a linha selecionada
            linha = args[1]
            
            # >> Define as regras de valor default e novo valor para seleção
            valor_default = False
            novo_valor = True
            
            # >> Instancia da Treeview 
            grade = self.grade_resposta
            
            # >> Váriaveis para vincular resposta ao gabarito
            cod_perg = grade.get_model()[linha][coluna["cod_pergunta"]]
            cod_resp = grade.get_model()[linha][coluna["cod_resposta"]]
            
            # >> Retorna o status da seleção atual
            status_selecao = grade.get_model()[linha][coluna["gabarito"]]
            
            if status_selecao == valor_default:
                # >> Caso o valor da seleção seja igual ao default é setado o novo valor
                grade.get_model()[linha][coluna["gabarito"]] = novo_valor
                
                try:
                    self.bd.vincularGabarito(cod_perg, cod_resp)
                
                except Exception as ex:
                    self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
                
            else:
                # Caso seja removido a seleção é setado o valor default
                grade.get_model()[linha][coluna["gabarito"]] = valor_default
                try:
                    self.bd.vincularGabarito(cod_perg, cod_resp)
                
                except Exception as ex:
                    self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
            
            if testing == True:
                param = [cod_perg, cod_resp]
                self.unitTest_ao_selecionar_resposta_gabarito(param, "ao_selecionar_resposta_gabarito")
        
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
                                
    def btnAlterarResposta(self, *args):
        try:
            if self.id_resposta != []:
                cod_alteracao = self.id_resposta[0]
                titulo = ("Alterar resposta código: %s" %
                            (cod_alteracao))
                sub_titulo = ("Descrição resposta:")
                self.lb_titulo_alteracao.set_text(titulo)
                self.lb_cod_reg_alter.set_text(sub_titulo)
                self.new_window_main(self.janela_alteracao,
                                        self.main_window, True, False,
                                        False)
            else:
                self.simple_msg_box(self.msg_dialog, "Atenção!",
                                    ("É necessário selecionar uma"
                                        " resposta para realizar"
                                        " atualização"))
            if testing == True:
                param = self.id_resposta
                self.unitTestbtnAlterarResposta(param, "btnAlterarResposta")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro!",
                                    ("Erro ao selecionar resposta\n!"
                                    "%s" % str(ex)))
                                    
    def btnExcluirResposta(self, *args):
        try:
            
            if self.id_resposta != []:
                self.bd.apagarResposta(self.id_resposta)
                self.simple_msg_box(self.msg_dialog, "Sucesso!",
                                    "Registro exclíudo com sucesso!")
            else:
                self.simple_msg_box(self.msg_dialog, "Atenção!",
                                    "É necessário selecionar"
                                    " o registro para excluir!")

        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
                                "Erro ao excluir %s" % (str(ex)))
        
        finally:
            self.id_resposta = []
            if testing == True:
                param = self.id_resposta
                self.unitTestbtnExcluirResposta(param, "btnExcluirResposta")
            
    #Botão Voltar
    def btnVoltarResposta(self, button):
        try:
            self.Stack.set_visible_child_name("viewInicio")
            if testing == True:
                param = self.Stack.props.visible_child_name
                self.unitTestbtnVoltarResposta(param, "btnVoltarResposta")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
            
#----------------------------------------------------View Config Jogo--------------------------------------------------#
    def btnJogar(self, *args):
        try:
            self.Stack.set_visible_child_name("viewConfig")
            
            if testing == True:
                param = self.Stack.props.visible_child_name
                self.unitTestbtnJogar(param, "viewConfig")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
        
    def ao_selecionar_pergunta_jogo(self, *args):
        try:
            # >> Define as colunas existentes na Grade
            coluna = {"selecao": 0, "id": 1, "pergunta": 2, "categoria": 3}
            
            # >> Pega a linha selecionada
            linha = args[1]
            
            # >> Define as regras de valor default e novo valor para seleção
            valor_default = False
            novo_valor = True
            
            # >> Instancia da Treeview 
            grade = self.grade_selecao_jogo
            
            # >> Retorna o status da seleção atual
            status_selecao = grade.get_model()[linha][coluna["selecao"]]
            
            if status_selecao == valor_default:
                # >> Caso o valor da seleção seja igual ao default é setado o novo valor
                grade.get_model()[linha][coluna["selecao"]] = novo_valor
                
                # >> Retorna o id da pergunta selecionada
                self.id_pergunta_selec.append(grade.get_model()
                                                    [linha][coluna["id"]])
                                                    
            else:
                # Caso seja removido a seleção é setado o valor default
                grade.get_model()[linha][coluna["selecao"]] = valor_default
                
                # >> Remove o id da pergunta selecionada
                self.id_pergunta_selec.remove(grade.get_model()
                                                [linha][coluna["id"]])
            
            if testing == True:
                param = self.id_pergunta_selec
                self.unitTest_ao_selecionar_pergunta_jogo(param, "ao_selecionar_pergunta_jogo")
            
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
            
    def ao_clicar_buscar_pergunta_jogo(self, *args):
        try:
            # >> reseta a lista para receber novo valor
            self.lst_selecao_jogo.clear()
            # >> define um filtro de pesquisa
            filtro = self.tx_busca_pergunta.get_text()
            # >> realiza a busca
            busca = self.bd.buscarPergunta(filtro)
            # >> exibe o resultado na grade
            for retorno in busca:
                selecao = False
                cod_pergunta = retorno[0]
                pergunta = retorno[1]
                categoria = retorno[2]				
                lst_busca_pergunta = (selecao, cod_pergunta, pergunta,
                                        categoria)
                self.lst_selecao_jogo.append(lst_busca_pergunta)
            
            if testing == True:
                param = busca
                self.unitTest_ao_clicar_buscar_pergunta_jogo(param, "ao_clicar_buscar_pergunta_jogo")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
                                ("Erro ao realizar pesquisa"
                                " %s") % (str(ex)))
    
    def ao_clicar_aplicar_jogo(self, *args):
        try:
            # >> Diretório para armazenamento das imagens das perguntas
            path_img_1 = "/home/rodrigues/Área de Trabalho/Quiz21-Desenvovilmento/images/1/img1.png"
            path_img_2 = "/home/rodrigues/Área de Trabalho/Quiz21-Desenvovilmento/images/2/img2.png"
            path_img_3 = "/home/rodrigues/Área de Trabalho/Quiz21-Desenvovilmento/images/3/img3.png"
            
            # >> Conta quantas perguntas estão selecionados
            qtd_pergunta = len(self.id_pergunta_selec)
            
            # >> Trata o número correto de perguntas selecionadas
            if qtd_pergunta < 3:
                self.simple_msg_box(self.msg_dialog, "Erro",
                                    ("Para iniciar o jogo é necessário\n"
                                    "selecionar 3 perguntas"))
                                    
            # >> Trata o número correto de perguntas selecionadas
            elif qtd_pergunta > 3:
                self.simple_msg_box(self.msg_dialog, "Erro",
                                    ("Para iniciar o jogo é necessário\n"
                                    "selecionar no máximo 3 perguntas"))
                                    
            # >> Trata o número correto de perguntas selecionadas
            elif qtd_pergunta == 3:
                
                # >> Recupera o código das perguntas selecionadas
                p1 = self.id_pergunta_selec[0]
                p2 = self.id_pergunta_selec[1]
                p3 = self.id_pergunta_selec[2]
            
            # # # # # # # # # # # # PERGUNTA 1 # # # # # # # # # # # # #
                # >> query busca pergunta 1
                sql_busca_p1 = (" select p.cod_pergunta,"
                                " p.pergunta,"
                                " p.imagem"
                                " from pergunta p"
                                " where p.cod_pergunta = %s" % (p1))
                
                # >> query busca resposta pergunta 1
                sql_resposta_p1 = (" select r.cod_resposta,"
                                    " r.resposta,"
                                    " r.cod_pergunta"
                                    " from resposta r"
                                    " where r.cod_pergunta = %s" % (p1))
    
                # >> Recupera a pergunta 1
                self.cursor.execute(sql_busca_p1)
                pergunta1 = self.cursor.fetchall()
                for i in pergunta1:
                    # >> seta a pergunta na Label da janela de Jogo
                    self.lb_pergunta_ab1.set_text(i[1])
                    # >> descompacta e recupera a imagem
                    with open(path_img_1, "wb") as file:
                        file.write(zlib.decompress(i[2]))
                
                # >> Recupera as respostas da pergunta 1
                self.cursor.execute(sql_resposta_p1)
                repostas_p1 = self.cursor.fetchall()
                
                # >> define o vetor da lista de respostas
                lst_resposta = []
                
                # - resposta 1
                for i in repostas_p1:
                    cod = i[0]
                    resposta = i[1]
                    cod_pergunta = i[2]
                    lst = (cod, resposta, cod_pergunta) 
                    lst_resposta.append(lst)
                
                # >> seta as respostas na label
                self.lb_r1_ab1.set_text(lst_resposta[0][1])
                self.lb_r2_ab1.set_text(lst_resposta[1][1])
                self.lb_r3_ab1.set_text(lst_resposta[2][1])
                
                # >> define as respostas no modelo da GtkListStored
                self.lst_r1_aba1.append(lst_resposta[0])
                self.lst_r2_aba1.append(lst_resposta[1])
                self.lst_r3_aba1.append(lst_resposta[2])
                
                # >> Seta a imagem da pergunta 1
                self.img_perg_ab1.set_from_file(path_img_1)
            
            # # # # # # # # # # # # PERGUNTA 2 # # # # # # # # # # # # #
            # >> query busca pergunta 2
                sql_busca_p2 = (" select p.cod_pergunta,"
                                " p.pergunta,"
                                " p.imagem"
                                " from pergunta p"
                                " where p.cod_pergunta = %s" % (p2))
                
                # >> query busca resposta pergunta 1
                sql_resposta_p2 = (" select r.cod_resposta,"
                                    " r.resposta,"
                                    " r.cod_pergunta"
                                    " from resposta r"
                                    " where r.cod_pergunta = %s" % (p2))
                
                # >> Recupera a pergunta 1
                self.cursor.execute(sql_busca_p2)
                pergunta2 = self.cursor.fetchall()
                for i in pergunta2:
                    # >> seta a pergunta na Label da janela de Jogo
                    self.lb_pergunta_ab2.set_text(i[1])
                    # >> descompacta e recupera a imagem
                    with open(path_img_2, "wb") as file:
                        file.write(zlib.decompress(i[2]))
                
                # >> Recupera as respostas da pergunta 1
                self.cursor.execute(sql_resposta_p2)
                repostas_p2 = self.cursor.fetchall()
                
                # >> define o vetor da lista de respostas
                lst_resposta_p2 = []
                
                # - resposta 1
                for i in repostas_p2:
                    cod = i[0]
                    resposta = i[1]
                    cod_pergunta = i[2]
                    lst = (cod, resposta, cod_pergunta) 
                    lst_resposta_p2.append(lst)
                
                # >> seta as respostas na label
                self.lb_r1_ab2.set_text(lst_resposta_p2[0][1])
                self.lb_r2_ab2.set_text(lst_resposta_p2[1][1])
                self.lb_r3_ab2.set_text(lst_resposta_p2[2][1])
                
                # >> define as respostas no modelo da GtkListStored
                self.lst_r1_aba2.append(lst_resposta_p2[0])
                self.lst_r2_aba2.append(lst_resposta_p2[1])
                self.lst_r3_aba2.append(lst_resposta_p2[2])
                
                # >> Seta a imagem da pergunta 2
                self.img_perg_ab2.set_from_file(path_img_2)
                
            # # # # # # # # # # # # PERGUNTA 3 # # # # # # # # # # # # #
            # >> query busca pergunta 3
                sql_busca_p3 = (" select p.cod_pergunta,"
                                " p.pergunta,"
                                " p.imagem"
                                " from pergunta p"
                                " where p.cod_pergunta = %s" % (p3))
                
                # >> query busca resposta pergunta 3
                sql_resposta_p3 = (" select r.cod_resposta,"
                                    " r.resposta,"
                                    " r.cod_resposta"
                                    " from resposta r"
                                    " where r.cod_pergunta = %s" % (p3))
                
                # >> Recupera a pergunta 3
                self.cursor.execute(sql_busca_p3)
                pergunta3 = self.cursor.fetchall()
                for i in pergunta3:
                    # >> seta a pergunta na Label da janela de Jogo
                    self.lb_pergunta_ab3.set_text(i[1])
                    # >> descompacta e recupera a imagem
                    with open(path_img_3, "wb") as file:
                        file.write(zlib.decompress(i[2]))
                
                # >> Recupera as respostas da pergunta 3
                self.cursor.execute(sql_resposta_p3)
                repostas_p3 = self.cursor.fetchall()
                
                # >> define o vetor da lista de respostas
                lst_resposta_p3 = []
                
                # - resposta 3
                for i in repostas_p3:
                    cod = i[0]
                    resposta = i[1]
                    cod_resposta = i[2]
                    lst = (cod, resposta, cod_pergunta) 
                    lst_resposta_p3.append(lst)
                
                # >> seta as respostas na label
                self.lb_r1_ab3.set_text(lst_resposta_p3[0][1])
                self.lb_r2_ab3.set_text(lst_resposta_p3[1][1])
                self.lb_r3_ab3.set_text(lst_resposta_p3[2][1])
                
                # >> define as respostas no modelo da GtkListStored
                self.lst_r1_aba3.append(lst_resposta_p3[0])
                self.lst_r2_aba3.append(lst_resposta_p3[1])
                self.lst_r3_aba3.append(lst_resposta_p3[2])
                
                # >> Seta a imagem da pergunta 3
                self.img_perg_ab3.set_from_file(path_img_3)
                
                # >> esconde a janela principal
                self.main_window.set_visible(False)
                
                # >> inicia a janela de jogar
                self.StackJogo.set_visible_child_name("view_primeira_resposta")
                self.new_window_main(self.janela_jogar,
                                        self.main_window, True)
            
            if testing == True:
                param = qtd_pergunta
                self.unitTest_ao_clicar_aplicar_jogo(param, "ao_clicar_aplicar_jogo")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
                                ("Erro ao iniciar jogo"
                                " %s") % (str(ex)))
    
    def ao_clicar_desfazer_jogo(self, *args):
        try:
            self.lst_selecao_jogo.clear()
            self.id_pergunta_selec = []
            self.grade_selecao_jogo.set_sensitive(True)
            self.Stack.set_visible_child_name("viewInicio")
            
            if testing == True:
                param = self.Stack.props.visible_child_name
                self.unitTest_ao_clicar_desfazer_jogo(param, "ao_clicar_desfazer_jogo")
        
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
#------------------------------------------View Jogo------------------------------------------------------------#
	
    def on_janela_jogar_delete_event(self, *args):
        try:
            self.main_window.set_visible(True)
            window = self.janela_jogar
            window.hide()
            return True
            
            if testing == True:
                param = True
                self.unitTest_on_janela_jogar_delete_event(param, "on_janela_jogar_delete_event")
        
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# >> Ao selecionar resposta -- A 
    def on_bt_r1_ab1_clicked(self, *args):
        try:
            # >> conteudo armazenado na resposta A aba 1
            model = self.lst_r1_aba1[0][0:]
            cod_resposta = model[0]
            cod_pergunta = model[2]
            
            sql_checa_resposta = (" select cod_gabarito,"
                                    " cod_resposta,"
                                    " cod_pergunta"
                                    " from gabarito"
                                    " where cod_resposta"
                                    " = %s" % (cod_resposta))
            self.cursor.execute(sql_checa_resposta)
            gabarito = self.cursor.fetchall()
            
            if gabarito == []:
                sql_args = [cod_pergunta, "N"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            else:
                sql_args = [cod_pergunta, "S"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
        
            self.StackJogo.set_visible_child_name("view_segunda_resposta")
            
            if testing == True:
                param = self.Stack.props.visible_child_name
                self.unitTest_on_bt_r1_ab1_clicked(param, "on_bt_r1_ab1_clicked")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
							   ("Erro ao gravar resposta\n"
							    "Contate o suporte!"
								" %s") % (str(ex)))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 	
	# >> Ao selecionar resposta -- B
    def on_bt_r2_ab1_clicked(self, *args):
        try:
            # >> conteudo armazenado na resposta A aba 1
            model = self.lst_r2_aba1[0][0:]
            cod_resposta = model[0]
            cod_pergunta = model[2]
            
            sql_checa_resposta = (" select cod_gabarito,"
                                    " cod_resposta,"
                                    " cod_pergunta"
                                    " from gabarito"
                                    " where cod_resposta"
                                    " = %s" % (cod_resposta))
            self.cursor.execute(sql_checa_resposta)
            gabarito = self.cursor.fetchall()
            
            if gabarito == []:
                sql_args = [cod_pergunta, "N"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            else:
                sql_args = [cod_pergunta, "S"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            self.StackJogo.set_visible_child_name("view_segunda_resposta")
            if testing == True:
                param = self.Stack.props.visible_child_name
                self.unitTest_on_bt_r2_ab1_clicked(param, "on_bt_r2_ab1_clicked")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
							   ("Erro ao gravar resposta\n"
							    "Contate o suporte!"
								" %s") % (str(ex)))
								
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# >> Ao selecionar resposta -- C 
    def on_bt_r3_ab1_clicked(self, *args):
        try:
            # >> conteudo armazenado na resposta A aba 1
            model = self.lst_r3_aba1[0][0:]
            cod_resposta = model[0]
            cod_pergunta = model[2]
            
            sql_checa_resposta = (" select cod_gabarito,"
                                    " cod_resposta,"
                                    " cod_pergunta"
                                    " from gabarito"
                                    " where cod_resposta"
                                    " = %s" % (cod_resposta))
            self.cursor.execute(sql_checa_resposta)
            gabarito = self.cursor.fetchall()
            
            if gabarito == []:
                sql_args = [cod_pergunta, "N"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            else:
                sql_args = [cod_pergunta, "S"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            self.StackJogo.set_visible_child_name("view_segunda_resposta")
            if testing == True:
                param = self.Stack.props.visible_child_name
                self.unitTest_on_bt_r3_ab1_clicked(param, "on_bt_r3_ab1_clicked")
        
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
							   ("Erro ao gravar resposta\n"
							    "Contate o suporte!"
								" %s") % (str(ex)))
								
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# >> Ao selecionar resposta -- A
    def on_bt_r1_ab2_clicked(self, *args):
        try:
            # >> conteudo armazenado na resposta A aba 1
            model = self.lst_r1_aba2[0][0:]
            cod_resposta = model[0]
            cod_pergunta = model[2]
            
            sql_checa_resposta = (" select cod_gabarito,"
                                    " cod_resposta,"
                                    " cod_pergunta"
                                    " from gabarito"
                                    " where cod_resposta"
                                    " = %s" % (cod_resposta))
            self.cursor.execute(sql_checa_resposta)
            gabarito = self.cursor.fetchall()
            
            if gabarito == []:
                sql_args = [cod_pergunta, "N"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            else:
                sql_args = [cod_pergunta, "S"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            self.StackJogo.set_visible_child_name("view_terceira_resposta")
            if testing == True:
                param = self.Stack.props.visible_child_name
                print(param)
                self.unitTest_on_bt_r1_ab2_clicked(param, "on_bt_r1_ab2_clicked")
        
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
                                ("Erro ao gravar resposta\n"
							    "Contate o suporte!"
								" %s") % (str(ex)))
								
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# >> Ao selecionar resposta -- B
    def on_bt_r2_ab2_clicked(self, *args):
        try:
            # >> conteudo armazenado na resposta A aba 1
            model = self.lst_r2_aba2[0][0:]
            cod_resposta = model[0]
            cod_pergunta = model[2]
            
            sql_checa_resposta = (" select cod_gabarito,"
                                    " cod_resposta,"
                                    " cod_pergunta"
                                    " from gabarito"
                                    " where cod_resposta"
                                    " = %s" % (cod_resposta))
            self.cursor.execute(sql_checa_resposta)
            gabarito = self.cursor.fetchall()
            
            if gabarito == []:
                sql_args = [cod_pergunta, "N"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            else:
                sql_args = [cod_pergunta, "S"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            self.StackJogo.set_visible_child_name("view_terceira_resposta")
            if testing == True:
                param = self.Stack.props.visible_child_name
                print(param)
                self.unitTest_on_bt_r2_ab2_clicked(param, "on_bt_r2_ab2_clicked")
        
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
							   ("Erro ao gravar resposta\n"
							    "Contate o suporte!"
								" %s") % (str(ex)))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # >> Ao selecionar resposta -- C
    def on_bt_r3_ab2_clicked(self, *args):
        try:
            # >> conteudo armazenado na resposta A aba 1
            model = self.lst_r3_aba2[0][0:]
            cod_resposta = model[0]
            cod_pergunta = model[2]
            
            sql_checa_resposta = (" select cod_gabarito,"
                                    " cod_resposta,"
                                    " cod_pergunta"
                                    " from gabarito"
                                    " where cod_resposta"
                                    " = %s" % (cod_resposta))
            self.cursor.execute(sql_checa_resposta)
            gabarito = self.cursor.fetchall()
            
            if gabarito == []:
                sql_args = [cod_pergunta, "N"]
                sql_registra_resultado = (" insert into resultado"
                                          " (cod_pergunta, correta)"
                                          " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            else:
                sql_args = [cod_pergunta, "S"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            self.StackJogo.set_visible_child_name("view_terceira_resposta")
            if testing == True:
                param = self.Stack.props.visible_child_name
                print(param)
                self.unitTest_on_bt_r3_ab2_clicked(param, "on_bt_r3_ab2_clicked")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
							   ("Erro ao gravar resposta\n"
							    "Contate o suporte!"
								" %s") % (str(ex)))
								
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# >> Ao selecionar resposta -- A
    def on_bt_r1_ab3_clicked(self, *args):
        try:
            # >> conteudo armazenado na resposta A aba 1
            model = self.lst_r1_aba3[0][0:]
            cod_resposta = model[0]
            cod_pergunta = model[2]
            
            sql_checa_resposta = (" select cod_gabarito,"
                                  " cod_resposta,"
                                  " cod_pergunta"
                                  " from gabarito"
                                  " where cod_resposta"
                                  " = %s" % (cod_resposta))
            self.cursor.execute(sql_checa_resposta)
            gabarito = self.cursor.fetchall()
            
            if gabarito == []:
                sql_args = [cod_pergunta, "N"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            else:
                sql_args = [cod_pergunta, "S"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            self.janela_jogar.set_visible(False)
            self.new_window_main(self.janela_parabens, self.main_window,
                                    True)
            
            if testing == True:
                param = self.janela_jogar.props.visible
                self.unitTest_on_bt_r1_ab3_clicked(param, "on_bt_r1_ab3_clicked")
                                            
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
                                ("Erro ao gravar resposta\n"
							    "Contate o suporte!"
								" %s") % (str(ex)))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# >> Ao selecionar resposta -- B
    def on_bt_r2_ab3_clicked(self, *args):
        try:
            # >> conteudo armazenado na resposta A aba 1
            model = self.lst_r2_aba3[0][0:]
            cod_resposta = model[0]
            cod_pergunta = model[2]
            
            sql_checa_resposta = (" select cod_gabarito,"
                                    " cod_resposta,"
                                    " cod_pergunta"
                                    " from gabarito"
                                    " where cod_resposta"
                                    " = %s" % (cod_resposta))
            self.cursor.execute(sql_checa_resposta)
            gabarito = self.cursor.fetchall()
            
            if gabarito == []:
                sql_args = [cod_pergunta, "N"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            else:
                sql_args = [cod_pergunta, "S"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            self.janela_jogar.set_visible(False)
            self.new_window_main(self.janela_parabens, self.main_window,
                                    True)
            
            if testing == True:
                param = self.janela_jogar.props.visible
                self.unitTest_on_bt_r2_ab3_clicked(param, "on_bt_r2_ab3_clicked")
            
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
                                ("Erro ao gravar resposta\n"
							    "Contate o suporte!"
								" %s") % (str(ex)))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# >> Ao selecionar resposta -- C
    def on_bt_r3_ab3_clicked(self, *args):
        try:
            # >> conteudo armazenado na resposta A aba 1
            model = self.lst_r3_aba3[0][0:]
            cod_resposta = model[0]
            cod_pergunta = model[2]
            
            sql_checa_resposta = (" select cod_gabarito,"
                                    " cod_resposta,"
                                    " cod_pergunta"
                                    " from gabarito"
                                    " where cod_resposta"
                                    " = %s" % (cod_resposta))
            self.cursor.execute(sql_checa_resposta)
            gabarito = self.cursor.fetchall()
            
            if gabarito == []:
                sql_args = [cod_pergunta, "N"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            else:
                sql_args = [cod_pergunta, "S"]
                sql_registra_resultado = (" insert into resultado"
                                            " (cod_pergunta, correta)"
                                            " values (?, ?)")
                self.cursor.execute(sql_registra_resultado, sql_args)
                self.conexao.commit()
            
            self.janela_jogar.set_visible(False)
            self.new_window_main(self.janela_parabens, self.main_window,
                                    True)
            
            if testing == True:
                param = self.janela_jogar.props.visible
                self.unitTest_on_bt_r3_ab3_clicked(param, "on_bt_r3_ab3_clicked")
                                            
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro",
							   ("Erro ao gravar resposta\n"
							    "Contate o suporte!"
								" %s") % (str(ex)))
								
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#--------------------------------------- Janela Parabens -------------------------------------------------------#
    def on_bt_retornar_clicked(self, *args):
        try:
            self.main_window.set_visible(True)
            window = self.janela_parabens
            window.hide()
            return True
            if testing == True:
                self.on_bt_retornar_clicked(True, "on_bt_retornar_clicked")
            
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
        
		
#--------------------------------------- View Relatorio --------------------------------------------------------#
    def on_bt_voltar_view_relatorio_clicked(self, *args):
        try:
            self.Stack.set_visible_child_name("viewInicio")
            self.lst_relatorio.clear()
            self.entry_dh_inicial.set_text("")
            self.entry_dh_final.set_text("")
            
            if testing == True:
                param = self.Stack.props.visible_child_name
                self.unitTest_on_bt_voltar_view_relatorio_clicked(param, "on_bt_voltar_view_relatorio_clicked")
            
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
    
    def on_btnGerenciarRelatorios_clicked(self, *args):
        try:
            self.Stack.set_visible_child_name("view_relatorio")
            hoje = self.data_hoje_formatada()
            self.entry_dh_inicial.set_text(hoje)
            self.entry_dh_final.set_text(hoje)
            
            if testing == True:
                param = self.Stack.props.visible_child_name
                self.unitTest_on_btnGerenciarRelatorios_clicked(param, "on_bt_voltar_view_relatorio_clicked")
        
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
    
    def on_bt_buscar_relatorio_clicked(self, *args):
        try:
            self.lst_relatorio.clear()
            d_ini = self.entry_dh_inicial.get_text().split("/")[0]
            m_ini = self.entry_dh_inicial.get_text().split("/")[1]
            a_ini = self.entry_dh_inicial.get_text().split("/")[2]
            dt_ini_formatada = (a_ini + "-" + m_ini + "-" + d_ini)
            
            d_fim = self.entry_dh_final.get_text().split("/")[0]
            m_fim = self.entry_dh_final.get_text().split("/")[1]
            a_fim = self.entry_dh_final.get_text().split("/")[2]
            
            dt_fim_formatada = (a_fim + "-" + m_fim + "-" + d_fim)
            
            busca = self.bd.relatorio_resultado(dt_ini_formatada,
												dt_fim_formatada)
			
            for i in busca:
                cod_pergunta = i[0]
                correta = i[1]
                data_reg = i[2]
                lst = (cod_pergunta, correta, data_reg)
                self.lst_relatorio.append(lst)
            
            resp_ok = self.bd.soma_resposta_correta(dt_ini_formatada,
                                                    dt_fim_formatada)
            resp_no = self.bd.soma_resposta_incorreta(dt_ini_formatada,
                                                        dt_fim_formatada)										
            self.lb_count_correta.set_text(resp_ok)
            self.lb_count_incorreta.set_text(resp_no)
            
            if testing == True:
                param = busca
                self.unitTest_on_bt_buscar_relatorio_clicked(param, "on_bt_buscar_relatorio_clicked")
            
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro!",
									("Erro ao gerar relatório\n"
									 "%s") % (str(ex)))
			
#--------------------------------------- multi uso -------------------------------------------------------------#
	
    def data_hoje_formatada(self, *args):
        try:
            dh_hoje = datetime.date.today()
            dh_hoje_formatada = ("{}/{}/{}").format("0" + str(dh_hoje.day) if int(dh_hoje.day) < 10 else str(dh_hoje.day),
                                                "0" + str(dh_hoje.month) if int(dh_hoje.month) < 10 else str(dh_hoje.month),
                                                dh_hoje.year)
            return dh_hoje_formatada
            
            if testing == True:
                param = dh_hoje_formatada
                self.unitTest_data_hoje_formatada(param, "data_hoje_formatada")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
        
    def atualizar_grade_pergunta(self, *args):
        try:
            sql_busca = (" select p.cod_pergunta, p.pergunta,"
                        " c.categoria "
                        " from pergunta p"
                        " join categoria c"
                        " on p.cod_categoria = c.cod_categoria")
            self.cursor.execute(sql_busca)
            busca_pergunta = self.cursor.fetchall()
            self.lstPergunta.clear()
            for perguntas in busca_pergunta:
                selecao = False
                id = perguntas[0]
                pergunta = perguntas[1]
                categoria = perguntas[2]
                lista_pergunta = (selecao, id, pergunta, categoria)
                self.lstPergunta.append(lista_pergunta)
            
            if testing == True:
                param = busca_pergunta
                self.unitTest_atualizar_grade_pergunta(param, "atualizar_grade_pergunta")
        
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
        
    
    def atualizar_grade_resposta(self, cod_registro):
        try:
            busca_resposta = self.bd.buscarResposta(cod_registro)
            self.lstResposta.clear()
            for i in busca_resposta:
                selec_reg = False
                cod_perg = i[0]
                perg = i[1]
                cod_resp = i[2]
                resp = i[3]
                gab = False if i[4] == None else True
                lst_respostas = (selec_reg, cod_perg, perg, cod_resp,
                                    resp, gab)
                self.lstResposta.append(lst_respostas)
            
            if testing == True:
                param = busca_resposta
                self.unitTest_atualizar_grade_resposta(param, "atualizar_grade_resposta")
            
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
    
    def atualizar_grade_categoria(self, *args):
        try:
            sql_busca = "select * from categoria"
            self.cursor.execute(sql_busca)
            busca_categoria = self.cursor.fetchall()
            self.lstCategoria.clear()
            for categoria in busca_categoria:
                selecao = False
                id = categoria[0]
                categoria = categoria[1]
                lista_categoria = (selecao, id, categoria)
                self.lstCategoria.append(lista_categoria)
            
            if testing == True:
                param = busca_categoria
                self.unitTest_atualizar_grade_categoria(param, "atualizar_grade_categoria")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
    
    # >> Encerra a execução da janela altear gabarito
    def on_janela_vincular_gabarito_delete_event(self, *args):
        try:
            window = self.janela_vincular_gabarito
            window.destroy()
            return True
            
            if testing == True:
                param = True
                self.unitTest_on_janela_vincular_gabarito_delete_event(param, "on_janela_vincular_gabarito_delete_event")
        
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
    
    # >> Encerra a execução da janela multi-alteração
    def ao_sair_janela_alteracao(self, *args):
        try:
            window = self.janela_alteracao
            window.hide()
            return True
            
            if testing == True:
                param = True
                self.unitTest_ao_sair_janela_alteracao(param, "ao_sair_janela_alteracao")
            
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
                                
    def ao_clicar_salvar_alteracao(self, *args):
        opcao = ["pergunta", "categoria", "resposta"]
        operacao = self.lb_titulo_alteracao.get_text().split()[1]
        cod_registro = self.lb_titulo_alteracao.get_text().split()[3]
        descricao = self.entry_texto_alter.get_text()
        try:
            if operacao == opcao[0]:
                self.bd.atualizarPergunta(descricao, cod_registro)
                self.simple_msg_box(self.msg_dialog, "Sucesso!",
                                    ("Pergunta atualizada "
                                     "com sucesso!"))
                self.atualizar_grade_pergunta()
                self.id_pergunta = []
                window = self.janela_alteracao
                window.hide()
                return True
                
            elif operacao == opcao[1]:
                self.bd.atualizarCategoria(descricao, cod_registro)
                self.simple_msg_box(self.msg_dialog, "Sucesso!",
                                    ("Pergunta atualizada "
                                        "com sucesso!"))
                self.atualizar_grade_pergunta()
                window = self.janela_alteracao
                window.hide()
                return True
            
            elif operacao == opcao[2]:
                self.bd.atualizar_Resposta(descricao, cod_registro)
                self.simple_msg_box(self.msg_dialog, "Sucesso!",
                                    ("Resposta atualizada "
                                     "com sucesso!"))
                window = self.janela_alteracao
                window.hide()
                return True
            
            if testing == True:
                param = descricao
                self.unitTest_ao_clicar_salvar_alteracao(param, "ao_clicar_salvar_alteracao")
                
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro!",
                                    ("Erro ao atualizar pergunta\n"
                                        "%s") % (str(ex)))
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # >> Chamar uma nova Janela no mesmo arquivo glade
    def new_window_main(self, new_window, now_window,  modal=False, 
						destroy_parent=False, maximize=False):
        try:
            new_window.set_transient_for(now_window)
            new_window.set_modal(modal)
            new_window.set_destroy_with_parent(destroy_parent)
            new_window.show_all()
            if maximize == True:
                new_window.maximize()
            
            if testing == True:
                param = new_window
                self.unitTest_new_window_main(param, "new_window_main")
        
        except Exception as ex:
            self.simple_msg_box(self.msg_dialog, "Erro", "Detalhes: %s"
                                % (str(ex)), icon="dialog-error")
        
if __name__ == "__main__":
	builder.connect_signals(Handler())
	Gtk.main()
