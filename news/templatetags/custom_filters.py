from django import template

register = template.Library()


@register.filter(name='Censor')
def Censor(value):
    stop_list = ['пиздуйте', 'херсон', 'test']
    sentence = value.split()
    for i in stop_list:
        for words in sentence:
            if i in words:
                pos = sentence.index(words)
                sentence.remove(words)
                sentence.insert(pos, '*' * len(i))
    return " ".join(sentence)
