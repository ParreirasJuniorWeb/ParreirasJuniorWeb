#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para documentar as mudanças de rename dos repositórios
Uso: python3 rename-script.py
"""

import json
from datetime import datetime

# Mapping de nomes antigos para novos
RENAME_MAP = {
    # Repositórios Didáticos a ARQUIVAR
    "HTTP_REACT_": {
        "action": "ARQUIVAR",
        "reason": "Repositório didático/estudo - não é um projeto final"
    },
    "ReactAPIContext": {
        "action": "ARQUIVAR",
        "reason": "Repositório didático/estudo - não é um projeto final"
    },
    "React-Router-dom": {
        "action": "ARQUIVAR",
        "reason": "Repositório didático/estudo - não é um projeto final"
    },
    
    # CONSOLIDAÇÕES - DELETAR DUPLICATAS
    "PROJETO_CALCULADORA_IMC": {
        "action": "DELETAR",
        "consolidar_em": "PROJECT_CALCULADORA_IMC_REACT",
        "reason": "Duplicata - versão JavaScript simples. Manter versão React"
    },
    "ToDoList_Simple_JS": {
        "action": "DELETAR",
        "consolidar_em": "PROJETO_DO_TO_LIST_AdvancedToDoPro",
        "reason": "Duplicata - versão simples. Manter versão avançada"
    },
    "PROJECT_TO_DO_LIST_Avan-ado": {
        "action": "DELETAR",
        "consolidar_em": "PROJETO_DO_TO_LIST_AdvancedToDoPro",
        "reason": "Duplicata - nome mal formatado. Manter versão principal"
    },
    "WeatherAppJavaScript": {
        "action": "DELETAR",
        "consolidar_em": "ReactWeatherApp_useAPIContext_customHookToFetch",
        "reason": "Duplicata - versão vanilla JS. Manter versão React avançada"
    },
    "PROJETO_PAGINAS_VENDAS_IPHONE": {
        "action": "DELETAR",
        "consolidar_em": "iphone13_clone-main",
        "reason": "Duplicata - versão simples. Manter versão clone melhor"
    },
    
    # RENOMEAÇÕES - PADRONIZAÇÃO (kebab-case, sem CAPS)
    "PROJETO_TABUADA": {
        "action": "RENOMEAR",
        "novo_nome": "tabuada-app",
        "reason": "Padronização: lowercase + kebab-case"
    },
    "PROJETO_GERADOR_SENHAS": {
        "action": "RENOMEAR",
        "novo_nome": "password-generator",
        "reason": "Padronização: lowercase + kebab-case + nome em inglês"
    },
    "PROJETO_GERADOR_QRCODE": {
        "action": "RENOMEAR",
        "novo_nome": "qr-code-generator",
        "reason": "Padronização: lowercase + kebab-case"
    },
    "PROJETO_DEV_NOTES": {
        "action": "RENOMEAR",
        "novo_nome": "dev-notes-app",
        "reason": "Padronização: lowercase + kebab-case"
    },
    "PROJECT_GERADOR_BOX_SHADOW": {
        "action": "RENOMEAR",
        "novo_nome": "box-shadow-generator",
        "reason": "Padronização: lowercase + kebab-case"
    },
    "PROJECT_CALCULADORA_IMC_REACT": {
        "action": "RENOMEAR",
        "novo_nome": "imc-calculator",
        "reason": "Padronização: lowercase + kebab-case + nome mais conciso"
    },
    "PROJETO_DO_TO_LIST_AdvancedToDoPro": {
        "action": "RENOMEAR",
        "novo_nome": "advanced-todo-pro",
        "reason": "Padronização: lowercase + kebab-case"
    },
    "SimonGameChallengeCompleted": {
        "action": "RENOMEAR",
        "novo_nome": "simon-game",
        "reason": "Padronização: lowercase + kebab-case + nome mais conciso"
    },
    "QuizReact": {
        "action": "RENOMEAR",
        "novo_nome": "quiz-app",
        "reason": "Padronização: lowercase + kebab-case"
    },
    "CountDownReact": {
        "action": "RENOMEAR",
        "novo_nome": "countdown-timer",
        "reason": "Padronização: lowercase + kebab-case"
    },
    "ReactPostApplication": {
        "action": "RENOMEAR",
        "novo_nome": "post-app",
        "reason": "Padronização: lowercase + kebab-case + nome mais conciso"
    },
    "ReactFormMultistep": {
        "action": "RENOMEAR",
        "novo_nome": "multistep-form",
        "reason": "Padronização: lowercase + kebab-case"
    },
    "PartyTimeProject": {
        "action": "RENOMEAR",
        "novo_nome": "party-time-events",
        "reason": "Padronização: lowercase + kebab-case"
    },
    "MemoriesProject": {
        "action": "RENOMEAR",
        "novo_nome": "memories-app",
        "reason": "Padronização: lowercase + kebab-case"
    },
    "MyResume_with_Bootstrap": {
        "action": "RENOMEAR",
        "novo_nome": "portfolio",
        "reason": "Padronização: lowercase + kebab-case + nome mais claro"
    },
    "HDC_HOST_PROJECT": {
        "action": "RENOMEAR",
        "novo_nome": "hdc-host-landing",
        "reason": "Padronização: lowercase + kebab-case"
    },
    "iphone13_clone-main": {
        "action": "RENOMEAR",
        "novo_nome": "iphone13-landing",
        "reason": "Padronização: remover '-main' redundante + kebab-case"
    },
    "Instagram_clone": {
        "action": "RENOMEAR",
        "novo_nome": "instagram-clone",
        "reason": "Padronização: lowercase + kebab-case"
    },
    "SiteNewspaper": {
        "action": "RENOMEAR",
        "novo_nome": "newspaper-blog",
        "reason": "Padronização: lowercase + kebab-case"
    },
    "Capstone3_Blog": {
        "action": "RENOMEAR",
        "novo_nome": "blog-cms",
        "reason": "Padronização: lowercase + kebab-case + nome mais profissional"
    },
}

def print_header(text, char="="):
    """Imprime um header formatado"""
    print(f"\n{char * 80}")
    print(f"  {text}")
    print(f"{char * 80}\n")

def generate_report():
    """Gera o relatório completo de mudanças"""
    
    print_header("📋 RELATÓRIO DE MUDANÇAS DE REPOSITÓRIOS", "=")
    print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Total de mudanças: {len(RENAME_MAP)}\n")
    
    # Contadores
    arquivar = 0
    deletar = 0
    renomear = 0
    
    # Separar por ação
    arquivos_arquivar = {}
    arquivos_deletar = {}
    arquivos_renomear = {}
    
    for nome_antigo, info in RENAME_MAP.items():
        if info["action"] == "ARQUIVAR":
            arquivos_arquivar[nome_antigo] = info
            arquivar += 1
        elif info["action"] == "DELETAR":
            arquivos_deletar[nome_antigo] = info
            deletar += 1
        elif info["action"] == "RENOMEAR":
            arquivos_renomear[nome_antigo] = info
            renomear += 1
    
    # Seção 1: ARQUIVAR
    if arquivos_arquivar:
        print_header(f"🗂️  REPOSITÓRIOS A ARQUIVAR ({arquivar})", "-")
        for nome, info in arquivos_arquivar.items():
            print(f"Repositório: {nome}")
            print(f"Motivo: {info['reason']}")
            print(f"GitHub CLI: gh repo archive ParreirasJuniorWeb/{nome}")
            print()
    
    # Seção 2: DELETAR (Duplicatas)
    if arquivos_deletar:
        print_header(f"🗑️  REPOSITÓRIOS A DELETAR (DUPLICATAS) ({deletar})", "-")
        for nome, info in arquivos_deletar.items():
            print(f"Repositório: {nome}")
            print(f"Consolidar em: {info['consolidar_em']}")
            print(f"Motivo: {info['reason']}")
            print(f"GitHub CLI: gh repo delete ParreirasJuniorWeb/{nome} --confirm")
            print()
    
    # Seção 3: RENOMEAR
    if arquivos_renomear:
        print_header(f"✏️  REPOSITÓRIOS A RENOMEAR ({renomear})", "-")
        
        # Tabela de renomeações
        print(f"{'Antigo':<40} {'→':<3} {'Novo':<40}")
        print("-" * 85)
        for nome, info in arquivos_renomear.items():
            print(f"{nome:<40} → {info['novo_nome']:<40}")
        
        print("\n" + "=" * 85)
        print("\n📌 INSTRUÇÕES DE RENOMEAÇÃO via GitHub API/CLI:\n")
        print("Usando GitHub CLI (recomendado):")
        print("-" * 85)
        for nome, info in arquivos_renomear.items():
            print(f"gh repo rename {nome} {info['novo_nome']} --repo ParreirasJuniorWeb/{nome}")
        
        print("\n\nManualmente via GitHub Web:")
        print("-" * 85)
        print("1. Vá para: https://github.com/ParreirasJuniorWeb/{repo-name}/settings")
        print("2. Localize a seção 'Repository name'")
        print("3. Digite o novo nome")
        print("4. Clique em 'Rename'")
    
    # Resumo Final
    print_header("📊 RESUMO FINAL", "=")
    print(f"✓ Arquivar:  {arquivar} repositórios")
    print(f"✗ Deletar:   {deletar} repositórios (duplicatas)")
    print(f"✏️  Renomear: {renomear} repositórios")
    print(f"\n📈 Total de mudanças: {arquivar + deletar + renomear}")
    print(f"📉 Redução final: de 85 para aproximadamente {85 - arquivar - deletar} repositórios")
    print("\n✅ Status: Pronto para executar mudanças!")

def generate_json_export():
    """Exporta dados em JSON para processamento automatizado"""
    output = {
        "generated_at": datetime.now().isoformat(),
        "total_changes": len(RENAME_MAP),
        "changes": RENAME_MAP
    }
    
    with open("rename-changes.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print("✅ Arquivo 'rename-changes.json' exportado com sucesso!")

if __name__ == "__main__":
    generate_report()
    print("\n")
    generate_json_export()
