from config import REQUIRE_CONFIRMATION

DANGEROUS_ACTIONS = {
    "shutdown": "Shut down the computer?",
    "restart": "Restart the computer?",
    "lock": "Lock the computer?",
    "delete": "Delete files?",
}

def confirm(action):
    if not REQUIRE_CONFIRMATION:
        return True
    answer = input(f"JARVIS SECURITY: {DANGEROUS_ACTIONS.get(action, 'Confirm action?')} [y/N]: ").strip().lower()
    return answer in {"y", "yes"}
