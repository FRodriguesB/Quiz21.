class UnitTest():
    def __init__(self, *args, **kwargs):
        super(UnitTest, self).__init__(*args, **kwargs)
        self.func_ok = 0
        self.func_erro = 0
    
    def unitTestbtnGerenciar(self, value, func):
        return_ok = "viewGerenciar"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestGerenciarPerguntas(self, value, func):
        return_ok = "viewPergunta"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    
    def unitTestbtnGerenciarRespostas(self, value, func):
        return_ok = "viewResposta"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnGerenciarCategorias(self, value, func):
        return_ok = "viewCategoria"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnNovoPergunta(self, value, func):        
        """
            Aqui verifico se a cursor não retornou uma lista vazia
            Se não retornou significa que a inclusão ocorreu com sucesso!
        """
        if len(value) > 0:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnAlterarPergunta(self, value, func):        
        """
            Aqui verifico se o usuário selecionou uma pengunta
            Caso sim o tamanho da lista deve ser maior que zero
        """
        if len(value) > 0:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnBuscarPergunta(self, value, func):        
        """
            Aqui verifico se o tipo de retorno é uma lista
        """
        if type(value) == list:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnExcluirPergunta(self, value, func):        
        """
            Aqui verifico se não existe mais nenhum código para ser excluído
        """
        if len(value) == 0:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_ao_selecionar_pergunta(self, value, func):        
        """
            Aqui verifico se o parametro ainda é do tipo lista
        """
        if type(value) == list:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnVoltarPergunta(self, value, func):        
        """
            Aqui verifico se a view atual é a esperada
        """
        return_ok = "viewInicio"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnNovoCategoria(self, value, func):        
        """
            Aqui verifico se a categoria não é nula
        """
        
        if value != "":
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_ao_selecionar_categoria(self, value, func):        
        """
            Aqui verifico se o parametro ainda é do tipo lista
        """
        if type(value) == list:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnAlterarCategoria(self, value, func):        
        """
            Aqui verifico se o usuário selecionou uma categoria
            Caso sim o tamanho da lista deve ser maior que zero
        """
        if len(value) > 0:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnBuscarCategoria(self, value, func):        
        """
            Aqui verifico se o tipo de retorno é uma lista
        """
        if type(value) == list:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnExcluirCategoria(self, value, func):        
        """
            Aqui verifico se não existe mais nenhum código para ser excluído
        """
        if len(value) == 0:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnVoltarCategoria(self, value, func):
        return_ok = "viewInicio"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_on_cmb_pergunta_changed(self, value, func):
        return_ok = "viewInicio"
        
        if type(value) == int:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnNovoResposta(self, value, func):        
        """
            Aqui verifico se a categoria não é nula
        """
        
        if value != "":
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_ao_selecionar_resposta(self, value, func):        
        """
            Aqui verifico se o parametro ainda é do tipo lista
        """
        if type(value) == list:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1

    def unitTest_ao_selecionar_resposta_gabarito(self, value, func):        
        """
            Aqui faço uma verificação de tipo dos parametros passados pela função
        """
        if type(value) == list:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnAlterarResposta(self, value, func):        
        """
            Aqui verifico se o parametro ainda é do tipo lista
        """
        if type(value) == list:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnExcluirResposta(self, value, func):        
        """
            Aqui verifico se não existe mais nenhum código para ser excluído
        """
        if len(value) == 0:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnVoltarResposta(self, value, func):
        return_ok = "viewInicio"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestbtnJogar(self, value, func):
        return_ok = "viewConfig"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_ao_selecionar_pergunta_jogo(self, value, func):        
        """
            Aqui verifico se o parametro ainda é do tipo lista
        """
        if type(value) == list:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_ao_clicar_buscar_pergunta_jogo(self, value, func):        
        """
            Aqui verifico se o parametro ainda é do tipo lista
        """
        if type(value) == list:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_ao_clicar_aplicar_jogo(self, value, func):        
        """
            Aqui verifico se o parametro ainda é do tipo lista
        """
        if value == 3:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
            
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_ao_clicar_desfazer_jogo(self, value, func):        
        """
            Aqui verifico se o a Stack atual é a viewInicio
        """
        return_ok = "viewInicio"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_on_janela_jogar_delete_event(self, value, func):        
        """
            Aqui verifico se o a Stack atual é a viewInicio
        """
        
        if value == True:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_on_bt_r1_ab1_clicked(self, value, func):        
        """
            Aqui verifico se o a Stack atual é a view_segunda_resposta
        """
        return_ok = "viewConfig"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_on_bt_r2_ab1_clicked(self, value, func):        
        """
            Aqui verifico se o a Stack atual é a view_segunda_resposta
        """
        return_ok = "viewConfig"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_on_bt_r3_ab1_clicked(self, value, func):        
        """
            Aqui verifico se o a Stack atual é a view_segunda_resposta
        """
        return_ok = "viewconfig"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_on_bt_r1_ab2_clicked(self, value, func):        
        """
            Aqui verifico se o a Stack atual é a view_terceira_resposta
        """
        return_ok = "viewConfig"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_on_bt_r2_ab2_clicked(self, value, func):        
        """
            Aqui verifico se o a Stack atual é a view_terceira_resposta
        """
        return_ok = "viewConfig"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_on_bt_r3_ab2_clicked(self, value, func):        
        """
            Aqui verifico se o a Stack atual é a view_terceira_resposta
        """
        return_ok = "viewConfig"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_on_bt_r1_ab3_clicked(self, value, func):        
        """
            Aqui verifico se a janela Jogo esta invisível
        """
        
        if value == False:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_on_bt_r2_ab3_clicked(self, value, func):        
        """
            Aqui verifico se a janela Jogo esta invisível
        """
        
        if value == False:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_on_bt_r3_ab3_clicked(self, value, func):        
        """
            Aqui verifico se a janela Jogo esta invisível
        """
        
        if value == False:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def on_bt_retornar_clicked(self, value, func):        
        if value == True:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_on_bt_voltar_view_relatorio_clicked(self, value, func):        
        """
            Aqui verifico se o a Stack atual é a viewInicio
        """
        return_ok = "viewInicio"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_on_btnGerenciarRelatorios_clicked(self, value, func):        
        """
            Aqui verifico se o a Stack atual é a view_relatorio
        """
        return_ok = "view_relatorio"
        
        if value == return_ok:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_on_bt_buscar_relatorio_clicked(self, value, func):        
        """
            Aqui vefiro se o tipo de retorno é uma lista
        """
        
        if type(value) == list:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_data_hoje_formatada(self, value, func):        
        """
            Aqui verifico se o tamanho da string esta no formato correto
            xx/xx/xxxx
        """
        
        if len(value) == 10:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_atualizar_grade_pergunta(self, value, func):        
        """
            Aqui verifico se o parametro retornado é uma lista
        """
        
        if type(value) == list:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_atualizar_grade_resposta(self, value, func):        
        """
            Aqui verifico se o parametro retornado é uma lista
        """
        
        if type(value) == list:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_atualizar_grade_categoria(self, value, func):        
        """
            Aqui verifico se o parametro retornado é uma lista
        """
        
        if type(value) == list:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_on_janela_vincular_gabarito_delete_event(self, value, func):        
        if value == True:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_ao_sair_janela_alteracao(self, value, func):        
        if value == True:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_ao_clicar_salvar_alteracao(self, value, func):        
        """
            Aqui verifico se a descrição informada não é nula
        """
        if value != "":
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTest_new_window_main(self, value, func):        
        """
            Aqui verifico se a janela não é um objeto nulo
        """
        if value != None:
            print("Teste executado com sucesso!\n"
                  "Função %s OK\n" % func)
            self.func_ok += 1
        
        else:
            print("Erro na execução da função: %s\n"
                  "Detalhes: Resultado diferente do esperado\n" % func)
            self.func_erro += 1
    
    def unitTestchecklog(self):
        totalFunc = (self.func_ok + self.func_erro)
        msg = (f"""
|----------------------------------------------------------------------|
|               Resultado de execução do programa                      |   
|----------------------------------------------------------------------|
Total de funções verificadas: {totalFunc}                             
Testes OK: {self.func_ok}                                             
Testes com Erro: {self.func_erro}                                     
|----------------------------------------------------------------------|
        """)
        
        print(msg)
