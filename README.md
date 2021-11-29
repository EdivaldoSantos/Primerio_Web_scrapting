# Web Scraping

A Book Club é uma Startup de troca de livros. O modelo de negócio funciona com base na troca de livros pelos usuários, cada livro cadastrado pelo usuário, dá o direito à uma troca, porém o usuário também pode comprar o livro, caso ele não queira oferecer outro livro em troca.

Umas das ferramentas mais importantes para que esse modelo de negócio rentabilize, é a recomendação. Uma excelente recomendação aumenta o volume de trocas e vendas no site.

Você é um Data Scientist contrato pela empresa para construir um Sistema de Recomendação que impulsione o volume de trocas e vendas entre os usuários. Porém, a Book Club não coleta e nem armazena os livros enviados pelos usuários.

Os livros para troca, são enviados pelos próprios usuários através de um botão “Fazer Upload”, eles ficam visíveis no site, junto com suas estrelas, que representam o quanto os usuários gostaram ou não do livro, porém a Startup não coleta e nem armazena esses dados em um banco de dados.

Logo, antes de construir um sistema de recomendação, você precisa coletar e armazenar os dados do site. Portanto seu primeiro trabalho como um Data Scientist será coletar e armazenar os seguintes dados:

1. O nome do livro.
2. A categoria do livro.
3. O número de estrelas que o livro recebeu.
4. O preço do livro.
5. Se o livro está em Estoque ou não.


Localização dos dados 
Os dados para serem coletados e armazenados, estão disponíveis neste site. http://books.toscrape.com/

Esse site foi desenvolvido e disponibilizado especialmente para praticar web scraping. Não existe nenhum tipo de problema legal ao fazer a coleta de dados.

**Roteiro Sugerido para a Resolução:**

*Esse é o roteiro de resolução do desafio que eu sugiro:*

1. Faça o web scraper, necessariamente, utilizando a linguagem Python.
2. Utiliza a biblioteca Selenium do Python para navegar entre os links das categorias e as páginas.
3. Utiliza a biblioteca BeautifulSoup do Python para coletar os dados das páginas HTML.
4. Instale no seu computador e configure um banco de dados SQL Server Express.
5. Crie uma tabela para armazenar os dados.
6. Agende seu script para rodar todos os dias em um horário específico. ( Não tem problema armazenar dados repetidos, já que o site não tem atualizações diárias )
7. Garanta que seu script saiba lidar com possíveis erros e não pare de funcionar por qualquer problema ( internet lenta, página não encontrada, objeto não carregado, etc )
8. Salve seu projeto em um repositório público Github ou Bitbucket.
9. Escreva o README com todos os passos necessários, para que outras pessoas consigam usar sua solução.

**Tornar sua solução Profissionalmente Respeitada:**

Crie sua solução modularizada. O Script em Python deve salvar um arquivo csv em alguma pasta da sua máquina e então outro script em bash, deve fazer a inserção dos dados no banco de dados.

Sincronize esse dois script ( Python para coletar e salvar os dados e o Bash script para inserir no banco Postgres ).

Faça o gerenciamento desses jobs utilizando o Airflow ( Framework de gerenciamento de Jobs ). Um script só pode rodar, quando o outro terminar.

Paraleliza seu script de coleta. Crie workers que trabalham em paralelo, cada um coleta e armazena os dados dos livros de uma página.
