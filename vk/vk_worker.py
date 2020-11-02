import random

from simple_avk import SimpleAVK

from vk import vk_constants


class VKWorker(SimpleAVK):

    async def reply(self, peer_id: int, text: str) -> None:
        divided_text = (
            text[i:i + vk_constants.SYMBOLS_LIMIT]
            for i in range(
                0,
                len(text),
                vk_constants.SYMBOLS_LIMIT
            )
        )
        for part in divided_text:
            await self.call_method(
                "messages.send",
                {
                    "message": part,
                    "peer_id": peer_id,
                    "random_id": random.randint(-1_000_000, 1_000_000)
                }
            )
