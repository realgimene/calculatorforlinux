 Calculadora Científica (Python/Tkinter)

Uma aplicação gráfica desenvolvida em Python e Tkinter que implementa uma calculadora com operações básicas e funções científicas. O projeto é um exercício de desenvolvimento de GUI em ambientes Linux (Lubuntu/Ubuntu), focando na manipulação de **widgets**, tratamento de **eventos** e integração com a biblioteca matemática (`math`).



# Interface de de Calculadora para Linux

Uma aplicação gráfica desenvolvida em Python para gerenciar usuários do sistema Linux (Lubuntu/Ubuntu), permitindo operações básicas de criação, modificação e exclusão de usuários através de uma interface amigável.

## Objetivo 

O principal objetivo é aprender e consolidar conceitos de programação, como lógica de controle e manipulação de interface gráfica (GUI), aplicando-os em um ambiente de desenvolvimento real (Linux). Este projeto permite a prática com bibliotecas específicas do sistema (como Tkinter ou GTK) e o uso de comandos de sistema (subprocess), aprofundando o conhecimento em Python e no ecossistema Linux.

## Requisitos

- Python 3.6 ou superior
- Sistema operacional Linux (testado no Lubuntu/Ubuntu)
- Privilégios de root ou execução via sudo
- tkinter (geralmente vem pré-instalado com Python)

### Instalação do tkinter (se necessário)

**Ubuntu/Debian/Lubuntu:**
```bash
sudo apt-get update
sudo apt-get install python3-tk
```

**Arch Linux:**
```bash
sudo pacman -S tk
```

### Funcionalidades da Interface


## Segurança

⚠️ **AVISO**: Esta aplicação executa comandos do sistema que podem modificar configurações críticas. Use apenas se você tiver conhecimento adequado sobre gerenciamento de usuários Linux.

- Sempre execute com privilégios de root/sudo
- Faça backup antes de realizar operações em sistemas de produção
- Use com cuidado em ambientes de produção


## Estrutura do Código

- `user_manager.py` - Aplicação principal com interface gráfica
- `requirements.txt` - Dependências do projeto (tkinter)

## Desenvolvimento

Este projeto foi desenvolvido para fins educacionais e demonstração de:
- Criação de interfaces gráficas com tkinter
- Execução de comandos do sistema via Python (subprocess)
- Interação com APIs do sistema (pwd, grp)
- Gerenciamento de privilégios e segurança



