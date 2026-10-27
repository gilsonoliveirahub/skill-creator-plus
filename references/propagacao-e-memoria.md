# Propagacao de aprendizado + skill vs. memoria

Usar no MODO IMPROVE quando o pedido nasce de um aprendizado concreto na conversa (correcao, validacao, padrao novo), nao de uma auditoria de rotina pedida direto ("melhora a skill X").

## 1. Tipos de aprendizado

- **Correcao**: "nao, nao faz assim" / "para de fazer X"
- **Validacao**: "isso, foi exatamente isso — fixa isso assim"
- **Padrao novo**: o usuario fez algo que a skill nao previa, e vale a pena guardar
- **Lacuna**: a skill devia ter tratado um caso e nao tratou

## 2. Achar skills afetadas

```bash
grep -rl "TERMO1\|TERMO2" ~/.claude/skills/*/SKILL.md
```

Classificar cada resultado por confianca, nunca aplicar tudo direto:

| Confianca | Quando | Acao |
|---|---|---|
| Alta | Mesmo topico, match direto | Propor a mudanca |
| Media | Topico adjacente, a regra pode ou nao se aplicar | Mostrar e perguntar antes de mudar |
| Baixa | So tangencial, a regra estica demais | So mencionar, nao propor mudanca |

## 3. Skill-especifico vs. principio geral

Perguntar: isto e uma regra so desta skill, ou um principio que vale para qualquer trabalho futuro do usuario (nao so skills)?

| Tipo | Onde fica |
|---|---|
| Regra so desta skill | Editar o `SKILL.md`/`references/` dela diretamente |
| Principio geral (vale para projetos, nao so skills) | Gravar na pasta de memoria de longo prazo que o usuario tiver configurada (ex.: `~/.claude/memory/` ou equivalente — o caminho exato varia por instalacao) |
| Os dois | Gravar a memoria E editar ja a(s) skill(s) que se aplicam |

Formato da memoria — usar exatamente o que ja existe no seu sistema, nao inventar outro:

```markdown
---
name: {slug-curto-em-kebab-case}
description: {uma linha, especifica — usada para decidir relevancia em conversas futuras}
metadata:
  type: feedback   # ou: user, project, reference
---

{a regra em si}

**Why:** {a razao dada pelo usuario — geralmente um incidente passado ou preferencia forte}

**How to apply:** {quando/onde esta regra entra em jogo}
```

E acrescentar uma linha no indice `MEMORY.md`: `- [Titulo curto](ficheiro.md) — gancho de uma linha, menos de 150 caracteres`.

Nunca escrever o conteudo da memoria diretamente no `MEMORY.md` — ele e so o indice.

## 4. Aprovar por ficheiro, nunca em lote

Mostrar cada mudanca como antes/depois com 1 linha de razao, esperar aprovacao, so depois passar ao ficheiro seguinte. Mudanca pequena e facil de aprovar isolada; em lote forca o usuario a aceitar ou rejeitar tudo junto, mesmo discordando de uma parte.
