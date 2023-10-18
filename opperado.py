from typing import Final
import random
import os

import hikari
import pymongo


opperado: Final[hikari.GatewayBot] = hikari.GatewayBot(os.environ["FICHA_DE_OPPERADO"])
cliente_banco_de_dados: Final[pymongo.MongoClient] = pymongo.MongoClient(
	os.environ["LINHA_DE_CONEXAO_DO_MONGODB_DE_OPPERADO"]
)

xingamentos: list[str] = cliente_banco_de_dados["opperado"]["opperado"].find_one()["xingamentos"]
calabocamentos: list[str] = cliente_banco_de_dados["opperado"]["opperado"].find_one()["calabocamentos"]
contador_de_mensagens_do_tutu: int = cliente_banco_de_dados["opperado"]["opperado"].find_one()[
	"contador_de_mensagens_do_tutu"
]


@opperado.listen()
async def xingamento_de_tutu(evento: hikari.MessageCreateEvent) -> None:
	global xingamentos
	if evento.content.lower() == "o tutu é":
		await evento.message.respond(random.choice(xingamentos))


def atualizar_a_contagem_do_tutu() -> None:
	cliente_banco_de_dados["opperado"]["opperado"].update_one(
		{}, {"$set": {"contador_de_mensagens_do_tutu": contador_de_mensagens_do_tutu}}
	)


@opperado.listen()
async def cala_a_boca(evento: hikari.MessageCreateEvent) -> None:
	global calabocamentos
	global contador_de_mensagens_do_tutu
	if evento.message.author.id == int(os.environ.get("ID_DO_TUTU", 624365838610202624)):
		contador_de_mensagens_do_tutu += 1
		atualizar_a_contagem_do_tutu()
	if contador_de_mensagens_do_tutu == 30:
		contador_de_mensagens_do_tutu = 0
		atualizar_a_contagem_do_tutu()
		await evento.message.respond(random.choice(calabocamentos))


opperado.run()
cliente_banco_de_dados.close()
