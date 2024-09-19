from django.shortcuts import render, redirect
from organs.models import Organ_systems, Organs
from .forms import Add_organ, Search_organ

# Create your views here.
def organ_home(response):
    organ_systems = []
    for i in range(len(Organ_systems.objects.all())):
        organ_systems.append((Organ_systems.objects.get(id = i+1)))
    return render(response, "organs/home.html", {"title":"Organ_systems","organ_systems":organ_systems})




def add_organ(response):
    form = Add_organ(response.POST or None)
    # print(f"\033[1;32;40m    \n\033[0m")
    all_organ_systems = []
    for i in range(len(Organ_systems.objects.all())):
        all_organ_systems.append(Organ_systems.objects.get(id = i+1).organ_system)
    
    form.fields["organ_system"].choices = [(organ, organ.capitalize()) for organ in all_organ_systems]
    
    if response.method == "POST":        
        if form.is_valid():
            form_organ_system = form.cleaned_data["organ_system"]
            form_organ_name = form.cleaned_data["organ_name"]
            form_organ_function = form.cleaned_data["organ_function"]
            # print(organ_system, organ_name , organ_function)
            print(f"\033[1;32;40m FORM_DATA  \n{form_organ_system} {form_organ_name}  {form_organ_function}\n\033[0m")
            
            
            all_organs = Organ_systems.objects.get(organ_system = form_organ_system).organs_set.all()
            duplicate_found = False
            for organ in all_organs:
                if organ.organ_name == form_organ_name:
                    duplicate_found = True
                    print(f"\033[1;32;40m  \nduplicate_found  \n\033[0m")
            if duplicate_found != True:
                    new = Organ_systems.objects.get(organ_system = form_organ_system).organs_set.create(organ_name = form_organ_name, organ_function= form_organ_function)
                    new.save()
                    print(new)
            
        else:
            
            print("hola")
        # print(form)            
    return render(response, "organs/add_organ.html", {"title":"Add organ", "form":form,  "all_organ_systems":all_organ_systems})





def search_organ(response):
    form = Search_organ(response.POST or None)
    all_organ_systems = [""]
    message = ""
    
    for organ_system in (Organ_systems.objects.all()):
        all_organ_systems.append(organ_system.organ_system)
    
    form.fields["organ_system"].choices = [(organ, organ.capitalize()) for organ in all_organ_systems]

    if response.method == "POST":
        if form.is_valid():
            form_organ_system = form.cleaned_data["organ_system"]
            form_organ_name = form.cleaned_data["organ_name"]
            # print(form_organ_system)
            print(f"\033[1;32;40m  {form_organ_name} {form_organ_system}  \n\033[0m")
            print(f":{type(form_organ_name)}:")
            if form_organ_system!="":
                if form_organ_name!="":
                    # "NONE OF THEM ARE EMPTY"
                    # redirect to organ_system/organ_name
                    found_organ = None
                    try:
                        found_organ = Organs.objects.get(organ_name = form_organ_name)
                    except:
                        message = "Invalid Organ_name" 
                    if found_organ != None:
                        return redirect(f"http://127.0.0.1:8000/{form_organ_system}/{form_organ_name}")
                                

                else:
                    # SYSTEM IS NOT EMPTY BUT ORGAN IS
                    print("redirect to organ_system_individual page")
                    return redirect(f"http://127.0.0.1:8000/{form_organ_system}")
            else:
                if form_organ_name!="":
                    # SYSTEM IS EMPTY BUT ORGAN IS NOT
                    print("redirect to one organ only page")
                    found_organ = None
                    try:
                        found_organ = Organs.objects.get(organ_name = form_organ_name)
                    except:
                        message = "Invalid Organ_name" 
                    if found_organ != None:
                        organ_system = Organs.objects.get(organ_name = form_organ_name).organ_system
                        message = f"{form_organ_name} is a part of {organ_system}_system"
                        return redirect(f"http://127.0.0.1:8000/{organ_system}/{form_organ_name}")
                else:
                    # BOTH OF THEM ARE EMPTY
                    message = "Enter organ_system or organ_name dumbass"
                    print("return to search page")

        else:
            print(form)
            print("form not valid")
    return render(response, "organs/search_organ.html", {"title":"search_organ", "form" : form, "all_organ_systems" : all_organ_systems, "message":message})


# dont take out request, or it wont work
def individual_organ_system(request, organ_system):
    #                     # WITH DICT
    # organs = {}
    
    # for i in range(len(Organ_systems.objects.get(organ_system = organ_system).organs_set.all())):
    #     try:            
    #         organs_query = Organ_systems.objects.get(organ_system=organ_system).organs_set.all()            
    #         for organ in organs_query:
    #             organs[organ.organ_name] = organ.organ_function            
    #     except:
    #         pass
    organs = []
    organs_query = Organ_systems.objects.get(organ_system = organ_system).organs_set.all()
    print(organs_query)
    for organ in organs_query:
        organs.append(organ.organ_name) 
    
    return render(request, "organs/individual_organ_system.html", {"title":organ_system.title(),"organs": organs, "organ_system":organ_system})


def individual_organ(request, organ_system, organ):
    try:
        found_organ = Organ_systems.objects.get(organ_system=organ_system).organs_set.get(organ_name = organ)
    except:
        pass
    if found_organ :
        organ_name = found_organ.organ_name
        organ_function = found_organ.organ_function
        return render(request, "organs/individual_organ.html", {"title":found_organ, "organ_name":organ_name, "organ_function":organ_function})
    return render(request, "organs/individual_organ.html", {"title":"bal"})
    