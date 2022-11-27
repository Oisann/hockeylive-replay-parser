import json
import re

def parse(line):
    # Skip empty lines
    if len(line) == 0:
        return
    line = line[:-1]
    # make sure we're on a dumped json line, like we expect.
    x = re.search("^\d+: ", line)
    if x:
        _, finish = x.span()
        # we skip these as they mean the connection timed out because nothing was happening (?)
        y = re.search("^\d+: \d+ \d+$", line)
        if not y:
            line = line[finish:]
            data = json.loads(line)
            # Match data is stored in the m variable
            match_data = data["m"]
            for current_data in match_data:
                relevant_data = current_data["d"]
                if len(relevant_data) > 0:
                    event = relevant_data["EventType"]
                    if event == 1:
                        # _delete
                        assert False, f"Delete {relevant_data}"
                    elif event == 2:
                        # _timer
                        assert False, f"Timer {relevant_data}"
                    elif event == 104:
                        # faceOff
                        assert False, f"Face Off {relevant_data}"
                    elif event == 109:
                        # gameWinningGoal
                        assert False, f"Game Winning Goal {relevant_data}"
                    elif event == 101:
                        # goal
                        assert False, f"Goal {relevant_data}"
                    elif event == 102:
                        # penalty
                        assert False, f"Penalty {relevant_data}"
                    elif event == 107:
                        # penaltyShot
                        assert False, f"Penalty Shot {relevant_data}"
                    elif event == 4:
                        # period
                        assert False, f"Period {relevant_data}"
                    elif event == 105:
                        # playerTime
                        assert False, f"Player Time {relevant_data}"
                    elif event == 108:
                        # shootout
                        assert False, f"Shootout {relevant_data}"
                    elif event == 103:
                        # shot
                        assert False, f"Shot {relevant_data}"
                    elif event == 3:
                        # team
                        assert False, f"Team {relevant_data}"
                    elif event == 106:
                        # timeOut
                        assert False, f"Timeout {relevant_data}"
                    elif event == 208:
                        # handballGoalie
                        assert False, "handballGoalie event????"
                    elif event == 205:
                        # handballInjury
                        assert False, "handballInjury event????"
                    elif event == 202:
                        # handballInterception
                        assert False, "handballInterception event????"
                    elif event == 204:
                        # handballPenalty
                        assert False, "handballPenalty event????"
                    elif event == 203:
                        # handballPenaltyShot
                        assert False, "handballPenaltyShot event????"
                    elif event == 201:
                        # handballShot
                        assert False, "handballShot event????"
                    elif event == 206:
                        # handballTechnicalFault
                        assert False, "handballTechnicalFault event????"
                    elif event == 207:
                        # handballTimeOut
                        assert False, "handballTimeOut event????"
                    else:
                        assert False, f"Unknown event {relevant_data}"
                else:
                    assert False, f"No relevant data, {current_data}"

def main() -> int:
    with open("match.log") as f:
        for line in f.readlines():
            parse(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
