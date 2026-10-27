from core.command_router import CommandRouter

def test_router():
    r = CommandRouter()
    assert r.route("open notepad")[0] == "open_app"
    assert r.route("volume up")[0] == "volume_up"
    assert r.route("take a screenshot")[0] == "screenshot"
    assert r.route("hello")[0] == "chat"

if __name__ == "__main__":
    test_router()
    print("Router tests passed.")
