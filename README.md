# 🎬 Movies API

[🇺🇸 Read this in English](README.en.md)

![Status](https://img.shields.io/badge/status-Em%20desenvolvimento-yellow)

API desenvolvida com Django Rest Framework para gerenciar informações sobre filmes, gêneros, atores e avaliações. Inclui autenticação via JWT, controle de permissões, endpoints estatísticos e estrutura modular para escalabilidade.

---

## 📦 Models e Campos

### 🎭 Genre
| Campo   | Tipo                                | Descrição                          |
|---------|-------------------------------------|------------------------------------|
| `id`    | AutoField                           | Gerado automaticamente pelo Django |
| `nome`  | CharField (max_length=200)          | Nome do gênero                     |

### 🧑‍🎤 Actor
| Campo        | Tipo                                                    | Descrição                          |
|--------------|---------------------------------------------------------|------------------------------------|
| `id`         | AutoField                                               | Gerado automaticamente             |
| `name`       | CharField (max_length=200)                              | Nome do ator                       |
| `birthdate`  | DateField (null=True, blank=True)                       | Data de nascimento                 |
| `nationality`| CharField (max_length=100, null=True, blank=True, choices=NATIONALTY_CHOICES) | Nacionalidade |

### 🎬 Movie
| Campo         | Tipo                                                   | Descrição                            |
|---------------|--------------------------------------------------------|--------------------------------------|
| `id`          | AutoField                                              | Gerado automaticamente               |
| `title`       | CharField (max_length=500)                             | Título do filme                      |
| `genre`       | ForeignKey para Genre (on_delete=PROTECT, related_name='movies') | Gênero do filme           |
| `release_date`| DateField (null=True, blank=True)                      | Data de lançamento                   |
| `actors`      | ManyToManyField para Actor (related_name='movies')     | Atores do filme                      |
| `resume`      | TextField (null=True, blank=True)                      | Resumo do filme                      |

### 🌟 Review
| Campo     | Tipo                                                                  | Descrição               |
|-----------|-----------------------------------------------------------------------|-------------------------|
| `id`      | AutoField                                                             | Gerado automaticamente |
| `movie`   | ForeignKey para Movie (on_delete=PROTECT, related_name='reviews')     | Filme avaliado          |
| `stars`   | IntegerField (valores de 0 a 5 com validadores)                       | Avaliação em estrelas   |
| `comment` | TextField (null=True, blank=True)                                     | Comentário              |

---

## 🔐 Autenticação JWT

A API usa autenticação baseada em JSON Web Token (JWT).

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
Endpoints JWT:

POST /api/token/ – obter token (obtain)

POST /api/token/refresh/ – renovar token

POST /api/token/verify/ – verificar validade

⚙️ Funcionalidades Implementadas
✅ Views baseadas em Generic Views
✅ Serializers com ModelSerializers
✅ Validações customizadas no serializer
✅ Uso de SerializerMethodField para campos calculados
✅ Serializers dinâmicos para respostas GET com dados descritivos
✅ Substituição de get_serializer_class na view
✅ Estrutura de URLs com versionamento (/api/v1/)
✅ Include de rotas nas apps individuais
✅ App de autenticação própria: authentication

📊 Endpoints Estatísticos
Endpoint de estatística criado sem utilizar views genéricas.

🛡️ Permissões
Uso de Permission Classes do DRF em todas as views.

Implementação de uma Global Permission Class customizada.

Controle de ações baseado no tipo de método HTTP (view, add, change, delete).

🧩 Organização de URLs
Cada app possui seu próprio urls.py.

Arquivo principal permite versionamento:

python
Copiar código
path("api/v1/", include("movies.urls"))
📥 Importação em Massa com Comando Customizado
Foi criado um comando customizado chamado actors_register para importar atores a partir de um arquivo.

Exemplo de uso:
bash
Copiar código
python manage.py actors_register --file data/actors.csv
O argumento --file define o caminho do arquivo com os dados.

O comando faz o parsing e cadastra automaticamente os atores no banco.

Aceita formatos simples como CSV ou JSON (dependendo de como você configurar o parser).

🧪 Testes e Execução
bash
Copiar código
# Instalar dependências
pip install -r requirements.txt

# Rodar o servidor local
python manage.py runserver
🚀 Tecnologias Utilizadas
Python 3.10+

Django 4.x

Django Rest Framework

Simple JWT

PostgreSQL / SQLite

Validações com Django Validators

Comandos customizados com management commands

📫 Contato
Projeto desenvolvido por Felipe Rodrigues Fonseca
📧 Email: comunidadehawks@gmail.com
🔗 GitHub: FelRFDev/movies_api
