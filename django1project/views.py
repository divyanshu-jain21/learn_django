from django.http import HttpResponse
# for html page import
from django.shortcuts import render

# for html page rendering
def homePage(request):
#     data={
#         'title':'home page',
#         'bdata':'welcome to DJ eras',
#         # for list data
#         'clist':['React','javaScript','Django','python'],
#         # dict in list data fetch
#         'student_details':[
#             {'name':'divyanshu','phone':7000682084},
#             {'name':'anurag','phone':9876543211},
#             {'name':'bhopa','phone':5647381919},
#         ],
#         # if-elif-else statement
#         'numbers' : [10,20,30,40,50,60,70],
#     }
#     return render(request , "index.html" , data)
    return render(request , "index.html")
    

# normalrouting
def aboutUs(request):
  return render(request , "aboutus.html")

def course(request):
    return render(request , "course.html")

# dynamic routing
def teamsDetails(request,teamId):
    return HttpResponse(teamId)

# user form
def userForm(request):
    # for data getting and error handlink
    finalAns =0
    data ={}
    try:
        # ---------get method--------
        # n1=int(request.GET('num1'))
        # n2=int(request.GET('num2'))

        #if request.method=="GET":
        # n1=int(request.GET.get('num1'))
        # n2=int(request.GET.get('num2'))
        # print(n1+n2)
        # ---------end get method---------
        # --------post method------------
        if request.method=="POST":
             n1=int(request.POST.get('num1'))
             n2=int(request.POST.get('num2'))
             finalAns=n1+n2

             data={
                 "n1":n1,
                 "n2":n2,
                 "output":finalAns
             }
        #---------END POST METHOD--------    
        
    except:
        pass    

    return render(request , "userForm.html", data)