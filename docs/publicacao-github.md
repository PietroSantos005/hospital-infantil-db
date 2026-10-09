# Publicar no GitHub

## Informações do repositório

- **Nome sugerido:** `hospital-infantil-db`
- **Descrição:** Modelagem de banco de dados para gestão de um hospital infantil, com Oracle SQL, DERs, regras de integridade e documentação de segurança e LGPD.
- **Topics sugeridos:** `database`, `database-design`, `data-modeling`, `oracle`, `sql`, `healthcare`, `academic-project`, `lgpd`.
- **Primeiro commit:** `Organiza modelagem hospitalar, DDL, diagramas e documentação`

## Pelo navegador

1. Extraia o ZIP recebido.
2. Crie um repositório no GitHub com o nome sugerido. Escolha **Public** se quiser exibi-lo no portfólio.
3. Como este pacote já inclui README e `.gitignore`, deixe essas opções de criação desmarcadas para usar os arquivos fornecidos.
4. Na página do repositório, escolha **uploading an existing file**; em um repositório já iniciado, use **Add file → Upload files**.
5. Arraste o conteúdo de `hospital-infantil-db` para a área de upload, preservando as pastas. O `README.md` deve ficar na raiz do repositório, e não dentro de uma segunda pasta `hospital-infantil-db`.
6. Confirme o upload dos arquivos e pastas, incluindo `.gitignore` e `.gitattributes`.
7. Escreva a mensagem do primeiro commit e conclua em **Commit changes**.
8. Abra o README e confira se a imagem e os links aparecem.

O ZIP é um pacote de transporte: publique os arquivos extraídos para que o GitHub apresente a documentação e permita navegar pelo SQL e pelos modelos.

## Com Git instalado

Abra o terminal dentro da pasta extraída `hospital-infantil-db`. Crie primeiro um repositório vazio no GitHub e use sua URL real no comando de remote:

```bash
git init
git add .
git commit -m "Organiza modelagem hospitalar, DDL, diagramas e documentação"
git branch -M main
git remote add origin URL_DO_SEU_REPOSITORIO
git push -u origin main
```

`URL_DO_SEU_REPOSITORIO` deve ser substituída pela URL exibida no GitHub. Este procedimento pressupõe repositório remoto vazio e autenticação Git já configurada.

## Créditos e apresentação

Complete a seção de autoria do README com os nomes dos integrantes e descreva sua contribuição individual. Uma licença de uso pode ser adicionada quando os autores definirem os termos; este pacote não escolhe uma licença em nome da equipe.

O projeto nativo pode ser acrescentado em `modelos/` quando estiver disponível. A documentação de portfólio não substitui o documento acadêmico nas normas ABNT.

Depois de publicar, fixe o repositório no seu perfil. Uma descrição curta para o portfólio:

> Projeto acadêmico de modelagem de banco de dados para gestão hospitalar infantil, com 12 tabelas, relacionamentos, constraints Oracle e documentação técnica sobre integridade e proteção de dados.

Referência: [GitHub — Adding a file to a repository](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).
