# Como contribuir com o PTS-BR

Este arquivo mostra os tipos de contribuição e o procedimento de cada tipo.

Antes de contribuir, leia o [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## 1. Tipos de contribuição

| Tipo | Use |
|---|---|
| Pedido de mudança no dicionário (PMD) | Issue com o modelo "PMD". Ver [`05-governanca.md`](05-governanca.md), seção 7.2. |
| Pedido de mudança de regra (PMR) | Issue com o modelo "PMR". Ver [`05-governanca.md`](05-governanca.md), seção 7.7. |
| Erro na especificação, no linter ou no plugin | Issue com o modelo "Erro". |
| Correção de texto ou de código | Pull request. Ver a seção 3. |
| Problema de segurança | Não crie uma issue. Ver o [`SECURITY.md`](SECURITY.md). |

## 2. Antes de criar uma issue

1. Procure uma issue igual na lista de issues.
2. Para uma palavra, procure a palavra no [`03-dicionario.md`](03-dicionario.md) e no [`04-termos-tecnicos.md`](04-termos-tecnicos.md).
3. Escreva a frase de novo com palavras aprovadas. Se a frase nova tiver o mesmo significado, não crie o PMD.

## 3. Criar um pull request

1. Crie um fork do repositório e uma branch para a alteração.
2. Escreva cada texto novo em PTS-BR.
3. Não altere o [`03-dicionario.md`](03-dicionario.md) manualmente. Altere os arquivos `tools/d1.txt` a `tools/d4.txt` e gere o 03:

   ```shell
   python3 tools/build.py
   python3 tools/build.py --render 03-dicionario.md
   ```

4. Execute os testes e as verificações. Use o Python 3.9 ou mais novo:

   ```shell
   python3 tools/gerar_regras_dicionario.py --verificar
   python3 tools/check_spec.py --teste
   python3 tools/check_spec.py --spec --falhar
   python3 tools/check_spec.py --lista-branca --spec --meta 1
   ```

5. Corrija cada falha.
6. Crie o pull request. Preencha o modelo do pull request.

## 4. Revisão

- O mantenedor revisa cada pull request. O redator e o revisor de uma alteração são pessoas diferentes.
- O mantenedor decide os PMD e os PMR com os prazos e os critérios do [`05-governanca.md`](05-governanca.md), seções 7.4 e 7.5.
- Uma alteração das regras ou do dicionário entra numa versão nova. O [`CHANGELOG.md`](CHANGELOG.md) registra a alteração.

## 5. Licença

O texto do PTS-BR usa a licença CC BY 4.0. Com a sua contribuição, você aceita a publicação da contribuição com esta licença.
