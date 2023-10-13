import random
import os

import hikari
import pymongo


opperado = hikari.GatewayBot(os.environ["FICHA_DE_OPPERADO"])
cliente_banco_de_dados = pymongo.MongoClient(os.environ["LINHA_DE_CONEXAO_DO_MONGODB_DE_OPPERADO"])

xingamentos = cliente_banco_de_dados["opperado"]["opperado"].find_one()["xingamentos"]
calabocamentos = cliente_banco_de_dados["opperado"]["opperado"].find_one()["calabocamentos"]
contador_de_mensagens_do_tutu = 0


@opperado.listen(hikari.MessageCreateEvent)
async def xingamento_de_tutu(evento):
	global xingamentos
	if evento.content.lower() == "o tutu é":
		await evento.message.respond(random.choice(xingamentos))


@opperado.listen(hikari.MessageCreateEvent)
async def cala_a_boca(evento):
	global calabocamentos
	global contador_de_mensagens_do_tutu
	if evento.message.author.id == os.environ.get("ID_DO_TUTU", 624365838610202624):
		contador_de_mensagens_do_tutu += 1
	if contador_de_mensagens_do_tutu == 30:
		contador_de_mensagens_do_tutu = 0
		await evento.message.respond(random.choice(calabocamentos))


opperado.run()
