# Teste Técnico
Teste técnico desenvolvido para CrossKnowledge.

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

Executar aplicação:
```
python3 manage.py
```

---

## Sobre o projeto

Foi utilizado:

- Python 3.6
- WSGI (webservice padrão do python)
- Virtualenv (ambiente virtual pra desenvolver aplicações em python).
