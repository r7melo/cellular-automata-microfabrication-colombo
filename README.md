# Emergent-CA-Intelligence

Este projeto investiga a possibilidade de gerar inteligência
através de Autômatos Celulares Adaptativos, inspirado em conceitos de 
Computação Emergente e neuroplasticidade.

## Objetivo
Criar uma matriz onde as regras de transição locais convergem para estados 
de processamento de informação estáveis.

## Referências Culturais
Inspirado na exploração de consciência digital e sistemas emergentes vistos 
na ficção científica (como o conceito de "Thronglets").

## Configuração do Ambiente

Esta seção descreve, de forma estruturada e sequencial, a preparação do ambiente
de desenvolvimento para o projeto Emergent-CA-Intelligence.

---

### 1. Clonagem do Repositório

Passo responsável por obter o código-fonte localmente.

```bash
git clone https://github.com/r7melo/Emergent-CA-Intelligence.git
cd Emergent-CA-Intelligence
```

---

### 2. Criação do Ambiente Virtual

Isola as dependências do projeto do restante do sistema.

Sistema Unix (Linux / macOS):

```bash
python3 -m venv venv
source venv/bin/activate
```

Sistema Windows:

```bash
python -m venv venv
venv\\Scripts\\activate
```

Estado esperado:
O terminal deve exibir o prefixo `(venv)` indicando ativação bem-sucedida.

---

### 3. Atualização do Gerenciador de Pacotes

Garante compatibilidade e suporte às versões mais recentes.

```bash
pip install --upgrade pip
```

---

### 4. Instalação das Dependências

Modo padrão (via requirements.txt):

```bash
pip install -r requirements.txt
```

### 5. Congelamento do Ambiente

Registre o estado exato do ambiente:

```bash
pip freeze > requirements.txt
```

---

### 6. Execução do Projeto

Execução direta do ponto de entrada principal:

```bash
python main.py
```

---

### 7. Encerramento do Ambiente

Desativa o ambiente virtual ao finalizar a sessão.

```bash
deactivate
```


## Licença
Distribuído sob a licença GNU GPL v3.0. Veja `LICENSE` para mais detalhes.
