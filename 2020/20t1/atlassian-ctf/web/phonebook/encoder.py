base_words =  {
    'Infinity':        "(''+1/0)",  # -----f--i----n-----t----y-
    'true':            "(''+!!1)",  # ----ef--i----n---r-tu---y-
    'false':           "(''+!1)",   # ab--ef--i--l-n---rstu---y-
    '[object Object]': "(''+{})",   # abc-ef--ij-l-no--rstu---y-
}
base_charmap = {
    'a': base_words['false'] + '[1]',
    'b': base_words['[object Object]'] + '[2]',
    'c': base_words['[object Object]'] + '[5]',
    'd': None,
    'e': base_words['true'] + '[3]',
    'f': base_words['Infinity'] + '[2]',
    'g': None,
    'h': None,
    'i': base_words['Infinity'] + '[3]',
    'j': base_words['[object Object]'] + '[3]',
    'k': None,
    'l': base_words['false'] + '[2]',
    'm': None,
    'n': base_words['Infinity'] + '[1]',
    'o': base_words['[object Object]'] + '[1]',
    'p': None,
    'q': None,
    'r': base_words['true'] + '[1]',
    's': base_words['false'] + '[3]',
    't': base_words['Infinity'] + '[6]',
    'u': base_words['true'] + '[2]',
    'v': None,
    'w': None,
    'x': None,
    'y': base_words['Infinity'] + '[7]',
    'z': None
}

def encode_str(s, charmap):
    encoded = ""
    for c in s:
        if c in charmap:
            if charmap[c] is None:
                return False
            encoded += charmap[c] + '+'
        else:
            encoded += "'" + c + "'+"
    return encoded[:-1]

adv_words = {
    # From base                                                                                                  # abc-ef--ij-l-no--rstu---y-
    'function RegExp() {\n    [native code]\n}': "(''+(/a/)[" + encode_str('constructor', base_charmap) + "])",  # abc-efg-ij-l-nop-rstuv-xy-
    'function Number() {\n    [native code]\n}': "(''+(1)[" + encode_str('constructor', base_charmap) + "])"     # abc-efg-ij-lmnop-rstuv-xy-
}

adv_charmap = {
    'a': base_charmap['a'],
    'b': base_charmap['b'],
    'c': base_charmap['c'],
    'd': adv_words['function RegExp() {\n    [native code]\n}'] + '[34]',
    'e': base_charmap['e'],
    'f': base_charmap['f'],
    'g': adv_words['function RegExp() {\n    [native code]\n}'] + '[11]',
    'h': None,
    'i': base_charmap['i'],
    'j': base_charmap['j'],
    'k': None,
    'l': base_charmap['l'],
    'm': adv_words['function Number() {\n    [native code]\n}'] + '[11]',
    'n': base_charmap['n'],
    'o': base_charmap['o'],
    'p': adv_words['function RegExp() {\n    [native code]\n}'] + '[14]',
    'q': None,
    'r': base_charmap['r'],
    's': base_charmap['s'],
    't': base_charmap['t'],
    'u': base_charmap['u'],
    'v': adv_words['function RegExp() {\n    [native code]\n}'] + '[29]',
    'w': None,
    'x': adv_words['function RegExp() {\n    [native code]\n}'] + '[13]',
    'y': base_charmap['y'],
    'z': None
}

full_word = {}
full_word['function'] = lambda payload: "(({})["+encode_str('constructor', adv_charmap)+"]["+encode_str('constructor', adv_charmap)+"]("+encode_str('return', adv_charmap)+'+'+payload+"))()"
full_word['body']     = full_word['function'](encode_str(' document.body', adv_charmap))
full_word['[object Window]']   = "(''+"+full_word['function'](encode_str(' top', adv_charmap)) +')'

full_charmap = {
    'a': base_charmap['a'],
    'b': base_charmap['b'],
    'c': base_charmap['c'],
    'd': adv_charmap['d'],
    'e': base_charmap['e'],
    'f': base_charmap['f'],
    'g': adv_charmap['g'],
    'h': full_word['body'] + "["+encode_str('baseURI', adv_charmap)+"][0]",
    'i': base_charmap['i'],
    'j': base_charmap['j'],
    'k': full_word['body'] + "[" + encode_str('classList', adv_charmap) + "][" + encode_str('constructor', adv_charmap) + "][" + encode_str('name', adv_charmap) + "][5]",
    'l': base_charmap['l'],
    'm': adv_charmap['m'],
    'n': base_charmap['n'],
    'o': base_charmap['o'],
    'p': adv_charmap['p'],
    'q': None,
    'r': base_charmap['r'],
    's': base_charmap['s'],
    't': base_charmap['t'],
    'u': base_charmap['u'],
    'v': adv_charmap['v'],
    'w': full_word['[object Window]'] + '[13]',
    'x': adv_charmap['x'],
    'y': base_charmap['y'],
    'z': None
}

full_charmap['q'] = '({})[' + encode_str('constructor', adv_charmap) + '][' + encode_str('keys', full_charmap) + ']('+full_word['function'](encode_str(' top', adv_charmap))+')[40][0]'
full_charmap['z'] = '({})[' + encode_str('constructor', adv_charmap) + '][' + encode_str('keys', full_charmap) + ']('+full_word['function'](encode_str(' top', adv_charmap))+')[17][4]'

def encode_runnable(cmd):
    return full_word['function'](encode_str(' ' + cmd, full_charmap))
