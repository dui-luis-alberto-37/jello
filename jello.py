#!/usr/bin/env python3
# by lgarciaorozco6@gmail.com
# GNU/GPL License

size_limon = 10
size_strawberry = 10

def slice(flavor):
    global size_limon
    global size_strawberry
    if 'limon' in flavor:
        if size_limon > 0:
            size_limon -= 1
            return True
        else: return False

    elif: 'strawberry' in flavor:
        if size_limon > 0:
            size_strawberry -= 1
            return True
        else: return False

strawberry_watter = 1.0 #L
strawberry_size = 10
strawberry_flavor = 'strawberry'
strawberry_grenetina = 15.0 #g
