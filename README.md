# 🐒 Monkeytype Auto-Typer

Um bot de automação desenvolvido em Python que digita automaticamente os textos do site [Monkeytype](https://monkeytype.com/). O script utiliza a biblioteca Selenium para controlar o navegador e interagir com os elementos ocultos da página, garantindo precisão e velocidade.

## 🚀 Funcionalidades

* **Leitura Dinâmica:** Captura em tempo real as palavras ativas na tela do Monkeytype.
* **Digitação Humanizada:** Possui intervalos aleatórios (em milissegundos) entre o envio de cada tecla para simular o comportamento humano.
* **Resolução de Bugs:** Interage diretamente com o campo de `input` oculto do site, evitando que teclas sejam perdidas ou que o layout da página quebre o bot.

## 🛠️ Tecnologias Utilizadas

* **Python** (Linguagem principal)
* **Selenium WebDriver** (Automação do navegador)
* **Google Chrome** (Navegador alvo)

## ⚙️ Como Instalar e Rodar

### Pré-requisitos
Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado no seu computador. Durante a instalação do Python no Windows, não se esqueça de marcar a opção **"Add Python to PATH"**.

### Passo a passo

1. **Clone este repositório** (ou baixe os arquivos em formato ZIP):
   ```bash
   git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
   Instale as dependências:
Abra o terminal na pasta do projeto e instale o Selenium executando:
python -m pip install selenium

Execute o Bot:
python nome_do_seu_arquivo.py

Configuração inicial: Ao rodar o script, o navegador Chrome será aberto automaticamente. Você terá 10 segundos para aceitar os cookies do site e ajustar as configurações do teste (tempo, idioma, pontuação, etc.) antes que o bot comece a digitar.

⚠️ Aviso Legal e Anti-Cheat
Este projeto foi criado estritamente para fins educacionais e de estudo sobre automação web com Selenium.

O Monkeytype possui um sistema anti-cheat rigoroso. Se o bot digitar rápido demais ou com intervalos perfeitamente idênticos, a sua pontuação não será salva no ranking oficial e a sua conta poderá ser banida. Para testes mais intensos, recomenda-se usar o site sem estar logado em uma conta pessoal.
