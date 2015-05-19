def g(a,b,c):
    if c=='+':
        return '(' + a + ' + ' + b + ')'
    elif c=='-':
        return '(' + a + ' - ' + b + ')'
    elif c=='*':
        return '(' + a + ' * ' + b + ')'
    elif c=='/':
        if len(str(a))>2:
            return '(' + a + ')' + ' / ' + b
        else:
            return a + ' / ' + b


print(f('(1+2)','2','+'))