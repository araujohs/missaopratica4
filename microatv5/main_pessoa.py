from Pessoa import Pessoa 
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

p = Pessoa('João','11','2000-01-01',False)
p.atributosPessoa()

pf = PessoaFisica('Amanda','123','2016-06-21',False,'1990-06-21','147.258.369-55','987654')
pf.atributosPessoa()

pj = PessoaJuridica('Desenvolvedores S.A.','753','2018-08-12',False,'2018-01-25','11.222.333/0001-99')
pj.atributosPessoa()

p.nome = 'Cristiane'
p.numeroConta = '1'
p.dataAberturaConta = '2013-04-04'
p.status = False
p.atributosPessoa()

pf.nome = 'Cristina'
pf.numeroConta = '2'
pf.dataAberturaConta = '1999-03-12'
pf.status = True
pf.dataNascimento = '1965-05-25'
pf.cpf = '357.159.924-11'
pf.rg = '654321'
pf.atributosPessoa()

pj.nome = 'FullStack Ltda'
pj.numeroConta = '951'
pj.dataAberturaConta = '2010-07-12'
pj.status = True
pj.dataAberturaEmpresa = '2010-01-31'
pj.cnpj = '66.777.888/0001-99'
pj.atributosPessoa()