def get_body(data, indentifier):
    lines = []
    for itme in data:
        line = ''
        for key, val in item.items():
            if(key == indentifier):
                line = str(val) + ',\n' + line
            else:
                line += key + ' = \t' + str(val) + ',\n'
        lines.append(line)
    return lines


def formatter(data, record_type, indentifier='id'):
    bodies = get_body(data, indentifier)
    text = ''
    for item in bodies:
        text += '@' + record_type + '{' + item + '}'
    return text
