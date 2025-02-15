# Projeto Django - Gerenciamento de Pacientes

Este projeto é um sistema de gerenciamento de pacientes e consultas médicas, desenvolvido com **Django**. Ele permite o cadastro de pacientes, registro de consultas, atribuição de tarefas e rastreamento de visualizações das consultas públicas.

## 🚀 Funcionalidades

- **Cadastro de Pacientes** com foto, e-mail e telefone.
- **Registro de Consultas** com humor, vídeo e descrição.
- **Atribuição de Tarefas** com frequência definida.
- **Visualizações de Consultas** com contagem total e única por IP.
- **Link Público das Consultas** apenas para pacientes com pagamento em dia.

## 🛠️ Tecnologias Utilizadas

- **Django** (Framework Web)
- **SQLite** (Banco de Dados padrão)
- **HTML + Tailwind CSS** (Interface do usuário)
- **Git/GitHub** (Controle de versão)

## 📌 Como Rodar o Projeto

### 1️⃣ Clonar o Repositório

```sh
 git clone https://github.com/seu-usuario/projeto-django.git
 cd projeto-django
```

### 2️⃣ Criar um Ambiente Virtual

```sh
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
```

### 3️⃣ Instalar Dependências

```sh
pip install -r requirements.txt
```

### 4️⃣ Rodar as Migrações do Banco de Dados

```sh
python manage.py migrate
```

### 5️⃣ Criar um Superusuário (Opcional)

```sh
python manage.py createsuperuser
```

### 6️⃣ Iniciar o Servidor

```sh
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📊 Registro de Visualizações

Todas as vezes que a página pública de uma consulta for carregada, a visualização será registrada no banco de dados:

```python
ip = request.META.get('REMOTE_ADDR', '0.0.0.0')
Visualizacoes.objects.create(consulta=consulta, ip=ip)
```

Isso permite acompanhar quantas vezes e quantos usuários únicos visualizaram a consulta.

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo!

---

✉️ **Contato**:fabio1010c\@hotmail.com

