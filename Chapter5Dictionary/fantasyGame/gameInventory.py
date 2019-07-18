
myStuff ={'rope' : 1, 'torch' : 6, 'gold coin' : 42, 'dagger' : 1, 'arrow' : 12}

def displayInventory(inventory):
    print('Inventory:')
    itemsTotal = 0
    for k , v in inventory.items():
        print(f'{v} {k}')
        itemsTotal += v
    print("Total items " + str(itemsTotal))
    
# displayInventory(myStuff)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}

def addInventory(inventory,loot):
    for i in range(len(loot)):
        if loot[i] in inventory:
            inventory[loot[i]] = inventory[loot[i]] + 1
        else:
            inventory.setdefault(loot[i],1)
    return inventory

inv = addInventory(myStuff, dragonLoot)

displayInventory(inv)