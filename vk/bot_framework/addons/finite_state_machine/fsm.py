from vk.bot_framework.dispatcher.storage import AbstractAsyncStorage


class State:
    def __init__(self, title: str, storage: AbstractAsyncStorage):
        self.title = title
        self.storage = storage


class FiniteStateMachine:
    def __init__(self, storage: AbstractAsyncStorage):
        self.storage = storage

    async def set_state(
        self, state: State, uid: int, extra_state_data=None,
    ) -> None:
        if extra_state_data is None:
            extra_state_data = {}
        uid = str(uid)

        if await self.storage.exists(uid):
            storage_data = await self.storage.get(uid)
            storage_data["__vk.py_fsm_state__"] = state.title
            storage_data.update(extra_state_data)
            return await self.storage.update(uid, storage_data)

        storage_data = {"__vk.py_fsm_state__": state.title}
        storage_data.update(extra_state_data)
        return await self.storage.place(uid, storage_data)

    async def add_data(self, uid: int, state_data: dict) -> None:
        uid = str(uid)

        data = await self.storage.get(uid)
        data.update(state_data)
        return await self.storage.update(uid, data)

    async def get_data(self, uid: int) -> None:
        uid = str(uid)
        return await self.storage.get(uid)

    async def finish(self, uid: int) -> None:
        uid = str(uid)
        return await self.storage.delete(uid)
