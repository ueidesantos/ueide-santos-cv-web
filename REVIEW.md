# Revisão adversarial e revitalização

2026-10-11. Revisão independente de código, UX, arquitetura da informação, storytelling e marketing, com correções implementadas.

| Achado | Correção |
|---|---|
| PDF de download inválido (2 bytes) | PDF real, texto selecionável, baseado no currículo e atualizado com experiência Safra |
| GitHub antigo retornava 404 | Links e metadados apontam ao perfil ueidesantos |
| Conteúdo dependia de JavaScript para aparecer | Conteúdo visível por padrão, sem script de animação |
| Impressão escondia seções | Estilos de impressão com texto escuro, sem ocultar a experiência |
| Âncoras cobertas pelo menu | Compensação de rolagem; menu estático no mobile |
| Movimento e teclado sem tratamento explícito | Reduced-motion, foco visível e atalho para conteúdo |
| Imagem pesada e sem dimensões | WebP sem perdas, dimensões explícitas e capa JPG original de 522 KB |
| Abertura longa e repetitiva | Nome, especialidade, contexto profissional e ação de contato |
| Provas e projetos pouco acessíveis | Casos por domínio, links às experiências e cards KISS AI Labs/Neuro Care |
| Fechamento sem ação | Convite de contato, email, LinkedIn e currículo |
| Identidade inconsistente | Navy, ciano, violeta e âmbar da imagem de referência; CSS separado |
| Formação futura ambígua | Pós-graduação identificada como em andamento |

Safra: descrição geral de engenharia de software, sem detalhes de sistemas, clientes, processos internos, volumes, prazos ou resultados não comprovados. Sem data de início presumida. Experiências anteriores preservadas.

## Evidências

Revisor independente: Edge em 320, 390, 768, 1024 e 1440 px, sem overflow nem imagens quebradas; conteúdo visível sem JavaScript; teclado e âncoras aprovados; impressão sem blocos invisíveis ou texto claro em fundo branco. PDF renderizado e texto conferido. Pipeline valida links locais, IDs, metadados, imagens e PDF; publica apenas index e assets referenciados.

As melhorias de marketing são editoriais; não há promessa de aumento de conversão nem coleta de dados. Publicação precisa de execução verde do workflow e verificação do site público.
