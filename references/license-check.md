# Checar licenca ao clonar skill externa

Usar no MODO CLONE EXTERNA, antes de copiar qualquer linha de codigo ou texto de uma skill que nao e sua.

## Tabela de classificacao

| Licenca | Classificacao | Acao |
|---|---|---|
| MIT / Apache-2.0 / BSD / ISC / CC0 / Unlicense | Verde | Pode copiar e adaptar livremente |
| MPL-2.0 / LGPL | Amarelo | Pode adaptar, mas confirmar e avisar sobre reciprocidade a nivel de ficheiro |
| GPL-2.0 / GPL-3.0 / AGPL | Vermelho | Risco de contagio — nao copiar sem aprovacao explicita e por escrito |
| Proprietaria / sem ficheiro de licenca | Vermelho | Parar — sem base legal para copiar |
| Nao reconhecida / pouco clara | Amarelo | Perguntar; se ninguem souber dizer, tratar como vermelho |

Script: `python3 ~/.claude/skills/skill-creator-plus/scripts/license_check.py --path /caminho/para/LICENSE`
Ou, se so se souber o nome: `--name "MIT"`.

Vermelho bloqueia o resto do MODO CLONE EXTERNA. So continuar se o usuario aprovar explicitamente a copia mesmo assim (ex.: porque so vai inspirar a ideia, nao copiar texto/codigo).

## Classificacao em 3 baldes

Apresentar como tabela para aprovacao do usuario antes de escrever qualquer ficheiro da skill nova:

| Balde | O que entra | Exemplo |
|---|---|---|
| Manter igual | Schema, scripts, formato de dados, regex, flags de ferramenta | Banco de perguntas, flags do ffmpeg, JSON schema |
| Adaptar | Paths, nomes, convencoes proprias do autor original | Repo generico do autor -> `~/.claude/skills/` do usuario |
| Adicionar | Referencias cruzadas com skills ja instaladas, convencoes do usuario (ex.: score minimo 45/60, `$SCRATCHPAD`) | "Combina com find-skills", "Rodar collision_check.py antes de entregar" |

Nao reescrever em silencio — mostrar a tabela e so escrever depois de aprovada.

## Modelo de `references/attribution.md`

Escrever este ficheiro dentro da pasta da skill nova, sempre que a fonte for externa:

```markdown
# Atribuicao

- **Fonte**: <URL do SKILL.md original>
- **Repositorio**: <URL do repo>
- **Autor**: <nome ou handle>
- **Commit SHA**: <SHA no momento da clonagem>
- **Licenca**: <nome + URL>
- **Clonado em**: <AAAA-MM-DD>

## O que foi mantido igual
- ...

## O que foi adaptado
- <antes> -> <depois>

## O que foi adicionado
- ...

## Como verificar se ha versao mais nova
`git ls-remote <URL do repo> HEAD` — se o SHA for diferente do acima, avaliar se vale a pena atualizar (nao e automatico).
```

Para licencas MIT/BSD/Apache, o texto da LICENSE original tambem deve ficar copiado dentro da pasta da skill nova (ficheiro `LICENSE` ou colado neste `attribution.md`) — e o unico requisito legal destas licencas, nao e opcional.
