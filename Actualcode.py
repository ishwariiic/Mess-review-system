mess_data ={}
mess_name={}

mess_name= input("Enter name of mess -")
def mess_owner_input():
    num = int(input("Enter the number of messes you want to add: "))
    for i in range(num):
        mess_name = input("Enter the name of your mess: ")
        location = input("Enter the location: ")
        dinner = input("Enter today's dinner menu: ")
        lunch= input("Enter today's lunch menu: ")
        waiting_time = input("Enter approximate  waiting time: ")
        mess_data[mess_name] = {"location": location, "Lmenu":lunch , "Dmenu":dinner, "waiting_time": waiting_time}
        print("Data for ",mess_name," submitted successfully!")


def student_view_data():
    print("Available Messes in your area are : ")
    for mess_name, data in mess_data.items():
        print("Name of the mess: ",mess_name)
        print("The mess is located in :" ,data['location'])
        print("Dinner Menu " ,data['Dmenu'])
        print("Lunch Menu: ",data['Lmenu'])
        print("Approximate waiting time " ,data['waiting_time'])
        if mess_name in reviews:
            print(f"Reviews: {', '.join(reviews[mess_name])}")
        print("\n")
reviews = {}
rating= int(input("How would you rate the mess on a scale of 1 to 5"))
def student_review():
    mess_name = input("Enter the name of the mess you want to review: ")
    review = input("Write your review:  ")
    rating= int(input("How would you rate the mess on a scale of 1 to 5"))
    
    if mess_name in reviews:
        reviews[mess_name].append(review)
    else:
        reviews[mess_name] = [review]
    
    print("Review submitted successfully!")
print("Reviews of previous messes")
print(mess_name,"is rated ",rating," out of 5")

while True:
    print("1. If you are a mess owner, input mess data")
    print("2. Student: If you are a student,press 2 to view mess and reviews")
    print("3. If you want to read reviews and ratings")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        mess_owner_input()
    elif choice == "2":
        student_view_data()
        student_review()
    elif choice=="3":
       student_review()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
