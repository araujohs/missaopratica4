from Pessoa import Pessoa 

p = Pessoa('João','2000-01-01','000.111.222-33','15975388-1',False)

attrs = vars(p)

print('Instância da classe Pessoa')
print(', '.join("%s: %s" % item for item in attrs.items()))
print("="*10)

#
p.nome = "Ana"
p.dataNascimento = "2002-03-01"
p.cpf = "987.654.321-14"
p.rg = "321654-9"
p.status = False

print('Instância da classe Pessoa')
print(', '.join("%s: %s" % item for item in attrs.items()))
print("="*10)
