01/03/2016
-Executar bigbang.py no servidor onde está o arquivo de configurações alterados, ele vai atualizar o segundo servidor;
-Necessário verificar como melhorar script para atualizar mais servidores;

INSTALL

1-Baixar script no server:
git clone https://pedroalpacheco@bitbucket.org/pedroalpacheco/update_files.git

2-Verificar a versão do python no server, recomenda-se a versão 2.7

3-Configuração no client:
	-Criar usuario no client;
	-Adicionar o novo usuario ao grupo do usuario da aplicação em:
		/etc/group

	-Dar pedrmissão chown para o novo usuario no /etc/sudoers:
	
		usuarionovo ALL=(root)NOPASSWD: /etc/init.d/tomcat7
		
		ou:
		
			Cmnd_Alias REBOOTOMCAT = /etc/init.d/tomcat7 restart
			# User privilege specification
			desenvolvimento ALL=(ALL) NOPASSWD: REBOOTOMCAT
			atualizapwm ALL=(ALL) NOPASSWD: REBOOTOMCAT
		
		
REQUERIDO:
apt-get install python-pip
apt-get install python-paramiko
pip install pysftp

---------------------------------------------------------------------
