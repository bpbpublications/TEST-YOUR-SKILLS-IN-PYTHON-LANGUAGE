def kungfu(*args):
    fighters = []
    for names in args:               
        fighters.append(names)
    return fighters

print(kungfu('Po','Shifu','Oogway'))