## UFSCAR - Machine Learning in Production - EML2 - Atividade 2

Este repositório possui o intuito de conter os códigos da atividade 2, no qual possui o objetivo de por em prática o processo de Continuous Deployment (CD) utilizando o Github Actions.

### Estrutura do projeto

```
/mlp-eml2-atividade1
    .github/
        workflows/
            docker-image.yml
    /app
        __init__.py
        main.py
    /data
        scaler.sav
        rf_modelo_identificacao_fraud.sav
    /tests
        conftest.py
        test_app.py
    Dockerfile
    requirements.txt
    .gitignore
    .github/
        workflows/
            docker-image.yml
```

### Steps do processo de CI

* checkout: realiza o checkout do repositório para que o workflow consiga acessar
* setup-python: configura o ambiente Python
* install dependencies: instala as dependências descritas no `requirements.txt`, além do `pytest` e `pytest-cov`
* linter: executa o ruff para garantir uma boa qualidade do código
* run tests: executa os testes unitários e define um limiar de 70% de cobertura de teste para que o step não falhe

### Steps do processo de CD

* Checkout: realiza o checkout do repositório para que o workflow consiga acessar
* Set up Docker Buildx: cria e inicializa um builder para que seja possível construir e exportar a imagem confeccionada
* Log in to Docker Hub: faz o login no docker hub
* Build and push API: constrói e publica a API no docker hub