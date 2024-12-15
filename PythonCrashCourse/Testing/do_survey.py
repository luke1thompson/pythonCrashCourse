from survey import Survey

surv = Survey("Do you think I'm sexy?")
print("We are conducting a survey on whether or not the author is sexy.")
print("Please enter your views here. Enter 'q' to quit and view the results.")

while True:
    response = input("Do you think I'm sexy?\t")
    if response == 'q':
        break
    surv.store_response(response)
    
print("Thank you for participating, here are the results!")
surv.show_results()