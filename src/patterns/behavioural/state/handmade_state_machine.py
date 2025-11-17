from enum import Enum


# we model a single phone call, so the final state is the on hook state
class State(Enum):
    OFF_HOOK = 0
    CONNECTING = 1
    CONNECTED = 2
    ON_HOLD = 3
    ON_HOOK = 4


class Trigger(Enum):
    CALL_DIALED = 0
    HUNG_UP = 1
    CALL_CONNECTED = 2
    PLACED_ON_HOLD = 3
    TAKEN_OFF_HOLD = 4
    LEFT_MESSAGE = 5


if __name__ == "__main__":
    rules = {
        State.OFF_HOOK: [
            # if phone is off the hook, when you dial a call you enter the connecting state
            (Trigger.CALL_DIALED, State.CONNECTING)
        ],
        State.CONNECTING: [
            # when in connecting state
            # if the call is hung up, you enter on hook state
            (Trigger.HUNG_UP, State.ON_HOOK),
            # if the call is answered (call connected), you enter the connected state
            (Trigger.CALL_CONNECTED, State.CONNECTED)
        ],
        State.CONNECTED: [
            # when you're in connected state
            # if the call is placed on hold, you enter the on hold state
            (Trigger.PLACED_ON_HOLD, State.ON_HOLD),
            # if the call is hung up, you enter on hook state
            (Trigger.HUNG_UP, State.ON_HOOK),
            # if a message is left, you enter the on hook state
            (Trigger.LEFT_MESSAGE, State.ON_HOOK)
        ],
        State.ON_HOLD: [
            # when the call is put on hold
            # if the call is taken off hold, you enter the connected state
            (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
            # if the call is hung up, you enter the on hook state
            (Trigger.HUNG_UP, State.ON_HOOK)
        ]
    }

    state = State.OFF_HOOK
    exit_state = State.ON_HOOK

    while state != exit_state:
        print(f"The phone is currently {state}")

        for i in range(len(rules[state])):
            t = rules[state][i][0]
            print(f"{i}: {t}")

        idx = int(input("Select a trigger: "))
        s = rules[state][idx][1]
        state = s

    print("We are done using the phone")
