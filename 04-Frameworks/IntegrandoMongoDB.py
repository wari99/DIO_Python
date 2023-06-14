from pprint import pprint
import pymongo as pyM

conectando = pyM.MongoClient("mongodb+srv://uuuuuuu:ssssssss@link-aqui")

#Criacao do banco de dados e da collection

db = conectando.bank
collection = db.bank_collection
print(db.bank_collection)

contas = [{
	"nome": "Mariana"
	"cpf": "19900977721"
	"endereco": "Universidade do Estado do Rio de Janeiro, RJ"
	"conta":[{
		"tipo": "CC"
		"agencia": "0001"
		"numero": "101"
		"saldo": 651
	},
	{
		"tipo": "CP"
		"agencia": "0001"
		"numero": "109"
		"saldo": 2150
	
	}]
},
{
	"nome": "Arthur"
	"cpf": "18770079929"
	"endereco": "Instituto de Matematica e Estatistica, UERJ"
	"conta":[{
		"tipo": "CC"
		"agencia": "0001"
		"numero": "111"
		"saldo": 1202.50
	},
	{
		"tipo": "CP"
		"agencia": "0001"
		"numero": "112"
		"saldo": 0
	}]
}
]


clientes = db.clientes
resultado = clientes.insert_many(contas)
print(resultado.inserted_ids)

print(db.clientes.find_one({"cliente": "Mariana"}))
