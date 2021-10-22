# Descrição do Projeto:

Este README tem por objetivo fornecer as informações necessárias para utilização desta api Rest que simula um
sistema de registro de funcionários.

# 🚨 Como Rodar o Aplicativo

## 🚨 Requisitos:

1.  PostgresSQL **instalado** para construir o banco de dados.
2.  python3 com Pip **instalado** para gerenciar os pacotes e instalar as dependências da API
3.  yarn **instalado** para gerenciar os pacotes e instalar as dependências da Aplicação WEB

## Criar um banco de dados no postgress:

- 1. Crie um banco de dados no postgress, uma sugestão de nome = "mmlabsDB"
- 2. Abra a pasta app_api -> abra o arquivo settings.toml -> em development edite o campo "DB_URI_DEV"
     neste insira o link de acordo com o banco de dados que você criou na 1 etapa.
- 3. Com o banco configurado, é hora de configurar nossa API:
  - va até a pasta app_api (**dev_env/app_api**), e execute os seguintes comandos no terminal:

```sh
  -> pip install --upgrade virtualenv
  -> virtualenv -p python3 .venv
  -> source .venv/bin/activate
  -> pip install -r requirements.txt
  -> uvicorn app:create_app --reload --factory
```

- Com a api configurada, e rodando, basta acessar a url -> **http://127.0.0.1:8000/docs**, e você conseguira ter acesso a documentação da Api :).

- 4. Hora de configurar o nosso frontend:
  - Vá até a pasta app_webpage (**dev_env/app_webpage**), e execute os seguintes commandos no terminal :
  ```sh
  -> yarn
  -> yarn dev
  ```
- 5. Perfeito, com tudo configurado e rodando basta acessar a url -> **http://localhost:3000/**

# 🏗 Ferramentas do Projeto :

### BackEnd:

Linguagem -> Python - FastAPI

- Design pattern - MVC
- ORM - SQLAlchemy
- Autenticação e Segurança - FastAPI JWT
- Gerenciamento das Rotas - FastApi ApiRouter.
- Serialização - Pydantic
- Gerenciador de alterações do banco - SQLAlchemy.orm

### FrontEnd:

Linguagem -> JavaScript - ECS6

- Design pattern - MVC
- Framework - VueJs, NuxtJs
- Estilização - SCSS, CSS
- Authenticação - Oauth Token

# 🏗 REST API

Api Restful com CRUD do usuário e Autenticação de rotas.

## USER

##Open Api:

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "FastAPI",
    "version": "0.1.0"
  },
  "paths": {
    "/": {
      "get": {
        "tags": ["Status"],
        "summary": "Status Router",
        "description": "Rota destinada a verificar se a api está no ar\n:return: um dicionário com uma mensagem ok sinalizando o funcionamento da rota.",
        "operationId": "status_router__get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    },
    "/person/": {
      "get": {
        "tags": ["Person"],
        "summary": "List Patients",
        "operationId": "list_patients_person__get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PersonSchema"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": ["Person"],
        "summary": "Create Person",
        "operationId": "create_person_person__post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PersonCreateSchema"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PersonSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/person/{current_id}": {
      "get": {
        "tags": ["Person"],
        "summary": "Get Current Person",
        "description": "This router return data by one person, with they id.\n:param user:\n:param current_id:\n:param db:\n:return:",
        "operationId": "get_current_person_person__current_id__get",
        "parameters": [
          {
            "required": true,
            "schema": {
              "title": "Current Id",
              "type": "integer"
            },
            "name": "current_id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PersonSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "OAuth2PasswordBearer": []
          }
        ]
      }
    },
    "/person/{person_id}": {
      "delete": {
        "tags": ["Person"],
        "summary": "Delete Person",
        "operationId": "delete_person_person__person_id__delete",
        "parameters": [
          {
            "required": true,
            "schema": {
              "title": "Person Id",
              "type": "integer"
            },
            "name": "person_id",
            "in": "path"
          }
        ],
        "responses": {
          "204": {
            "description": "Successful Response"
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "OAuth2PasswordBearer": []
          }
        ]
      },
      "patch": {
        "tags": ["Person"],
        "summary": "Update Person",
        "operationId": "update_person_person__person_id__patch",
        "parameters": [
          {
            "required": true,
            "schema": {
              "title": "Person Id",
              "type": "integer"
            },
            "name": "person_id",
            "in": "path"
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PersonUpdateSchema"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PersonSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "OAuth2PasswordBearer": []
          }
        ]
      }
    },
    "/users/me": {
      "get": {
        "tags": ["users"],
        "summary": "Get User",
        "operationId": "get_user_users_me_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserSchema"
                }
              }
            }
          }
        },
        "security": [
          {
            "OAuth2PasswordBearer": []
          }
        ]
      }
    },
    "/token": {
      "post": {
        "tags": ["users"],
        "summary": "Generate Token",
        "operationId": "generate_token_token_post",
        "requestBody": {
          "content": {
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Body_generate_token_token_post"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/users": {
      "post": {
        "tags": ["users"],
        "summary": "Create User",
        "operationId": "create_user_users_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UserPersonCreateSchema"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/user/{user_id}": {
      "patch": {
        "tags": ["users"],
        "summary": "Update User",
        "operationId": "update_user_user__user_id__patch",
        "parameters": [
          {
            "required": true,
            "schema": {
              "title": "User Id",
              "type": "integer"
            },
            "name": "user_id",
            "in": "path"
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UserUpdateSchema"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/profile/": {
      "get": {
        "tags": ["profile"],
        "summary": "List Patients",
        "operationId": "list_patients_profile__get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ProfileSchema"
                }
              }
            }
          }
        },
        "security": [
          {
            "OAuth2PasswordBearer": []
          }
        ]
      },
      "post": {
        "tags": ["profile"],
        "summary": "Create Profile",
        "operationId": "create_profile_profile__post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ProfileCreateSchema"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ProfileSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/profile/{profile_id}": {
      "get": {
        "tags": ["profile"],
        "summary": "Get Person",
        "operationId": "get_person_profile__profile_id__get",
        "parameters": [
          {
            "required": true,
            "schema": {
              "title": "Profile Id",
              "type": "integer"
            },
            "name": "profile_id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ProfileSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "OAuth2PasswordBearer": []
          }
        ]
      },
      "delete": {
        "tags": ["profile"],
        "summary": "Delete Person",
        "operationId": "delete_person_profile__profile_id__delete",
        "parameters": [
          {
            "required": true,
            "schema": {
              "title": "Profile Id",
              "type": "integer"
            },
            "name": "profile_id",
            "in": "path"
          }
        ],
        "responses": {
          "204": {
            "description": "Successful Response"
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "OAuth2PasswordBearer": []
          }
        ]
      },
      "patch": {
        "tags": ["profile"],
        "summary": "Update Person",
        "operationId": "update_person_profile__profile_id__patch",
        "parameters": [
          {
            "required": true,
            "schema": {
              "title": "Profile Id",
              "type": "integer"
            },
            "name": "profile_id",
            "in": "path"
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ProfileUpdateSchema"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ProfileSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "OAuth2PasswordBearer": []
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "Body_generate_token_token_post": {
        "title": "Body_generate_token_token_post",
        "required": ["username", "password"],
        "type": "object",
        "properties": {
          "grant_type": {
            "title": "Grant Type",
            "pattern": "password",
            "type": "string"
          },
          "username": {
            "title": "Username",
            "type": "string"
          },
          "password": {
            "title": "Password",
            "type": "string"
          },
          "scope": {
            "title": "Scope",
            "type": "string",
            "default": ""
          },
          "client_id": {
            "title": "Client Id",
            "type": "string"
          },
          "client_secret": {
            "title": "Client Secret",
            "type": "string"
          }
        }
      },
      "HTTPValidationError": {
        "title": "HTTPValidationError",
        "type": "object",
        "properties": {
          "detail": {
            "title": "Detail",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ValidationError"
            }
          }
        }
      },
      "PersonCreateSchema": {
        "title": "PersonCreateSchema",
        "required": ["cpf", "name", "phone"],
        "type": "object",
        "properties": {
          "cpf": {
            "title": "Cpf",
            "type": "string"
          },
          "name": {
            "title": "Name",
            "type": "string"
          },
          "birth_date": {
            "title": "Birth Date",
            "type": "string",
            "format": "date"
          },
          "phone": {
            "title": "Phone",
            "type": "string"
          }
        }
      },
      "PersonSchema": {
        "title": "PersonSchema",
        "required": ["id", "cpf", "name", "phone"],
        "type": "object",
        "properties": {
          "id": {
            "title": "Id",
            "type": "integer"
          },
          "cpf": {
            "title": "Cpf",
            "type": "string"
          },
          "name": {
            "title": "Name",
            "type": "string"
          },
          "birth_date": {
            "title": "Birth Date",
            "type": "string",
            "format": "date"
          },
          "phone": {
            "title": "Phone",
            "type": "string"
          }
        }
      },
      "PersonUpdateSchema": {
        "title": "PersonUpdateSchema",
        "type": "object",
        "properties": {
          "cpf": {
            "title": "Cpf",
            "type": "string",
            "default": ""
          },
          "name": {
            "title": "Name",
            "type": "string",
            "default": ""
          },
          "birth_date": {
            "title": "Birth Date",
            "type": "string",
            "format": "date"
          },
          "phone": {
            "title": "Phone",
            "type": "string",
            "default": ""
          }
        }
      },
      "ProfileCreateSchema": {
        "title": "ProfileCreateSchema",
        "required": ["profile_url", "banner_profile_url", "bio"],
        "type": "object",
        "properties": {
          "profile_url": {
            "title": "Profile Url",
            "type": "string"
          },
          "banner_profile_url": {
            "title": "Banner Profile Url",
            "type": "string"
          },
          "bio": {
            "title": "Bio",
            "type": "string"
          },
          "user_id": {
            "title": "User Id",
            "type": "integer"
          }
        }
      },
      "ProfileSchema": {
        "title": "ProfileSchema",
        "required": ["id", "profile_url", "banner_profile_url", "bio", "user"],
        "type": "object",
        "properties": {
          "id": {
            "title": "Id",
            "type": "integer"
          },
          "profile_url": {
            "title": "Profile Url",
            "type": "string"
          },
          "banner_profile_url": {
            "title": "Banner Profile Url",
            "type": "string"
          },
          "bio": {
            "title": "Bio",
            "type": "string"
          },
          "user": {
            "$ref": "#/components/schemas/UserSchema"
          }
        }
      },
      "ProfileUpdateSchema": {
        "title": "ProfileUpdateSchema",
        "type": "object",
        "properties": {
          "profile_url": {
            "title": "Profile Url",
            "type": "string",
            "default": ""
          },
          "banner_profile_url": {
            "title": "Banner Profile Url",
            "type": "string",
            "default": ""
          },
          "bio": {
            "title": "Bio",
            "type": "string"
          },
          "user_id": {
            "title": "User Id",
            "type": "integer"
          }
        }
      },
      "UserPersonCreateSchema": {
        "title": "UserPersonCreateSchema",
        "required": [
          "name",
          "username",
          "cpf",
          "email",
          "phone",
          "birth_date",
          "user_group",
          "password"
        ],
        "type": "object",
        "properties": {
          "name": {
            "title": "Name",
            "type": "string"
          },
          "username": {
            "title": "Username",
            "type": "string"
          },
          "cpf": {
            "title": "Cpf",
            "type": "string"
          },
          "email": {
            "title": "Email",
            "type": "string"
          },
          "phone": {
            "title": "Phone",
            "type": "string"
          },
          "birth_date": {
            "title": "Birth Date",
            "type": "string"
          },
          "user_group": {
            "title": "User Group",
            "type": "string"
          },
          "password": {
            "title": "Password",
            "type": "string"
          }
        }
      },
      "UserSchema": {
        "title": "UserSchema",
        "required": ["id", "username", "email", "user_group", "person"],
        "type": "object",
        "properties": {
          "id": {
            "title": "Id",
            "type": "integer"
          },
          "username": {
            "title": "Username",
            "type": "string"
          },
          "email": {
            "title": "Email",
            "type": "string"
          },
          "user_group": {
            "title": "User Group",
            "type": "string"
          },
          "person": {
            "$ref": "#/components/schemas/PersonSchema"
          }
        }
      },
      "UserUpdateSchema": {
        "title": "UserUpdateSchema",
        "type": "object",
        "properties": {
          "username": {
            "title": "Username",
            "type": "string",
            "default": ""
          },
          "email": {
            "title": "Email",
            "type": "string",
            "default": ""
          },
          "last_password": {
            "title": "Last Password",
            "type": "string",
            "default": ""
          },
          "new_password": {
            "title": "New Password",
            "type": "string",
            "default": ""
          },
          "user_group": {
            "title": "User Group",
            "type": "string",
            "default": ""
          },
          "person_id": {
            "title": "Person Id",
            "type": "integer"
          }
        }
      },
      "ValidationError": {
        "title": "ValidationError",
        "required": ["loc", "msg", "type"],
        "type": "object",
        "properties": {
          "loc": {
            "title": "Location",
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "msg": {
            "title": "Message",
            "type": "string"
          },
          "type": {
            "title": "Error Type",
            "type": "string"
          }
        }
      }
    },
    "securitySchemes": {
      "OAuth2PasswordBearer": {
        "type": "oauth2",
        "flows": {
          "password": {
            "scopes": {},
            "tokenUrl": "token"
          }
        }
      }
    }
  }
}
```
