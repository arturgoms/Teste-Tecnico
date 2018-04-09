# Teste Técnico
Teste técnico desenvolvido para CrossKnowledge.

[Demo](http://demo.arturgomes.com.br)

## Objetivo
Criar uma página única (Single page application) de cadastro de pessoas (nome, sobrenome e endereço) utilizando HTML, Javascript, CSS, MySQL e PHP (ou Python).

## Regras
A página deve mostrar:
- Uma lista refletindo o banco de dados atualizado, sem o recarregamento da página
- Atalhos para edição e remoção dos registros da lista
- Um formulário para inserção de novos registros e edição dos registros existentes

Requisitos:
- A inserção, remoção e edição dos registros deverá ser feita assincronamente utilizando AJAX e JSON.

## Frameworks Aceitos
- Pode ser utilizado um framework Javascript (como o jQuery) para chamadas assíncronas e comportamento da página
- Não deve ser utilizado nenhum framework PHP, Python, CSS e HTML

## Critérios de avaliação:
- Separação das camadas MVC
- Estrutura dos arquivos
- Clareza e simplicidade do código
- Uso das tecnologias citadas acima

---

## Reprodução
Testado em Ubuntu e MacOS

Clonar o projeto:
```
git clone https://github.com/arturgoms/Teste-Tecnico.git
```

Entrar na pasta:
```
cd Teste-Tecnico
```

Ativar o Virtualenv:
```
. venv/bin/activate
```

Editar o arquivo settings.py com as configurações do seu banco de dados:
```
DATABASE = {
  'user': 'usuario',
  'password': 'senha',
  'host': '127.0.0.1',
  'database': 'nome_do_banco',
  'raise_on_warnings': True,
  'use_pure': False,
}
```

Criar tabela 'users' dentro do banco, seguindo o modelo do models/user.sql:
```
CREATE TABLE IF NOT EXISTS nome_do_banco.users(                            
    -> id INT NOT NULL AUTO_INCREMENT,
    -> nome varchar(50) NOT NULL, 
    -> sobrenome varchar(50) NOT NULL, 
    -> endereco varchar(100) NOT NULL,
    -> PRIMARY KEY(id)
    -> );
```

Instalar o MySQL e Python connector MySQL para seu sistema operacional

Executar aplicação:
```
python3 manage.py
```

---

## Sobre o projeto
[Demo](http://demo.arturgomes.com.br)

<img src="https://preview.ibb.co/kzgzux/Screen_Shot_2018_04_08_at_00_09_02.png" width="400"><img src="https://preview.ibb.co/dAVESH/Screen_Shot_2018_04_08_at_00_09_16.png" width="400">

Foi utilizado:

- Python 3.6
- WSGI - Web Server Gateway Interface (webservice padrão do python)
- Virtualenv (ambiente virtual pra desenvolver aplicações em python).
- [Python connector to MySQL (MacOS)](https://dev.mysql.com/downloads/file/?id=472642)
- [MySQL (MacOS)](https://dev.mysql.com/downloads/file/?id=475582)

Funcionalidades:

- Single page application
- Estrutura MVC feita a mão com WSGI
- API com GET POST PUT e DELETE
- MySQL como Banco de dados        
- Retorno de erros vindo do servidor
- Alertas com mensagens de errors
