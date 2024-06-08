# Base image
# Atenção a imagem base deve ser a mesma da que vc versionou o modelo
FROM python:3.11.4

WORKDIR /mlp-eml2-atividade1

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "app/main.py"]

#----------INSTRUCTIONS----------

# buildar a imagem
#docker build -t api_deteccao_fraude .

# executar o container com os containers visualizando a rede da maquina
#--run in background--
#docker run -d --name api_deteccao_fraude --network host api_deteccao_fraude
#--run--
#docker run --name api_deteccao_fraude --network host api_deteccao_fraude 

# acessar o container
#docker exec -i -t api_deteccao_fraude bash

# finalizar a execucao do container
#docker kill api_deteccao_fraude

# excluir os containers finalizados
#docker rm $(docker ps -a -q)