import numpy as np

def shift(org, offset):
    if offset == 11:
        return [1] * 11 + [0]
    offset = len(org) - offset
    if offset == 0:
        return org
    return org[-offset:] + org[:len(org) - offset] + [1]

def helper(offset: int):
    #res = ([0] * (offset)) + [1] + ([0] * (11 - offset)) +  
    res = shift(
                [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0], offset
            )
    return res


generator = np.array([helper(x) for x in range(12)])
control = generator
msg = [1, 1] + 5 * [0, 1]
msg = np.array(msg)
print(generator)
print(msg)
sent = np.dot(generator, msg.T) % 2
print(sent)
print(np.dot(control, sent) % 2)
