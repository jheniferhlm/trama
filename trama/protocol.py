class Protocol:
    def parse(self, message):
        messages = message.split(' ', 2)
        match messages[0]:
            case 'PUBLISH':
                if len(messages) == 3:
                    return messages[0], messages[1], messages[2]
                else:
                    raise ValueError("Invalid command")
            case 'CONSUME':
                if len(messages) == 2:
                    return messages[0], messages[1], ""
                else:
                    raise ValueError("Invalid command")
            case _:
                raise ValueError("Invalid command")