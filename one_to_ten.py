# count to ten
count = 0

while count < 10:
    should_run = True
    
    while should_run:
        count = count + 1
        print(count)
        if count >= 10:
            should_run = False 