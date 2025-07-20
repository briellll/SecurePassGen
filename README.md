
# 🔐 SecurePassGen — API de Geração de Senhas Fortes

API simples e rápida feita com **FastAPI**, que gera senhas seguras personalizadas conforme as opções definidas pelo usuário.  
Ideal para integração em sistemas, aplicações web ou ferramentas de segurança.

---

## 🚀 Tecnologias Utilizadas

- **FastAPI** — Framework web para APIs rápidas
- **Uvicorn** — Servidor ASGI para rodar a aplicação
- **Pydantic** — Validação de dados
- **Pytest** — Testes automatizados
- **Taskipy** — Automação de comandos
- **Ruff** — Linter e formatador de código

---

## 🛠️ Funcionalidades

- Gerar senhas com comprimento definido
- Incluir ou não números na senha
- Incluir ou não símbolos na senha
- Retornar a senha gerada junto com os parâmetros utilizados

---

## 📦 Instalação e Execução

```bash
git clone https://github.com/briellll/securepassgen.git
cd securepassgen
poetry install
```

### Executar a aplicação:
```bash
poetry run task run
```

Acesse em: [http://localhost:8000/docs](http://localhost:8000/docs) — Documentação Swagger

---

## 🧪 Rodando os Testes

```bash
poetry run task test
```

---

## 🔥 Exemplo de Requisição

### POST `/gerar-senha`

**Body:**
```json
{
  "length": 16,
  "add_number": true,
  "add_symbol": true
}
```

**Resposta esperada:**
```json
{
  "password_created": "A1b2C3d4E5f6G7h8",
  "parameter": {
    "length": 16,
    "add_number": true,
    "add_symbol": true
  }
}
```

---

## ✨ Autor

Gabriel — [briellll](https://github.com/briellll)

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 📝 Use este projeto como base para suas aplicações ou estudos! 🚀
