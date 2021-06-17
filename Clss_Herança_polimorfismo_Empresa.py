import re

class Pessoa:
    def __init__(self,nome,idade):
        if not isinstance(nome, str):
            raise TypeError ('Se nome não for string, levanta um TypeError')
        if nome == "":
            raise ValueError('Se nome for vazio, levanta um ValueError')
        if not isinstance(idade,int):
            raise TypeError('Se idade não for um inteiro, levanta um TypeError')
        if idade <0:
            raise ValueError(' Se idade for negativo, levanta um ValueError')
        self.__nome = nome
        self.__idade = idade
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    def aniversario(self):
        self.__idade += 1

class Funcionario(Pessoa):
    def __init__(self, nome, idade, email, carga_horaria):
        super().__init__(nome, idade)
        self.email=email
        self.carga_horaria=carga_horaria

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):
        if not isinstance(novo_email,str):
            raise TypeError('O email deve ser uma string.')
        if re.match("^[a-zA-ZO-9]*@[a-zA-ZO-9.]*$",novo_email) == None:
            raise ValueError('O emial deve conter apenas letras,números','pontos e um e somente um arroba')
        self.__email=novo_email

    @property
    def carga_horaria(self):
        raise NotImplementedError

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        raise NotImplementedError

    def calcula_salario(self):
        raise NotImplementedError

    def aumenta_salario(self):
        self.__salario_hora*= 1.05

class Programador(Funcionario):
    def __init__(self,nome,idade,email,carga_horaria):
        super().__init__(nome,idade,email,carga_horaria)
        self.__salario_hora = 35.00
        self.carga_horaria = carga_horaria
    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self,nova_carga_horaria):
        if nova_carga_horaria <20 or nova_carga_horaria >40:
            raise ValueError('A carga horária do programdor deve ser >=20',' e <=40')
        self.__carga_horaria = nova_carga_horaria
    def calcula_salario(self):
        return self.__salario_hora*self.carga_horaria*4.5

class Estagiario(Funcionario):
    def __init_(self,nome,idade,email,carga_horaria):
        super().__init__(nome,idade,email,carga_horaria)
        self.__salario_hora = 15.50
        self.__aux_alimentacao = 250.00
        self.carga_horaria = carga_horaria

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if nova_carga_horaria <16 or nova_carga_horaria >30:
            raise ValueError ('A carga do estagiario deve ser >=16','e <=30')
        self.__carga_horaria = nova_carga_horaria
    
    def calcula_salario(self):
        return(self.__salario_hora*self.carga_horaria*4.5 + self.__aux_alimentacao)

class Vendedor(Funcionario):
    def __init__(self,nome,idade,email,carga_horaria):
        super().__init__(nome,idade,email,carga_horaria)
        self.__salario_hora = 30.00
        self.__aux_alimentacao = 350.00
        self.__aux_transporte_visita = 30.00
        self.zerar_visitas()
    
    @property
    def carga_horaria(self):
        return self.__carga_horaria
    
    @carga_horaria.setter
    def carga_horaria(self,nova_carga_horaria):
        if nova_carga_horaria <15 or nova_carga_horaria >45:
            raise ValueError('A carga horaria do vendedor deve ser >=15', 'e <=45')
        self.__carga_horaria = nova_carga_horaria
    def calcular_salario(self):
        return(self.__salario_hora*self.carga_horaria*4.5+self.__aux_alimentação+self.visitas*self.__aux_transporte_visita)
    
    @property
    def visitas(self):
        return self.__visitas
    
    def realizar_visita(self,n_visitas):
        if n_visitas <0 or n_visitas >10:
            raise ValueError('O parâmetro n_visitas deve ser >0 0 e <=10')
        self.__visitas += n_visitas
    def zerar_visitas(self):
        self.__visitas = 0

class Empresa:
    def __init__(self, nome, cnpj, area_atuacao, equipe):
        self.nome = nome
        self.cnpj = cnpj
        self.area_atuacao = area_atuacao
        self.__equipe = []
        try:
            for f in equipe:
                self.contrata(f)
        except TypeError:
            raise EmpresaCreationError
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome (self,novo_nome):
        if not isinstance(novo_nome,str):
            raise EmpresaCreationError
        self.__nome = novo_nome
    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self,novo_cnpj):
        if not isinstance(novo_cnpj,str):
            raise EmpresaCreationError
        self.__cnpj = novo_cnpj
    @property
    def area_atuacao(self):
        return self.__area_atuacao
    @area_atuacao.setter
    def area_atuacao(self,nova_area_atuacao):
        if not isinstance(nova_area_atuacao,str):
            raise EmpresaCreationError
        self.__area_atuacao = nova_area_atuacao
    @property
    def equipe(self):
        return self.__equipe

    def contrata(self, novo_funcionario):
        if not isinstance(novo_funcionario,Funcionario):
            raise TypeError('O parâmetro novo_funcionario deve ser da classes','Funcionario')
        self.__equipe.append(novo_funcionario)

    def folha_pagamento(self):
        return sum([f.calcula_salario()for f in self.equipe])

    def folha_pagamento(self):
        return sum([f.calcula_salario() for f in self.equipe])

    def dissidio_anual(self):
        for f in self.equipe:
            f.aumenta_salario()

    def listar_visitas(self):
        return {f.email: f.visitas for f in self.equipe if isinstance(f, Vendedor)}

    def zerar_visitas_vendedores(self):
        for f in self.equipe:
            if isinstance(f,Vendedor):
                f.zerar_visitas()
        

