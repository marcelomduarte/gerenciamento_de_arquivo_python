# 🧩 Gerenciamento de Arquivos

## 📋 Sobre o Projeto

Este repositório reúne protótipos iniciais de automação para organização e padronização de arquivos locais, desenvolvidos em Python, com foco em aplicações corporativas.

Os scripts permitem:

- Renomear arquivos com prefixos e sufixos personalizados;

- Organizar arquivos por tipo (extensão) ou por regras personalizadas;

- Registrar logs detalhados de execução para auditoria e rastreabilidade.

🚧 Status: Protótipo em desenvolvimento — versão experimental para testes locais (.py).

## 🧠 Lógica do Protótipo

### 🔹 `ad_pref_suf_arqs.py`

Adiciona prefixos e sufixos aos nomes dos arquivos de um diretório:

```python
add_prefix_suffix("C:/Arquivos", prefix="novo_", suffix="_v1")
```

### 🔹 `org_arqs_por_tipo.py`

Classifica os arquivos da pasta `Downloads` automaticamente:

```text
Downloads/
 ├── pdf/
 ├── jpg/
 ├── xlsx/
 └── py/
```

### 🔹 `org_arqs_por_regras.py`

Permite definir regras personalizadas de organização:

```python
regras = {
    'Documentos': ['.docx', '.xlsx', '.pptx', '.pdf', '.txt', '.csv', '.log'],
    'Audios': ['.mp3', '.wav'],
    'Videos': ['.mp4', '.avi', '.mkv'],
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.ico'],
    'Compactados': ['.zip', '.rar', '.7z'],
    'Programas': ['.exe', '.msi'],
    'Scripts': ['.ps1', '.py', '.bat', '.sh']
}
```

## ▶️ **Como Usar**

### 1. Pré-requisitos

- **Python 3.10+** instalado no sistema  
- Permissões de leitura/escrita nas pastas onde os arquivos serão organizados  
- **VS Code** ou **PowerShell**

### 2. Execução Local via Terminal

Você pode executar qualquer script diretamente pelo terminal (CMD, PowerShell ou Bash):

```bash
# Exemplo: executar script de prefixo/sufixo
python ad_pref_suf_arqs.py

# Exemplo: organizar arquivos por tipo
python org_arqs_por_tipo.py

# Exemplo: organizar por regras personalizadas
python org_arqs_por_regras.py
```

> **Dica:** para testar sem mover arquivos reais, copie uma pasta de exemplo e aponte o script para ela.
