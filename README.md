# Challenge---IOT
RM558640 - Caio Amarante

RM556325 - Felipe Camargo

RM555997 - Caio Marques

--Tecnologias Utilizadas

-Hardware & IoT:
Sensor ultrassônico HC-SR04 com Arduino UNO (simulação no Tinkercad) e ESP8266/NodeMCU para envio de dados via HTTP POST.
LEDs indicadores (verde/vermelho) para sinalização de vaga livre/ocupada.

-Backend:
Python 3.8+ com Flask e flask-cors para criar uma API RESTful (POST /vaga, GET /vagas).
vagas.json como armazenamento simples de estado.

-Visão Computacional:
OpenCV (recorte automático de região de interesse) para isolar a placa da moto.
Tesseract OCR (modo --psm 7) para reconhecer caracteres de placas em imagens capturadas.

-Frontend:
HTML5 e CSS3 para estrutura e estilo do dashboard.
JavaScript (Fetch API) para interagir com a API e atualizar dinamicamente um grid de vagas a cada 2 s.

-Ambiente & Ferramentas:
Google Colab para prototipar e rodar o notebook de OCR.
VSCode como IDE, Postman/curl/PowerShell para testes de API.

--Resultados Parciais
OCR de Placa: leitura correta de placas simuladas (“XHC2F1”) em mais de 95 % dos testes no Colab, com pipeline que abrange detecção de contornos, binarização e ampliação.

Detecção de Ocupação: sensor ultrassônico identifica presença de motos até 50 cm com aproximadamente 98 % de confiabilidade; LEDs indicam o estado da vaga em tempo real.

Dashboard Web: interface responsiva em grid, capaz de refletir mudanças enviadas pela API em menos de 2 segundos, exibindo status (“livre”/“ocupada”) e placa associada a cada vaga.
