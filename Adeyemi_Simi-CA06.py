# Adeyemi Simi  December 2021 CA-06.py
# Modularisation of actor list to produce alien names

# this function splits the names of the actors up
def create_actor(actor_list):
    actor_string =' '.join(actor_list)
    split_list = actor_string.split()

    givenNameList =(split_list[::2])
  
    familyNameList = (split_list[1::2])
   
    list_to_split(familyNameList,givenNameList,actor_list)

#this function creates the alien names 
def list_to_split(familyNameList,givenNameList,actor_list):
    family3List = []
    for i in (familyNameList):
        family3List.append(i[:3])
     
        
    given2List = []
    for i in (givenNameList):
        given2List.append(i[:2])

    alienList = [i + j for i, j in zip(family3List, given2List)]
    shortalienlist(alienList,actor_list)

#this function splits the list into vowels and non vowels and also provides a director name
def shortalienlist(alienList,actor_list):
    vowel = ['a','e','i','o','u']
    shortList = ["stean","venha", "blyph", "spiyu", "elbsa", "wynst", "ergze"]
    alienlistshort = [word for word in shortList if any(v in word for v in vowel)]

    novowelList = list(set(alienList) - set(alienlistshort))

    directorname = []
    for i in (alienlistshort):
        directorname.append(i[:3])
    directorname[0:2] = [''.join(directorname[0:2])]
    directorname[1:4] = [''.join(directorname[1:4])]
    del actor_list[2]
    del actor_list[5]
    output(alienlistshort,actor_list,directorname)
    
# output provides all the elements in lists that are required   
def output(alienlistshort,actor_list,directorname):
    print(*directorname, sep = ", ")
    print("Presents")
    print("Space Beyond!")

    actor = "Actor names:"
    print(actor + ', '.join(actor_list))
    character ="Alien names:"
    print(character + ', '.join(alienlistshort))

    print("The following lists were used:",
          "actor_list,",
          "aliennamelist,",
          "split_list,",
          "familyNamelist,",
          "givenNamelist,",
          "family3list,",
          "given2List,",
          "alienlist,",
          "shortlist,",
          "alienlistshort,",
          "novowelList and",
          "directorname")
    
    

# contains the actor list and passes this to the first function
def main():
    actor_list = ["andrei stephens",
                  "harry venables",
                  "phillipa blythe",
                  "yuan spield",
                  "sadiq elbahi",
                  "stephanie wynne",
                  "zeng ergan"]
    aliennamelist = create_actor(actor_list)
    
    
main()
