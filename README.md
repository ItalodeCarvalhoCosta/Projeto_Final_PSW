# Projeto_Final_PSW#  Floricultura Aurora 

Sistema web desenvolvido para gerenciamento de vendas de uma floricultura, permitindo organizar produtos, categorias, usuários e pedidos através de uma única plataforma.

O projeto foi desenvolvido utilizando o framework **Django**, seguindo o padrão arquitetural **MVT (Model - View - Template)**, proporcionando uma estrutura organizada e separada entre dados, regras de negócio e interface.

---

# Objetivo do Projeto

O objetivo principal é criar uma solução digital para auxiliar no gerenciamento interno de uma floricultura, substituindo controles manuais e centralizando informações importantes da operação.

O sistema permite que usuários realizem pedidos enquanto administradores conseguem gerenciar produtos, categorias e informações do negócio.

---

#  Funcionalidades

##  Usuários e Autenticação

O sistema possui gerenciamento de usuários utilizando a autenticação do Django.

Funcionalidades:

✅ Cadastro de usuários;  
✅ Login no sistema;  
✅ Controle de informações pessoais;  
✅ Integração com o sistema de usuários do Django;  
✅ Gerenciamento administrativo pelo Django Admin.

---

# Módulo de Produtos

Responsável pelo gerenciamento dos produtos comercializados pela floricultura.

Funcionalidades:

✅ Cadastro de produtos;  
✅ Organização por categorias;  
✅ Controle de descrição dos produtos;  
✅ Controle de preço unitário;  
✅ Controle de quantidade em estoque;  
✅ Informações adicionais como peso do produto.

Categorias disponíveis:

-  Flores;
-  Arranjos;
-  Mudas;
-  Ferramentas;
-  Outros.

---

#  Módulo de Categorias

Permite organizar os produtos da floricultura de forma estruturada.

Funcionalidades:

✅ Cadastro de categorias;  
✅ Descrição das categorias;  
✅ Associação entre produtos e categorias;  
✅ Organização do catálogo.

---

#  Módulo de Pedidos

Responsável pelo gerenciamento das compras realizadas pelos usuários.

Funcionalidades:

✅ Cadastro de pedidos;  
✅ Número identificador do pedido;  
✅ Associação entre usuário e pedido;  
✅ Adição de produtos ao pedido;  
✅ Controle de quantidade;  
✅ Cálculo de subtotal dos itens;  
✅ Controle do valor total;  
✅ Registro de informações de entrega.

Informações registradas:

- Usuário responsável pelo pedido;
- Endereço de entrega;
- Data e hora;
- Produtos escolhidos;
- Quantidades;
- Valores.

---

#  Arquitetura do Sistema

O projeto utiliza o padrão **MVT (Model - View - Template)** do Django.

## Model

Responsável pela representação dos dados e comunicação com o banco através do Django ORM.

Principais modelos:

- Usuário;
- Produto;
- Categoria;
- Pedido;
- ItemPedido.

## View

Responsável pela lógica de funcionamento da aplicação, recebendo requisições e retornando respostas.

## Template

Responsável pela interface visual utilizando HTML, CSS e JavaScript.

---

#  Tecnologias Utilizadas

## Backend

| Tecnologia | Descrição |
|---|---|
| Python | Linguagem principal |
| Django | Framework web utilizado |
| Django ORM | Comunicação com banco de dados |
| SQLite | Banco de dados padrão |
| Django Admin | Gerenciamento administrativo |

---

## Frontend

| Tecnologia | Descrição |
|---|---|
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização |
| JavaScript | Interações da interface |

---

## Ferramentas

| Ferramenta | Utilização |
|---|---|
| Git | Controle de versão |
| GitHub | Hospedagem do código |
| VS Code | Desenvolvimento |

---

#  Como Executar o Projeto Localmente

## 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Acesse a pasta:

```bash
cd PSW-ITALOCARVALHO-CAUA
```

---

## 2. Criar ambiente virtual

### Windows

```bash
python -m venv .venv
```

Ativar:

```bash
.venv\Scripts\activate
```

### Linux

```bash
python3 -m venv .venv
```

Ativar:

```bash
source .venv/bin/activate
```

---

## 3. Instalar dependências

Execute:

```bash
pip install -r requirements.txt
```

---

## 4. Configurar banco de dados

Execute as migrações:

```bash
python manage.py migrate
```

---

## 5. Criar administrador

Para acessar o painel administrativo:

```bash
python manage.py createsuperuser
```

Informe:

```text
Usuário:
Email:
Senha:
```

---

## 6. Executar aplicação

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000/
```

---

# 🔗 Principais Endereços

Página inicial:

```text
http://127.0.0.1:8000/
```

Admin Django:

```text
http://127.0.0.1:8000/admin/
```

---

# Testes Realizados

Foram realizados testes de:

✅ Cadastro de usuários;  
✅ Login no sistema;  
✅ Cadastro de categorias;  
✅ Cadastro de produtos;    
✅ Criação de pedidos;  
✅ Associação entre produtos e pedidos;  
✅ Integração com banco de dados;  
✅ Funcionamento do Django Admin.

---

#  Equipe:

Projeto desenvolvido por:

**Ítalo Carvalho e Cauã Maurício**

Projeto Final - Programação de Sistemas Web (PSW)
