from typing import Final
import random
import os

import hikari
import pymongo


opperado: Final[hikari.GatewayBot] = hikari.GatewayBot(os.environ["FICHA_DE_OPPERADO"])
OPPERANTES: Final[list[int]] = [310169288432418817, 308358218839752704, 331650696585805825]
cliente_bd: Final[pymongo.MongoClient] = pymongo.MongoClient(os.environ["LINHA_DE_CONEXAO_DO_MONGODB_DE_OPPERADO"])

xingamentos: pymongo.cursor.Cursor = cliente_bd["opperado"]["xingamentos"].find()
xingamentos: list[str] = [documento["xingamento"] for documento in xingamentos]

calabocamentos: pymongo.cursor.Cursor = cliente_bd["opperado"]["calabocamentos"].find()
calabocamentos: list[str] = [documento["calabocamento"] for documento in calabocamentos]

contador_mensagens_tutu: int = cliente_bd["opperado"]["miscelânea"].find_one()["contador_de_mensagens_do_tutu"]


@opperado.listen()
async def xinga_tutu(evento: hikari.MessageCreateEvent) -> None:
	global xingamentos
	if evento.content.lower() == "o tutu é":
		await evento.message.respond(random.choice(xingamentos))


def atualiza_bd() -> None:
	cliente_bd["opperado"]["opperado"].update_one(
		{}, {"$set": {"contador_de_mensagens_do_tutu": contador_mensagens_tutu}}
	)


@opperado.listen()
async def calaboca_tutu(evento: hikari.MessageCreateEvent) -> None:
	global calabocamentos
	global contador_mensagens_tutu
	if evento.message.author.id == int(os.environ.get("ID_DO_TUTU", 624365838610202624)):
		contador_mensagens_tutu += 1
		atualiza_bd()
	if contador_mensagens_tutu == 30:
		contador_mensagens_tutu = 0
		atualiza_bd()
		await evento.message.respond(random.choice(calabocamentos))


@opperado.listen()
async def desliga(evento: hikari.DMMessageCreateEvent):
	if evento.content.lower() == "desliga" and evento.author_id in OPPERANTES:
		await evento.message.respond("Desligando...")
		await opperado.close()


opperado.run()
cliente_bd.close()
