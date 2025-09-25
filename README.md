# CommitFake

Script em Python para gerar **commits automáticos** em um repositório GitHub, útil para estudos sobre manipulação de datas de commits e preenchimento do gráfico de contribuições.

⚠️ **Aviso**: este projeto é apenas para fins de aprendizado. Usar commits falsos para manipular métricas públicas pode ser considerado antiético ou contra políticas de algumas plataformas. Use por sua conta e risco.

---

## ✨ Funcionalidades
- Definir ano inicial e final dos commits.
- Variar quantidade de commits por dia (configurável).
- Pular dias aleatoriamente para parecer natural.
- Envio automático (`git push`) para o GitHub.
- Criação de commit inicial caso o repositório esteja vazio.

---

## 📦 Pré-requisitos
- [Python 3.x](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- Um repositório GitHub (já criado e clonado).

---

## 🚀 Como usar

1. Clone o repositório no seu computador:
   ```powershell
   git clone https://github.com/SEU_USUARIO/CommitFake
   cd CommitFake
