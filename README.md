
# Gerador de Chave Secreta

Este projeto é um script em Python para gerar chaves secretas seguras e copiá-las automaticamente para o clipboard. Ele é ideal para uso em projetos que necessitam de chaves como `SECRET_KEY` em frameworks como Django.

## Recursos

- Gera uma chave secreta segura usando o módulo `secrets`.
- Copia a chave automaticamente para o clipboard usando comandos nativos do sistema operacional.
- Compatível com Windows, macOS e Linux.

## Pré-requisitos

Certifique-se de que você possui:

- Python 3.6 ou superior instalado.
- Um dos seguintes utilitários disponíveis no sistema:
  - **Windows**: `clip` (disponível por padrão).
  - **macOS**: `pbcopy` (disponível por padrão).
  - **Linux**: `xclip` (necessário instalar).

Para instalar o `xclip` no Linux:
```bash
sudo apt-get install xclip
```

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/santanadeveloper/generate-strong-key.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd generate-strong-key
   ```

## Uso

Execute o script diretamente no terminal:

```bash
python secret_key_generator.py
```

### Saída
O script gera uma chave secreta como esta:

```
FNknLcDYPWFlxc2iwUw6tPNLq8lOa0CQKgCoicqGFs_6o5dR4KTCT1XKBKb0SOwa3no
```

Você pode então colar a chave onde for necessário (ex.: variáveis de ambiente ou arquivos de configuração).

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature ou correção:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m "Descrição da minha feature"
   ```
4. Faça o push para sua branch:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request no GitHub.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

Feito com ❤️ por [João Paulo Santana](https://github.com/santanadeveloper)
