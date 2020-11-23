#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class WidgetsConstructor(object):
    
    def startWidgets(self, builder, ui, *args):
        """
            param: builder é o construtor do Gtk Builder
        """
        
        # Carregando o arquivo gerado pelo Glade
        builder.add_from_file(ui)
        
         # >> Janela principal
        self.main_window = builder.get_object("janelaPrincipal")
        self.main_window.show_all()	
        
        # >> Message Box
        self.msg_dialog = builder.get_object("msg_dialog")
        
        # >> Janela atualização de registro
        self.janela_alteracao = builder.get_object("janela_alteracao")
        self.lb_titulo_alteracao = builder.get_object("lb_titulo_alteracao")
        self.lb_cod_reg_alter = builder.get_object("lb_cod_reg_alter")
        self.entry_texto_alter = builder.get_object("entry_texto_alter")
        self.bt_canc_alteracao = builder.get_object("bt_canc_alteracao")
        self.bt_conf_alteracao = builder.get_object("bt_conf_alteracao")
        
        # >> ComboBox Categoria
        self.cmb_categoria = builder.get_object("cmb_categoria")
        self.lst_combo_categoria = builder.get_object("lst_combo_categoria")
        self.op_categoria_default = (1, "->> Selecione a categoria <<-")
        self.lst_combo_categoria.append(self.op_categoria_default)
        self.cmb_categoria.set_active(0)
        
        # >> View cadastrar resposta
        self.check_resposta_1 = builder.get_object("check_resposta_1")
        self.cmb_pergunta = builder.get_object("cmb_pergunta")
        self.lst_cmb_pergunta = builder.get_object("lst_cmb_pergunta")
        self.op_pergunta_default = (1, "->> Selecione a pergunta <<-")
        self.lst_cmb_pergunta.append(self.op_pergunta_default)
        
        # >> View Config Reposta para jogar
        self.tx_busca_pergunta = builder.get_object("tx_busca_pergunta")
        self.lst_selecao_jogo = builder.get_object("lst_selecao_jogo")
        self.grade_selecao_jogo = builder.get_object("grade_selecao_jogo")
        self.bt_aplicar = builder.get_object("bt_aplicar")
        self.bt_desfazer = builder.get_object("bt_desfazer")
        self.lb_conta_pergunta = builder.get_object("lb_conta_pergunta")
        
        # >> ListStore para amazenar respostas
        
        # -> Aba 1
        self.lst_r1_aba1 = builder.get_object("lst_r1_aba1")
        self.lst_r2_aba1 = builder.get_object("lst_r2_aba1")
        self.lst_r3_aba1 = builder.get_object("lst_r3_aba1")
        
        # -> Aba 2
        self.lst_r1_aba2 = builder.get_object("lst_r1_aba2")
        self.lst_r2_aba2 = builder.get_object("lst_r2_aba2")
        self.lst_r3_aba2 = builder.get_object("lst_r3_aba2")
        
        # -> Aba 3
        self.lst_r1_aba3 = builder.get_object("lst_r1_aba3")
        self.lst_r2_aba3 = builder.get_object("lst_r2_aba3")
        self.lst_r3_aba3 = builder.get_object("lst_r3_aba3")
        
        # >> Janela Jogar
        self.janela_jogar = builder.get_object("janela_jogar")
        self.StackJogo = builder.get_object("StackJogo")
        
        # -> View 1 
        self.lb_pergunta_ab1 = builder.get_object("lb_pergunta_ab1")
        self.lb_r1_ab1 = builder.get_object("lb_r1_ab1")
        self.lb_r2_ab1 = builder.get_object("lb_r2_ab1")
        self.lb_r3_ab1 = builder.get_object("lb_r3_ab1")
        self.img_perg_ab1 = builder.get_object("img_perg_ab1")
        self.bt_r1_ab1 = builder.get_object("bt_r1_ab1")
        self.bt_r1_ab2 = builder.get_object("bt_r1_ab2")
        self.bt_r1_ab3 = builder.get_object("bt_r1_ab3")
        
        # -> View 2
        self.lb_pergunta_ab2 = builder.get_object("lb_pergunta_ab2")
        self.lb_r1_ab2 = builder.get_object("lb_r1_ab2")
        self.lb_r2_ab2 = builder.get_object("lb_r2_ab2")
        self.lb_r3_ab2 = builder.get_object("lb_r3_ab2")
        self.img_perg_ab2 = builder.get_object("img_perg_ab2")
        
        # -> View 3
        self.lb_pergunta_ab3 = builder.get_object("lb_pergunta_ab3")
        self.lb_r1_ab3 = builder.get_object("lb_r1_ab3")
        self.lb_r2_ab3 = builder.get_object("lb_r2_ab3")
        self.lb_r3_ab3 = builder.get_object("lb_r3_ab3")
        self.img_perg_ab3 = builder.get_object("img_perg_ab3")
        
        # >> Janela parabens
        self.janela_parabens = builder.get_object("janela_parabens")
        self.bt_retornar = builder.get_object("bt_retornar")
        
        # >> View Principal
        self.Stack = builder.get_object("Stack")
        self.grade_pergunta = builder.get_object("gradePergunta")
        self.grade_categoria = builder.get_object("gradeCategoria")
        self.grade_resposta = builder.get_object("gradeResposta")
        self.lstPergunta = builder.get_object("lstPergunta")
        self.lstResposta = builder.get_object("lstResposta")
        self.lstCategoria = builder.get_object("lstCategoria")
        self.entryPergunta = builder.get_object("entryPergunta")
        self.selecionar_imagem = builder.get_object("selecionar_imagem")
        self.entryCategoria = builder.get_object("entryCategoria")
        self.entryResposta = builder.get_object("entryResposta")
        self.entrybuscar = builder.get_object("entrybuscar")
        self.lb_statusPergunta = builder.get_object("lb_statusPergunta")
        self.lb_statusCategoria = builder.get_object("lb_statusCategoria")
        self.lb_statusResposta = builder.get_object("lb_statusResposta")
        
        # >> View Relatório
        self.grade_relatorio = builder.get_object("grade_relatorio")
        self.lst_relatorio = builder.get_object("lst_relatorio")
        self.entry_dh_inicial = builder.get_object("entry_dh_inicial")
        self.entry_dh_final = builder.get_object("entry_dh_final")
        self.lb_count_correta = builder.get_object("lb_count_correta")
        self.lb_count_incorreta = builder.get_object("lb_count_incorreta")
