# _DÆMON - ver. 0.9.5-beta ~~ Desenvolvido pelo Bandeirinha
                                                                                                    
<p align="center">
  <img src="/docs/snapshots/satelite.png" alt="satelite" width="800"/>
</p>                                   
             
Para apoiar este e mais projetos:

    pixgg.com/bandeirinha

    
**_DÆMON** (_DAEMON) é um jogo de RPG single-player em modo texto (terminal) que simula um ecossistema dinâmico de IAs, reputações faccionais, operações de invasão abstratas, eventos mundiais e missões narrativas. O projeto é **ficcional** e não ensina técnicas reais de intrusão ou instruções práticas de ataque.

<img src="https://img.shields.io/badge/status-active-brightgreen">  
<img src="https://img.shields.io/badge/engine-python3-blue">

<p align="center">
  <img src="/docs/snapshots/events.png" alt="events" width="800"/>
</p>
<br>
<p align="center">
  <img src="/docs/snapshots/ingame.png" alt="gameplay" width="800"/>
</p>
<br>
<p align="center">
  <img src="/docs/snapshots/sing.png" alt="dialogue" width="800"/>
</p>

> **Aviso de origem:** Este projeto é inspirado conceitualmente em *Endgame: Singularity*, mas **não utiliza conteúdo oficial** do jogo original e **não é afiliado** aos autores originais. Todo o lore, personagens, nomes e textos deste repositório são originais ou reescritos para evitar uso de material protegido.

---

## Estado do projeto

- **Status:** Em desenvolvimento / versão experimental.  
- Pode conter bugs, código incompleto e mudanças de API entre commits.  
- Sem save/load game.
- Código aberto e **redistribuível: licenciado sob **GNU General Public License v3.0 ou posterior** (SPDX: `GPL-3.0-or-later`). Veja a seção *Licença* abaixo ou consulte o arquivo `LICENSE` para mais detalhes.


## Licença

_DAEMON
Copyright (C) 2025 Bandeirinha

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


## Nota do desenvolvedor
Decidi deixar o jogo em copyleft primeiro porque tudo começou como uma oportunidade para interagir com técnicas relativamente mais complexas dentro da linguagem Python. É um projeto para fins educacionais e de entretenimento. Segundo porque provavelmente não terei tempo até deixar o jogo como eu gostaria. Mas já fico imensamente satisfeito de ter conseguido publicar uma versão beta pelo menos... Então contarei com a comunidade Open Source para corrigir, melhorar, expandir e espalhar este "worm". 

    
## ATUALIZAÇÃO 26/01/2026 (ver. 0.9.5-beta):

- CORREÇÃO DE ENCERRAMENTO E MISSÃO FINAL EM FORMA DE DIÁLOGO EM sg_m6_dialogue.py

---

## Recursos principais

- Mundo procedural com regiões, tendências e desbloqueios.  
- IAs inimigas com perfis (Pirata, Federal, Hacktivista, Genérico).  
- Reputação por facção, missões narrativas e eventos que afetam gameplay.  
- Alvos gerados diariamente com chance de honeypot.  
- Sistema de risco, trace, multas e possibilidade de prisão (mecânicas de jogo).  
- Skills (recon, exploit, stealth), inventário e assets com renda passiva.  
- Tudo rodando via terminal — sem GUI.

---

## Requisitos

- **Python 3.8 ou superior** (testado com 3.8–3.11).  
- Sistema operacional: Linux, macOS ou Windows (com `python3` / `py`).  
- **Sem dependências externas**: apenas biblioteca padrão do Python.  
- Recomendado: terminal que suporte UTF-8 para melhor renderização dos caracteres usados nas animações ASCII.

Verifique a versão do Python:

```bash
python3 --version
# ou no Windows
py --version



    Instalação (passo a passo)

1. Clone o repositório:

git clone https://github.com/Loboguar4/_DAEMON.git
cd _DAEMON


2. (Opcional) Crie e ative um ambiente virtual:

python3 -m venv .venv
source .venv/bin/activate      # Linux / macOS
.venv\Scripts\activate         # Windows (PowerShell: .venv\Scripts\Activate.ps1)


3. Execute o jogo:

python3 _DAEMON.py
# ou no Windows
py _DAEMON.py

