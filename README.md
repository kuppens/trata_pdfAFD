# Tratamento de Arquivos para upload no AFD
Na v1 deste programa, a funcionalidade desenvolvida é a separação de PDF's com base em seu tamanho, em MB.
## Operação
Como o SIGEPE aceita apenas arquivos iguais ou menores a 120mb, faz-se necessário separação de PDF's em determinado número de partes, diretamente proporcional ao tamanho do arquivo original. Optou-se por esta alternativa visto que a compressão dos PDF's iria resolver a problemática em raros casos, devido ao grande tamanho dos arquivos.
## Conversão
Por não termos, atualmente, licença de serviço de conversão OCR via API, optamos por realizar a conversão via apliativo PDF24. As funções de remove_digit destinam-se a tratar o resultado da conversão, para retornar o nome dos arquivos ao formato original.