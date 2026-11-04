import os
def text_loading():
    dialogue={}
    for i in os.listdir("text"):
        dialogue[i]={}
        texts=os.path.join("text",i)
        with open (texts,"r") as dial:
            dialogue_in=0
            for t in dial:
                dialogue[i][dialogue_in]=t
                dialogue_in+=1

                print(t,"\n")
    return dialogue

