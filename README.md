🕹️ Jogo em Pygame — Prática de Código Limpo
Este projeto é um jogo simples desenvolvido com Pygame com o objetivo de praticar os princípios de código limpo, como modularidade, legibilidade, separação de responsabilidades e reutilização de componentes.

=> Como iniciar o projeto
Certifique-se de ter o Python instalado

Instale as dependências executando o seguinte comando na raiz do projeto:
pip install -r requirements.txt
Para iniciar o jogo, execute:
execulte:
python scripts/main.py

📁 Estrutura do projeto
FAZENDA/
├── data/               # Dados do jogo (tilesets, mapas, gráficos)
│   ├── graphics/
│   ├── maps/
│   └── tilesets/
├── imagens/            # Recursos visuais
│   ├── animais/
│   ├── inimigo/
│   ├── player/
│   ├── fundo.png
│   ├── pedra.png
│   └── player.png
├── scripts/            # Código-fonte do jogo
│   ├── __pycache__/
│   ├── animais.py
│   ├── config.py
│   ├── inimigo.py
│   ├── main.py
│   ├── mapa.py
│   ├── player.py
│   └── todasSprites.py
├── requirements.txt   


🎨 Créditos dos sprites
Todos os sprites utilizados neste projeto foram gentilmente disponibilizados por Kenmi no itch.io: "https://kenmi-art.itch.io/"

# Objetivo educacional
Este projeto não tem como foco a complexidade do gameplay, mas sim a organização do código, com boas práticas como:

Separação entre lógica de jogo e renderização

Uso de funções e classes bem definidas

Evitar duplicação e acoplamento excessivo

Nomes claros e intuitivos para variáveis e funções

📌 Observações
O jogo pode ser expandido com novos recursos, como sons, pontuação, inimigos e fases.

Sugestões e melhorias são bem-vindas!
