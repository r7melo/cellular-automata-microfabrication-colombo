# Cellular Automata Microfabrication - Colombo (2017)

Este projeto é uma implementação acadêmica dos modelos e algoritmos de Autômatos Celulares (AC) propostos por Fábio Belotti Colombo em sua tese de doutorado pela Escola Politécnica da USP (2017).

O foco reside na simulação física de processos de fabricação de semicondutores e microssistemas (MEMS).

---

## 🔬 Escopo Científico

A simulação abandona métodos convencionais de rastreamento de interface (como Level Set) em favor de uma abordagem baseada em regras locais de Autômatos Celulares, garantindo alta performance e escalabilidade para estruturas 3D complexas.

---

## 1️⃣ Modelo de Evolução Topográfica (Corrosão e Deposição)

O motor central baseia-se no Princípio de Huygens, onde cada célula da matriz de autômatos funciona como uma fonte secundária de uma frente de onda.

### 📌 Contador de Distância

Cada célula armazena um vetor de distância $\\vec{D}$.

A evolução da superfície ocorre conforme as células vizinhas propagam seus valores, minimizando o vetor resultante.

### 📌 Anisotropia

O modelo permite a simulação de taxas de corrosão distintas para diferentes planos cristalográficos (como os planos {100}, {110} e {111} do Silício), essencial para a fabricação de cavidades e membranas.

---

## 2️⃣ Modelo de Transporte de Massa (Difusão e Oxidação)

Para processos que envolvem migração de átomos, o projeto utiliza o Modelo de Autômatos Celulares Multipartículas.

### 📌 Caminhada Aleatória (Random Walk)

Simulação estocástica do movimento de dopantes para prever perfis de concentração.

### 📌 Oxidação Térmica

Modelagem da reação química na interface $Si/SiO_2$ e a expansão volumétrica resultante do crescimento do óxido.

---

## 📐 Parâmetros de Validação

A precisão dos algoritmos é validada através de métricas descritas no Capítulo 3 da tese, garantindo que a discretização do espaço (voxels) não comprometa a física do processo.

### 🔢 Número de iterações ($N_p$)

Cálculo do tempo discreto necessário para atingir profundidades físicas reais.

### 🔷 Vizinhança de von Neumann

Uso de 6 vizinhos (em 3D) para otimizar o processamento sem perda de resolução topográfica.

---

## 📖 Referência Principal

COLOMBO, Fábio Belotti.

Aplicação de autômatos celulares para simulação de processos de microfabricação.

2017. Tese (Doutorado em Engenharia Elétrica) - Escola Politécnica, Universidade de São Paulo, São Paulo, 2017.


## Licença
Distribuído sob a licença GNU GPL v3.0. Veja `LICENSE` para mais detalhes.
