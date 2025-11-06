from vyl.ai.chatloader import ai_chat_flush
from vyl.ai.memoryloader import ai_memorize
from vyl.ai.solver import solve
from vyl.platform.requirements import crash_if_cant_launch


def route(prompt: str):
    crash_if_cant_launch()

    if prompt.lower().startswith('remember'):
        ai_memorize(prompt)
        return

    if prompt.lower().startswith('flashbang'):
        ai_chat_flush()
        return

    solve(prompt)
