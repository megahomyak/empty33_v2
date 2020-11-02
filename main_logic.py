import asyncio
import random
import traceback

import aiohttp
import simplest_logger

from vk import vk_constants
from vk.vk_worker import VKWorker


class MainLogic:

    def __init__(
            self, vk_worker: VKWorker, logger: simplest_logger.Logger) -> None:
        self.vk_worker = vk_worker
        self.logger = logger

    async def future_done_callback(
            self, text: str, peer_id: int, future: asyncio.Future) -> None:
        exc = future.exception()
        if exc:
            exc_traceback_text = "".join(
                traceback.TracebackException.from_exception(exc).format()
            )
            self.logger.error(
                f"Текст сообщения: \"{text}\". Ошибка: {exc_traceback_text}"
            )
            await self.vk_worker.reply(
                peer_id,
                (
                    f"При обработке команды \"{text}\" произошла ошибка! Какая "
                    f"нахер ошибка, я же человек..."
                )
            )

    async def handle_message(
            self, text: str, peer_id: int, from_id: int) -> None:
        if f"[club{vk_constants.GROUP_ID}|@{vk_constants.TAG}]" in text:
            await self.vk_worker.reply(
                peer_id, random.choice(
                    [
                        *vk_constants.REPLIES,
                        f"Эй! Я тоже так могу! [id{from_id}|Тык!]"
                    ]
                )
            )

    async def listen_for_messages(self) -> None:
        async for event in self.vk_worker.listen():
            if event["type"] == "message_new":
                message_info: dict = event["object"]["message"]
                text: str = message_info["text"]
                peer_id: int = message_info["peer_id"]
                asyncio.create_task(
                    self.handle_message(
                        text, peer_id, message_info["from_id"]
                    )
                ).add_done_callback(
                    lambda future: asyncio.create_task(
                        self.future_done_callback(text, peer_id, future)
                    )
                )


async def main():
    async with aiohttp.ClientSession() as session:
        main_logic = MainLogic(
            VKWorker(
                session,
                vk_constants.TOKEN,
                vk_constants.GROUP_ID
            ),
            simplest_logger.Logger(
                "errors.log"
            )
        )
        await main_logic.listen_for_messages()


if __name__ == '__main__':
    asyncio.run(main())
