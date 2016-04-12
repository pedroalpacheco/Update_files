# README #

Script atualiza determinado arquivo em varios servidores.

### What is this repository for? ###

* Quick summary
* Version

### How do I get set up? ###

* Summary of set up

    Executar bigbang.py no servidor onde está o arquivo de configurações alterados, ele vai atualizar o segundo servidor;

* Configuration

    1-Baixar script no server:

    git clone https://pedroalpacheco@bitbucket.org/pedroalpacheco/update_files.git
    
    ou 
    
    git clne git@github.com:pedroalpacheco/Update_files.git

    2-Verificar a versão do python no server, recomenda-se a versão 2.7

    3-Configuração no client:
        -Adicionar o novo usuario ao grupo do usuario da aplicação em:
        /etc/group
    
    4-Dar pedrmissão chown para o novo usuario no /etc/sudoers:

        usuarionovo ALL=(root)NOPASSWD: /etc/init.d/tomcat7

    ou:

        Cmnd_Alias REBOOTOMCAT = /etc/init.d/tomcat7 restart
        # User privilege specification
        desenvolvimento ALL=(ALL) NOPASSWD: REBOOTOMCAT
        atualizapwm ALL=(ALL) NOPASSWD: REBOOTOMCAT

* Dependencies

    apt-get install python-pip

    apt-get install python-paramiko

    pip install pysftp



* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact
