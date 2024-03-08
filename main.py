def rule_action(perception, rules):
    if perception == "reboot":
        return "reset"
    else:
        return rules.get(perception, "undefined")


def main():
    rules = {"coin": "ask-code", "c1": "serve c1", "c2": "serve c2", "c3": "serve c3"}

    while True:
        print("Write the perception you want to:")
        perception = input()

        action = rule_action(perception, rules)
        print(action)

main()
