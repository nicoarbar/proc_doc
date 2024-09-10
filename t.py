a = {
    "Parameters":{
        "0":"nombre",
        "1":"producto",
        "2":"firma"
    },
    "Value":{
        "0":" Nicolas",
        "1":" Proc Doc",
        "2":" Aragon Barrero Nicolas"
    }
}

n_params = len(a["Parameters"])
for i in range(0,n_params):
    j = str(i)
    print(a["Parameters"][str(i)], a["Value"][str(i)])

for i, j in a.items():
    print('key: ',i)
    print('val: ',j)