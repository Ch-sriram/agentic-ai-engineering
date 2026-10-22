from random import randint
from tools import get_current_time, generate_password, roll_dice

TOOL_WORDS = {
    "time": {"time", "clock"},
    "dice": {"dice", "die"},
    "password": {"password", "passcode", "hash"}
}


def execute_tool(user_sanitized_prompt):
    user_prompt_words = set(user_sanitized_prompt.split())

    if user_prompt_words & TOOL_WORDS['time']:
        return f"\n🤖> Current time is: {get_current_time()}"

    if user_prompt_words & TOOL_WORDS['dice']:
        return f"\n🤖> Rolled a dice, and you got: {roll_dice()}"

    if user_prompt_words & TOOL_WORDS['password']:
        pass_len = randint(12, 30)
        return f"\n🤖> Generating a random password of length {pass_len}: {generate_password(pass_len)}"

    return
