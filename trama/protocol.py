class Protocol:
    def parse(self, message):
        messages = message.split(' ', 2)
        match messages[0]:
            case 'PUBLISH':
                return messages[0], messages[1], messages[2]
            case 'CONSUME':
                return messages[0], messages[1], ""