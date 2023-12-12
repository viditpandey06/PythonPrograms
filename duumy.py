def procedural(val1): 
    try: 
        sum1=0 
        for item in str(val1):
            sum1+=int(item_val)
    except TypeError:
        print("Type error occurred")
    finally:
        print("Finally in function")   
try: 
    procedural(792)
    print("Try handled")
except ValueError:
    print("Value error occurred")
except NameError:
    print("Name error occurred")
finally:
    print("Finally in main")