'''assuming 
a = length of tail
x = length of loop from start to meeting point
y = remaining distance between meeting point and loop start

turtle travels = a + x
rabbit travels = a + x + y + x

multiply turtle by 2 since twice of turtle equals rabbits distance

2(a+x) = 2x + a + y
2a = a + y
a = y

therefore the meeting point back to cycle start distance is 
equal to the tail to cycle start distance '''


def loop_start(ll):

    turtle = ll.head.next
    rabbit = ll.head.next.next

    while rabbit and rabbit.next:
        rabbit = rabbit.next.next
        turtle = turtle.next
        if turtle is rabbit:
            break

    if not rabbit or rabbit.next:
        return None

    turtle = ll.head
    while turtle is not rabbit:
        turtle = turtle.next
        rabbit = rabbit.next

    return turtle
