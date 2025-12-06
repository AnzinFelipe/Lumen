# Como contribuir no Lumen ฅ(^•ﻌ•^ฅ)

👋 Seja muito bem-vindo à sessão de passos para ser um bom contribuidor para a plataforma do Lumen! 

---

## Pré-requisitos 🛠

Antes de começar a nos ajudar no aprimoramento do nosso projeto, certifique-se de ter as seguintes ferramentas instaladas:

- **Python**
- **Git**
- **Visual Studio Code (VSCode)**

---

## Primeiros passos . . . 👣

### 1. Faça um fork deste repositório.

### 2. Clone o repositório do projeto em seu computador:

Abra seu terminal e navegue até o diretório onde deseja clonar o repositório.
Em seguida, execute o comando:

```bash
git clone https://github.com/AnzinFelipe/Lumen.git
```
   
⛵ Navegue até o Diretório do Projeto

Use o comando:

```bash
cd Lumen
```

### 3. Crie e Ative um Ambiente Virtual 🧑‍💻

Caso não tenha o Virtualenv instalado, execute:

```bash 
pip install virtualenv
```
   
Agora crie o ambiente virtual:

```bash
python -m venv venv
```
   
Para ativar:

🔹 Windows:
```bash
venv\Scripts\activate
```
🔹 macOS/Linux:
```bash
source venv/bin/activate
```

### 4. Instale as Dependências 🔌

Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

### 5. Execute as Migrações 🔄

Crie as migrações:

```bash
python manage.py makemigrations
```
   
Depois aplique:

```bash
python manage.py migrate
```
*Em alguns dispositivos use "py" em vez de "python"*


### 6. Inicie o Servidor de Desenvolvimento ▶️

Execute:

```bash
python manage.py runserver
```
   
E então abra no navegador:

```bash
http://localhost:8000/
```

---

## Contribuindo com Código 🧑‍🔧

Recomendamos o uso do Visual Studio Code (VSCode) para desenvolver o projeto.
Para abrir o projeto no VSCode, siga os passos:
    
1. Abra o VSCode.  
2. Clique em *File > Open Folder...* e selecione o diretório do projeto **Lumen**.  
3. Tenha certeza de que o ambiente virtual esteja ativado no terminal do VSCode.

---

## Abra um Pull Request 💡

### 🔍 Processo de Revisão

Nossos *desenvolvedores analisarão cada Pull Request com atenção.  
Somente aqueles que estiverem alinhados com as diretrizes e os objetivos do projeto* serão aprovados.

---

## 🧾 Dúvidas?

Se ouver alguma duvida, abra uma **issue** e nossa equipe ficará feliz em ajudar.

---

## 📚 Diretrizes de Desenvolvimento 🤔

🔹 **Use boas práticas de código** em *Python, HTML e CSS*  
🔹 **Mantenha a formatação limpa e padronizada**  
🔹 **Organize os imports com elegância e ordem**
