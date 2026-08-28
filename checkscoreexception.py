def check_score():
    try:
        print(score)
        score=90
    except UnboundLocalError:
        print("Error:you must assign the value first")
check_score()
