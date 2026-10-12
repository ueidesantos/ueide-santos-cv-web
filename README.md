![Ueide Santos — engenharia de software, sistemas críticos, arquitetura e IA aplicada](assets/identity-cover.jpg)

# Ueide Santos — currículo web

[Visite o currículo](https://ueidesantos.github.io/ueide-santos-cv-web/) · [Baixe o PDF](assets/ueide-santos-cv.pdf)

Site estático em HTML/CSS, com conteúdo acessível sem JavaScript. Identidade baseada na capa original: navy, ciano, violeta e âmbar. Resumo, projetos públicos, experiências, competências, formação, formação complementar selecionada e contato.

## Validar e publicar

`python scripts/validate_site.py --build` verifica links locais, âncoras, imagens, JSON-LD e integridade básica do PDF; cria `_site` somente com os arquivos públicos referenciados. O workflow **Validate and publish CV** executa a validação e publica no GitHub Pages após push em main; também permite execução manual.

O PDF é versionado. Para atualizá-lo, execute `python scripts/build_resume.py` com ReportLab e fontes Segoe UI instalados (ou configure `CV_FONT_DIR`), mantendo texto e datas sincronizados com a página. Inspecione o PDF gerado antes de publicar.

Veja [REVIEW.md](REVIEW.md) para achados e verificações da revisão adversarial. Nenhum material de conversas privadas é publicado; a descrição profissional do Safra usa apenas atividades gerais.
