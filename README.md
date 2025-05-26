# Challenge IoT

**RM558640** – Caio Amarante  
**RM556325** – Felipe Camargo  
**RM555997** – Caio Marques

---

## Tecnologias Utilizadas

- **Hardware & IoT**  
  - Sensor ultrassônico HC-SR04 com Arduino UNO (simulação no Tinkercad)  
  - ESP8266/NodeMCU para envio de dados via HTTP POST  
  - LEDs indicadores (verde/vermelho) para sinalização de vaga livre/ocupada

- **Backend**  
  - Python 3.8+  
  - Flask & flask-cors para criar API RESTful  
    - **Endpoints**:  
      - `POST /vaga` – registrar ocupação de vaga  
      - `GET /vagas` – consultar status de todas as vagas  
  - Armazenamento: `vagas.json`

- **Visão Computacional**  
  - OpenCV para recorte automático da região de interesse (placa da moto)  
  - Tesseract OCR (modo `--psm 7`) para reconhecimento de caracteres

- **Frontend**  
  - HTML5 & CSS3 para estrutura e estilo  
  - JavaScript (Fetch API) para comunicação com a API  
  - Atualização dinâmica do dashboard a cada 2 segundos

- **Ambiente & Ferramentas**  
  - Google Colab para prototipagem do notebook de OCR  
  - VSCode como IDE  
  - Testes de API: Postman / curl / PowerShell

**Link Tinkercad:** [Visualização e Simulação](https://www.tinkercad.com/things/iyV2wHXrPS4/editel?sharecode=H4G81FURtnBcGJ910LN6aG40tuQJstCI72vHQZuynd8)

---

## Resultados Parciais

- **OCR de Placa**  
  - Leitura correta de placas simuladas (ex.: “XHC2F1”) em >95% dos testes no Colab  
  - Pipeline: detecção de contornos → binarização → ampliação → OCR

- **Detecção de Ocupação**  
  - Sensor ultrassônico identifica presença de motos até 50 cm com ≈98% de confiabilidade  
  - LEDs indicam estado da vaga em tempo real (verde = livre, vermelho = ocupada)

- **Dashboard Web**  
  - Interface responsiva em grid  
  - Atualização em <2 s após mudança de estado  
  - Exibe status e placa associada a cada vaga

---
