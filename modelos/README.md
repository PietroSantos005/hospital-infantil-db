# Projeto nativo do Data Modeler

Os PDFs exportados estão em `docs/diagramas/`. O arquivo nativo `.dmd` e sua pasta de dados ainda não foram fornecidos para este pacote.

## Acrescentar o projeto editável

1. No Data Modeler, use **File → Save As** e salve uma cópia com o nome `Hospital_Infantil.dmd`.
2. Copie para esta pasta tanto `Hospital_Infantil.dmd` quanto a pasta `Hospital_Infantil` criada ao lado dele, incluindo suas subpastas.
3. Mantenha os dois nomes e sua posição relativa; salve todas as alterações antes de copiar.
4. Teste a cópia usando **File → Open** e abrindo o `.dmd`.
5. Inclua os dois itens no commit. O `.gitignore` ignora arquivos locais de sessão, mas permite os dados do modelo.

O `.dmd` contém referências aos arquivos da pasta associada. Copiar somente o `.dmd` não transporta o projeto completo. Os PDFs são representações visuais; o SQL descreve o schema e pode ser importado como DDL para reconstruir um modelo relacional, sem garantir o layout ou os displays originais.

Referência: [Oracle — Database Design e Saving Designs](https://docs.oracle.com/en/database/oracle/sql-developer-data-modeler/24.3/dmdug/data-modeler-concepts-usage.html).
