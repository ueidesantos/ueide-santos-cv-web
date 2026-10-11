"""Build the downloadable résumé. Requires reportlab; optional CV_FONT_DIR for TTFs.
Run: python scripts/build_resume.py
Content transcribed from the existing public index.html, with the current GitHub URL.
"""
from pathlib import Path
import os
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
font_dir = Path(os.environ.get('CV_FONT_DIR', 'C:/Windows/Fonts'))
for face, file in [('CV', 'segoeui.ttf'), ('CVBold', 'segoeuib.ttf')]:
    if not (font_dir/file).exists():
        raise SystemExit('Set CV_FONT_DIR to a directory containing segoeui.ttf and segoeuib.ttf.')
    pdfmetrics.registerFont(TTFont(face, str(font_dir/file)))
pdfmetrics.registerFontFamily('CV', normal='CV', bold='CVBold')
navy, ink, blue, orange = [colors.HexColor(x) for x in ['#101c35','#263247','#185797','#ca5b19']]
styles = {
 'body': ParagraphStyle('Body',fontName='CV',fontSize=10,leading=14.1,textColor=ink,spaceAfter=7),
 'title': ParagraphStyle('Title',fontName='CVBold',fontSize=29,leading=34,textColor=navy,spaceAfter=6),
 'sub': ParagraphStyle('Sub',fontName='CVBold',fontSize=12,leading=17,textColor=blue,spaceAfter=10),
 'section': ParagraphStyle('Section',fontName='CVBold',fontSize=15,leading=20,textColor=navy,spaceBefore=12,spaceAfter=9),
 'role': ParagraphStyle('Role',fontName='CVBold',fontSize=11,leading=15,textColor=blue,spaceAfter=4),
 'meta': ParagraphStyle('Meta',fontName='CV',fontSize=9,leading=13,textColor=ink,spaceAfter=6),
 'bullet': ParagraphStyle('Bullet',fontName='CV',fontSize=10,leading=14.1,textColor=ink,leftIndent=10,firstLineIndent=-8,spaceAfter=3),
}
story=[]
def p(text, kind='body'): return Paragraph(text,styles[kind])
def add(text,kind='body'): story.append(p(text,kind))
def section(text): add(text,'section')
def role(company,title,period,summary,bullets=(),stack=''):
    block=[p(company,'role'),p(escape(title)+' | '+period,'meta'),p(summary)]
    block += [p('- '+escape(b),'bullet') for b in bullets]
    if stack: block.append(p('<b>Tecnologias:</b> '+escape(stack),'meta'))
    block.append(Spacer(1,6));story.append(KeepTogether(block))
def footer(canvas,doc):
    canvas.setStrokeColor(orange);canvas.setLineWidth(2);canvas.line(42, A4[1]-30,A4[0]-42,A4[1]-30)
    canvas.setStrokeColor(colors.HexColor('#dce1e8'));canvas.setLineWidth(.5);canvas.line(42,39,A4[0]-42,39)
    canvas.setFont('CV',8);canvas.setFillColor(ink);canvas.drawString(42,25,'Ueide Santos | Backend .NET, arquitetura e IA aplicada')
    canvas.drawRightString(A4[0]-42,25,f'{doc.page}')

add('Ueide Santos','title')
add('Engenheiro de Software | Backend .NET','sub')
add('Osasco/SP, Brasil · <link href="mailto:usjunior@gmail.com" color="#185797">usjunior@gmail.com</link><br/><link href="https://www.linkedin.com/in/ueide-santos" color="#185797">linkedin.com/in/ueide-santos</link> · <link href="https://github.com/ueidesantos" color="#185797">github.com/ueidesantos</link>','meta')
section('Perfil profissional')
add('Desenvolvedor Backend .NET com experiência em sistemas críticos para bancos, fintechs e saúde. Trajetória que combina engenharia de software, liderança técnica, arquitetura moderna e integração de sistemas. Atuação com APIs, microsserviços, arquitetura hexagonal, Kafka, RabbitMQ e cloud.')
add('Pós-graduando em Engenharia de Software com IA, com foco em IA generativa, RAG, guardrails, observabilidade e privacidade por design.')
section('Experiência profissional')
role('Banco Safra','Engenharia de software','Atual','Desenvolvimento de soluções corporativas em ambiente bancário, conectando entendimento das regras de negócio, especificação e implementação.',[
'Desenvolvimento de front e backend, com atenção à consistência entre interface, regras e integrações.',
'Organização do trabalho com desenvolvimento orientado por especificações (SDD), traduzindo necessidades em tarefas e verificações.',
'Aplicação de SOLID, Clean Architecture e padrões de projeto para separar responsabilidades e facilitar a evolução do código.',
'Instrumentação e análise do comportamento da aplicação com observabilidade e métricas técnicas.'
])
role('GFT · Banco BMG','Engenheiro de Software Backend .NET Core','Set 2024 - Jun 2026','Modernização da esteira de pagamentos, contribuindo para escalabilidade, resiliência e desacoplamento de processos críticos.',[
'Evolução de APIs REST em .NET 10 e integração assíncrona via Kafka, RabbitMQ e AWS MSK.',
'Arquitetura hexagonal para isolamento de domínio e suporte a fluxos orquestrados com Camunda.',
'Liderança técnica na concepção do Worker de Recálculo de Valores para Empréstimos.',
'Aplicação de SOLID, Strategy, Abstract Factory, Factory Method, Template Method e Specification.'
],'.NET 10, Kafka, RabbitMQ, MSK, MongoDB, Oracle, Redis, Camunda')
role('Verity · InterPlayers','Engenheiro de Software Backend .NET Core','Jul 2021 - Jun 2024','Evolução do backend do aplicativo Healthy, suportando jornadas de onboarding, e-commerce e billing.',[
'Desenvolvimento e manutenção de APIs REST e evolução da arquitetura para escalabilidade.',
'Integração com serviços Azure e pipelines de dados; implementação de testes unitários.'
],'C#, .NET 8, SQL Server, Redis, RabbitMQ, Azure, Azure Data Factory, xUnit')


role('Altran · BTG Pactual','Engenheiro de Software Backend .NET Core','Nov 2020 - Jul 2021','Backend .NET em ambiente financeiro, com foco em integração, exigência técnica e qualidade de entrega.',stack='Backend .NET Core, APIs, integrações')
role('Repom · Edenred Brasil','Desenvolvedor Backend','Mar 2020 - Nov 2020','Desenvolvimento e análise de sistemas com plataforma Microsoft, APIs, mensageria e infraestrutura para aplicações corporativas.',stack='ASP.NET Core, Web API, C#, SQL Server, RabbitMQ, Kubernetes, Azure')
role('Unimed FESP','Analista Sr. · Líder Técnico','Set 2007 - Jan 2018','Liderança técnica, arquitetura corporativa, governança e sustentação de sistemas críticos no setor de saúde suplementar.',[
'Referência técnica para equipes de Negócios de TI, QA e Desenvolvimento.',
'Governança de processos apoiados por RUP, PMBOK, ITIL, COBIT, SCRUM, Lean IT e DevOps.',
'Acompanhamento de indicadores financeiros, produtividade e KPIs de sistemas críticos.',
'Definição de arquitetura corporativa orientada a serviços e atuação com o padrão TISS da ANS.',
'Participação em soluções comercializadas para outras Unimeds, como o Consultório Online.'
],'SOA, WCF, SQL Server, SharePoint, Azure DevOps')
role('Sage Brasil · Dotz Marketing · Rapp Collins','Primeira base técnica','1999 - 2007','Desenvolvimento web e plataforma Microsoft, consolidando a base prática para manutenção e evolução de sistemas corporativos.',stack='C#, VB.NET, ASP.NET, ADO.NET, SQL Server')
section('Competências técnicas')
for title, text in [
('Backend','C#, .NET 4.x, .NET Core, .NET 8, .NET 10, ASP.NET Core, Web API, workers e APIs REST.'),
('Arquitetura','Camadas, hexagonal, DDD, SOLID, microsserviços, CQRS e EDA.'),
('Mensageria e dados','Kafka, RabbitMQ, AWS MSK, MSMQ, SQL Server, Oracle, MongoDB, DynamoDB, MySQL e Redis.'),
('Cloud e qualidade','Azure, AWS, S3, Azure Data Factory, CI/CD, Azure DevOps, xUnit e observabilidade.'),
('IA aplicada','LLMOps, RAG, IA generativa, guardrails, privacidade por design e human-in-the-loop.')]:
 add('<b>'+title+':</b> '+text)

section('Formação acadêmica')
for school,course,period in [
('UNIPDS','Pós-graduação em Engenharia de Software com IA','2026 - 2027 · em curso'),
('IBTA','Pós-graduação em Engenharia de Software (SOA)','2008 - 2009'),
('FIAP','Graduação em Sistemas de Informação','2001 - 2004'),
('Colégio Padre Anchieta','Técnico em Processamento de Dados','1998 - 2000')]:
 add('<b>'+school+'</b> | '+course+'<br/>'+period)
section('Projetos públicos')
add('KISS AI Labs','role')
add('Nove laboratórios educacionais em .NET e Python: Ollama, RAG, MCP, SDD e agents, com código, especificações e limites de validação documentados.')
add('<link href="https://ueidesantos.github.io/kiss-ai-labs/" color="#185797">ueidesantos.github.io/kiss-ai-labs</link>','meta')
add('Neuro Care | Cognitive Report Generator for Consultation','role')
add('Laboratório educacional de IA generativa aplicada à saúde digital, desenvolvido durante a pós-graduação. Simula a organização de relatos cognitivos, funcionais e comportamentais em relatório não diagnóstico para conversa com profissional de saúde. Explora regras determinísticas, guardrails, auditoria, observabilidade, structured output, RAG e human-in-the-loop. Não diagnostica nem substitui avaliação médica.')
add('<link href="https://github.com/ueidesantos/neurocare-ai-lab" color="#185797">github.com/ueidesantos/neurocare-ai-lab</link>','meta')
section('Formação complementar')
for item in [
'Desenvolvedor.io: Desenvolvimento SPA com Angular.',
'Alura: C# Entrada e saída (I/O) com streams; Técnicas de refatoração de código; Collections: listas, arrays, listas ligadas, dicionários e filas.',
'FIAP: TOGAF Foundation - nível 1.',
'eBusiness: Planejamento e Gestão de Budget de TI; Métricas e Indicadores de TI.',
'Lambda3: Professional Scrum; Professional Scrum Master; ALM Essential.',
'Paideia Educação · IDORT: Contabilidade para não contadores.',
'OpenDreams: Comunicação e Oratória; Liderança Pessoal.',
'Brás Figueiredo: Windows Communication Foundation (WCF); Advanced Distributed Application Development; Microsoft Solution Architectures.',
'Jump Education: Arquitetura da Informação em Projetos WEB.',
'IDORT: Negociação.'
]: add(item)
output=ROOT/'assets/ueide-santos-cv.pdf'
SimpleDocTemplate(str(output),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=43,bottomMargin=53,title='Ueide Santos - Currículo profissional',author='Ueide Santos').build(story,onFirstPage=footer,onLaterPages=footer)
print(output)
