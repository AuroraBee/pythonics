# Ion-Module to fit Bot Framework, returns Keys if it hath been asked
# TODO: Design this to fit the Bot Framework and specific Use-Case (Only check "Numpad keys")

def keydown(key):
    if key == 1:
        return True
    return False

# This is a mockup, im tired.