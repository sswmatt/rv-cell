# 🚀 Sistema de Cadastro de Clientes

Sistema web desenvolvido com **Django** para gerenciamento de clientes, permitindo cadastro, edição, exclusão e visualização em tempo real.

---

## 📌 Sobre o projeto

Este sistema foi criado com o objetivo de aplicar conceitos de desenvolvimento web utilizando o framework **Django**, integrando backend com frontend dinâmico através de **JavaScript** e consumo de API.

---

## ⚙️ Funcionalidades

✅ Cadastro de clientes  
✅ Listagem dinâmica de clientes  
✅ Edição de dados  
✅ Exclusão de clientes  
✅ Atualização em tempo real sem recarregar a página  
✅ Separação em múltiplas páginas  

---

## 🖥️ Tecnologias utilizadas

- Python 🐍  
- Django 🌐  
- HTML5  
- CSS3 🎨  
- JavaScript ⚡  

---

## 📂 Estrutura do projeto

```bash
sistema_cadastro/
│
├── clientes/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── home.html
│   │   └── lista.html
│   └── static/
│       └── css/
│           └── style.css
│
├── core/
├── manage.py
└── db.sqlite3

🔌 API

O sistema possui uma API simples para manipulação dos dados:

GET /api/clientes/ → Lista todos os clientes
POST /api/clientes/deletar/<id>/ → Remove cliente
GET /api/clientes/editar/<id>/ → Busca dados do cliente
POST /api/clientes/editar/<id>/ → Atualiza cliente
