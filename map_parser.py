import sys,os,re

def Search(InputComponents):

    for component in InputComponents:
        mapFile=open('Memory_Map_File.map','r')
        regex=r'(\w+)(\s+)(.rodata|.data|.bss|.text)(\s+)'+'('+component+')'+'(\w+)'
        AllLists = re.findall(regex,mapFile.read())
        print(AllLists)
        
        #make list of needed data of each component
        myList=[]
        for list in  AllLists:
            #memory section
            myList.append(list[2])
            #size of memory section of each component
            myList.append(int(list[0],16))
        print(myList)
        
        #make dict of needed data of each component        
        dict={}
        i=0
        while i in range(len(myList)):
            if myList[i] not in(dict.keys()):
                dict[myList[i]]=myList[i+1]               
            else:
                dict[myList[i]]+=myList[i+1] 
                
            i+=2            
        print(dict)   
                
        ROMSize=0
        RAMSize=0      
        for key,value in dict.items():
            if(key=='.text' or key=='.rodata'):
               ROMSize+=value               
            else:
               RAMSize+=value
               
        if(".text" not in dict):
           dict[".text"]=0
        if(".rodata" not in dict):
           dict[".rodata"]=0  
        if(".data" not in dict):
           dict[".data"]=0
        if(".bss" not in dict):
           dict[".bss"]=0 
           
        #WRITING DATA IN THE FILE 
        file=open(component+'.txt','w')
        file.write('\n\n\t***** '+ component +' component Info *****\n\n')        
        file.write('Size of .text   section in '+component+' component is = '+str(dict[".text"]) + ' Bytes\n')
        file.write('Size of .rodata section in '+component+' component is = '+str(dict[".rodata"]) + ' Bytes\n\n')
        file.write('Size of .data   section in '+component+' component is = '+str(dict[".data"]) + ' Bytes\n')
        file.write('Size of .bss    section in '+component+' component is = '+str(dict[".bss"]) + ' Bytes\n\n')  
        file.write('\n-> Size of ROM in '+component+' component is = '+str(ROMSize)+ ' Bytes\n')
        file.write('-> Size of RAM in '+component+' component is = '+str(RAMSize)+ ' Bytes\n')
        
        print(component+'_info file is created')
        file.close()
        mapFile.close()



def main():
    if(len(sys.argv)==1):
        print("Please parse components name.........")
        
    else:
        Components=[]
        for i in range(1,len(sys.argv)):
            mapFile=open('Memory_Map_File.map','r')
            #search for component name if exist or not 
            regex=r'(\w+)(\s+)(.rodata|.data|.bss|.text)(\s+)'+'('+sys.argv[i]+')'+'(\w+)'
            result = re.findall(regex,mapFile.read())
            if(len(result)>0):
                Components.append(sys.argv[i])
            else:
                print(sys.argv[i]+' is incorrect component name')
        #call Search function to find the data of each component and calculate the size of each section in the memory        
        Search(Components)        


if __name__ == '__main__':
  main() 
  
